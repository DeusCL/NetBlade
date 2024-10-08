"""RFC-822 message manipulation class.

XXX This is only a very rough sketch of a full RFC-822 parser;
in particular the tokenizing of addresses does not adhere to all the
quoting rules.

Directions for use:

To create a Message object: first open a file, e.g.:
  fp = open(file, 'r')
(or use any other legal way of getting an open file object, e.g. use
sys.stdin or call os.popen()).
Then pass the open file object to the Message() constructor:
  m = Message(fp)

To get the text of a particular header there are several methods:
  str = m.getheader(name)
  str = m.getrawheader(name)
where name is the name of the header, e.g. 'Subject'.
The difference is that getheader() strips the leading and trailing
whitespace, while getrawheader() doesn't.  Both functions retain
embedded whitespace (including newlines) exactly as they are
specified in the header, and leave the case of the text unchanged.

For addresses and address lists there are functions
  realname, mailaddress = m.getaddr(name) and
  list = m.getaddrlist(name)
where the latter returns a list of (realname, mailaddr) tuples.

There is also a method
  time = m.getdate(name)
which parses a Date-like field and returns a time-compatible tuple,
i.e. a tuple such as returned by time.localtime() or accepted by
time.mktime().

See the class definition for lower level access methods.

There are also some utility functions here.
"""

import string
import time


_blanklines = ('\r\n', '\n')            # Optimization for islast()


class Message:
    """Represents a single RFC-822-compliant message."""
    
    def __init__(self, fp, seekable = 1):
        """Initialize the class instance and read the headers."""
        self.fp = fp
        self.seekable = seekable
        self.startofheaders = None
        self.startofbody = None
        #
        if self.seekable:
            try:
                self.startofheaders = self.fp.tell()
            except IOError:
                self.seekable = 0
        #
        self.readheaders()
        #
        if self.seekable:
            try:
                self.startofbody = self.fp.tell()
            except IOError:
                self.seekable = 0
    
    def rewindbody(self):
        """Rewind the file to the start of the body (if seekable)."""
        if not self.seekable:
            raise IOError, "unseekable file"
        self.fp.seek(self.startofbody)
    
    def readheaders(self):
        """Read header lines.
        
        Read header lines up to the entirely blank line that
        terminates them.  The (normally blank) line that ends the
        headers is skipped, but not included in the returned list.
        If a non-header line ends the headers, (which is an error),
        an attempt is made to backspace over it; it is never
        included in the returned list.
        
        The variable self.status is set to the empty string if all
        went well, otherwise it is an error message.
        The variable self.headers is a completely uninterpreted list
        of lines contained in the header (so printing them will
        reproduce the header exactly as it appears in the file).
        """
        self.dict = {}
        self.unixfrom = ''
        self.headers = list = []
        self.status = ''
        headerseen = ""
        firstline = 1
        while 1:
            line = self.fp.readline()
            if not line:
                self.status = 'EOF in headers'
                break
            # Skip unix From name time lines
            if firstline and line[:5] == 'From ':
                self.unixfrom = self.unixfrom + line
                continue
            firstline = 0
            if self.islast(line):
                break
            elif headerseen and line[0] in ' \t':
                # It's a continuation line.
                list.append(line)
                x = (self.dict[headerseen] + "\n " +
                string.strip(line))
                self.dict[headerseen] = string.strip(x)
            elif ':' in line:
                # It's a header line.
                list.append(line)
                i = string.find(line, ':')
                headerseen = string.lower(line[:i])
                self.dict[headerseen] = string.strip(
                line[i+1:])
            else:
                # It's not a header line; stop here.
                if not headerseen:
                    self.status = 'No headers'
                else:
                    self.status = 'Bad header'
                # Try to undo the read.
                if self.seekable:
                    self.fp.seek(-len(line), 1)
                else:
                    self.status = \
                                                self.status + '; bad seek'
                break
    
    def islast(self, line):
        """Determine whether a line is a legal end of RFC-822 headers.
        
        You may override this method if your application wants
        to bend the rules, e.g. to strip trailing whitespace,
        or to recognise MH template separators ('--------').
        For convenience (e.g. for code reading from sockets) a
        line consisting of \r\n also matches.                
        """
        return line in _blanklines
    
    def getallmatchingheaders(self, name):
        """Find all header lines matching a given header name.
        
        Look through the list of headers and find all lines
        matching a given header name (and their continuation
        lines).  A list of the lines is returned, without
        interpretation.  If the header does not occur, an
        empty list is returned.  If the header occurs multiple
        times, all occurrences are returned.  Case is not
        important in the header name.
        """
        name = string.lower(name) + ':'
        n = len(name)
        list = []
        hit = 0
        for line in self.headers:
            if string.lower(line[:n]) == name:
                hit = 1
            elif line[:1] not in string.whitespace:
                hit = 0
            if hit:
                list.append(line)
        return list
    
    def getfirstmatchingheader(self, name):
        """Get the first header line matching name.
        
        This is similar to getallmatchingheaders, but it returns
        only the first matching header (and its continuation
        lines).
        """
        name = string.lower(name) + ':'
        n = len(name)
        list = []
        hit = 0
        for line in self.headers:
            if hit:
                if line[:1] not in string.whitespace:
                    break
            elif string.lower(line[:n]) == name:
                hit = 1
            if hit:
                list.append(line)
        return list
    
    def getrawheader(self, name):
        """A higher-level interface to getfirstmatchingheader().
        
        Return a string containing the literal text of the
        header but with the keyword stripped.  All leading,
        trailing and embedded whitespace is kept in the
        string, however.
        Return None if the header does not occur.
        """
        
        list = self.getfirstmatchingheader(name)
        if not list:
            return None
        list[0] = list[0][len(name) + 1:]
        return string.joinfields(list, '')
    
    def getheader(self, name):
        """Get the header value for a name.
        
        This is the normal interface: it return a stripped
        version of the header value for a given header name,
        or None if it doesn't exist.  This uses the dictionary
        version which finds the *last* such header.
        """
        try:
            return self.dict[string.lower(name)]
        except KeyError:
            return None
    
    def getaddr(self, name):
        """Get a single address from a header, as a tuple.
        
        An example return value:
        ('Guido van Rossum', 'guido@cwi.nl')
        """
        # New, by Ben Escoto
        alist = self.getaddrlist(name)
        if alist:
            return alist[0]
        else:
            return (None, None)
    
    def getaddrlist(self, name):
        """Get a list of addresses from a header.
        
        Retrieves a list of addresses from a header, where each
        address is a tuple as returned by getaddr().
        """
        # New, by Ben Escoto
        try:
            data = self[name]
        except KeyError:
            return []
        a = AddrlistClass(data)
        return a.getaddrlist()
    
    def getdate(self, name):
        """Retrieve a date field from a header.
        
        Retrieves a date field from the named header, returning
        a tuple compatible with time.mktime().
        """
        try:
            data = self[name]
        except KeyError:
            return None
        return parsedate(data)
    
    def getdate_tz(self, name):
        """Retrieve a date field from a header as a 10-tuple.
        
        The first 9 elements make up a tuple compatible with
        time.mktime(), and the 10th is the offset of the poster's
        time zone from GMT/UTC.
        """
        try:
            data = self[name]
        except KeyError:
            return None
        return parsedate_tz(data)
    
    
    # Access as a dictionary (only finds *last* header of each type):
    
    def __len__(self):
        """Get the number of headers in a message."""
        return len(self.dict)
    
    def __getitem__(self, name):
        """Get a specific header, as from a dictionary."""
        return self.dict[string.lower(name)]
    
    def __delitem__(self, name):
        """Delete all occurrences of a specific header, if it is present."""
        name = string.lower(name)
        if not self.dict.has_key(name):
            return
        del self.dict[name]
        name = name + ':'
        n = len(name)
        list = []
        hit = 0
        for i in range(len(self.headers)):
            line = self.headers[i]
            if string.lower(line[:n]) == name:
                hit = 1
            elif line[:1] not in string.whitespace:
                hit = 0
            if hit:
                list.append(i)
        list.reverse()
        for i in list:
            del self.headers[i]

    def has_key(self, name):
        """Determine whether a message contains the named header."""
        return self.dict.has_key(string.lower(name))
    
    def keys(self):
        """Get all of a message's header field names."""
        return self.dict.keys()
    
    def values(self):
        """Get all of a message's header field values."""
        return self.dict.values()
    
    def items(self):
        """Get all of a message's headers.
        
        Returns a list of name, value tuples.
        """
        return self.dict.items()



# Utility functions
# -----------------

# XXX Should fix unquote() and quote() to be really conformant.
# XXX The inverses of the parse functions may also be useful.


def unquote(str):
    """Remove quotes from a string."""
    if len(str) > 1:
        if str[0] == '"' and str[-1:] == '"':
            return str[1:-1]
        if str[0] == '<' and str[-1:] == '>':
            return str[1:-1]
    return str


def quote(str):
    """Add quotes around a string."""
    return '"%s"' % string.join(
    string.split(
    string.join(
    string.split(str, '\\'),
    '\\\\'),
    '"'),
    '\\"')


def parseaddr(address):
    """Parse an address into a (realname, mailaddr) tuple."""
    a = AddrlistClass(address)
    list = a.getaddrlist()
    if not list:
        return (None, None)
    else:
        return list[0]


class AddrlistClass:
    """Address parser class by Ben Escoto.
    
    To understand what this class does, it helps to have a copy of
    RFC-822 in front of you.
    """
    
    def __init__(self, field):
        """Initialize a new instance.
        
        `field' is an unparsed address header field, containing
        one or more addresses.
        """
        self.specials = '()<>@,:;.\"[]'
        self.pos = 0
        self.LWS = ' \t'
        self.CR = '\r'
        self.atomends = self.specials + self.LWS + self.CR
        
        self.field = field
        self.commentlist = []
    
    def gotonext(self):
        """Parse up to the start of the next address."""
        while self.pos < len(self.field):
            if self.field[self.pos] in self.LWS + '\n\r':
                self.pos = self.pos + 1
            elif self.field[self.pos] == '(':
                self.commentlist.append(self.getcomment())
            else: break
    
    def getaddrlist(self):
        """Parse all addresses.
        
        Returns a list containing all of the addresses.
        """
        ad = self.getaddress()
        if ad:
            return ad + self.getaddrlist()
        else: return []
    
    def getaddress(self):
        """Parse the next address."""
        self.commentlist = []
        self.gotonext()
        
        oldpos = self.pos
        oldcl = self.commentlist
        plist = self.getphraselist()
        
        self.gotonext()
        returnlist = []
        
        if self.pos >= len(self.field):
            # Bad email address technically, no domain.
            if plist:
                returnlist = [(string.join(self.commentlist), plist[0])]
            
        elif self.field[self.pos] in '.@':
            # email address is just an addrspec
            # this isn't very efficient since we start over
            self.pos = oldpos
            self.commentlist = oldcl
            addrspec = self.getaddrspec()
            returnlist = [(string.join(self.commentlist), addrspec)]
            
        elif self.field[self.pos] == ':':
            # address is a group
            returnlist = []
            
            self.pos = self.pos + 1
            while self.pos < len(self.field):
                self.gotonext()
                if self.field[self.pos] == ';':
                    self.pos = self.pos + 1
                    break
                returnlist = returnlist + self.getaddress()
            
        elif self.field[self.pos] == '<':
            # Address is a phrase then a route addr
            routeaddr = self.getrouteaddr()
            
            if self.commentlist:
                returnlist = [(string.join(plist) + ' (' + \
                         string.join(self.commentlist) + ')', routeaddr)]
            else: returnlist = [(string.join(plist), routeaddr)]
            
        else:
            if plist:
                returnlist = [(string.join(self.commentlist), plist[0])]
        
        self.gotonext()
        if self.pos < len(self.field) and self.field[self.pos] == ',':
            self.pos = self.pos + 1
        return returnlist
    
    def getrouteaddr(self):
        """Parse a route address (Return-path value).
        
        This method just skips all the route stuff and returns the addrspec.
        """
        if self.field[self.pos] != '<':
            return
        
        expectroute = 0
        self.pos = self.pos + 1
        self.gotonext()
        adlist = None
        while self.pos < len(self.field):
            if expectroute:
                self.getdomain()
                expectroute = 0
            elif self.field[self.pos] == '>':
                self.pos = self.pos + 1
                break
            elif self.field[self.pos] == '@':
                self.pos = self.pos + 1
                expectroute = 1
            elif self.field[self.pos] == ':':
                self.pos = self.pos + 1
                expectaddrspec = 1
            else:
                adlist = self.getaddrspec()
                self.pos = self.pos + 1
                break
            self.gotonext()
        
        return adlist
    
    def getaddrspec(self):
        """Parse an RFC-822 addr-spec."""
        aslist = []
        
        self.gotonext()
        while self.pos < len(self.field):
            if self.field[self.pos] == '.':
                aslist.append('.')
                self.pos = self.pos + 1
            elif self.field[self.pos] == '"':
                aslist.append(self.getquote())
            elif self.field[self.pos] in self.atomends:
                break
            else: aslist.append(self.getatom())
            self.gotonext()
        
        if self.pos >= len(self.field) or self.field[self.pos] != '@':
            return string.join(aslist, '')
        
        aslist.append('@')
        self.pos = self.pos + 1
        self.gotonext()
        return string.join(aslist, '') + self.getdomain()
    
    def getdomain(self):
        """Get the complete domain name from an address."""
        sdlist = []
        while self.pos < len(self.field):
            if self.field[self.pos] in self.LWS:
                self.pos = self.pos + 1
            elif self.field[self.pos] == '(':
                self.commentlist.append(self.getcomment())
            elif self.field[self.pos] == '[':
                sdlist.append(self.getdomainliteral())
            elif self.field[self.pos] == '.':
                self.pos = self.pos + 1
                sdlist.append('.')
            elif self.field[self.pos] in self.atomends:
                break
            else: sdlist.append(self.getatom())
        
        return string.join(sdlist, '')
    
    def getdelimited(self, beginchar, endchars, allowcomments = 1):
        """Parse a header fragment delimited by special characters.
        
        `beginchar' is the start character for the fragment.
        If self is not looking at an instance of `beginchar' then
        getdelimited returns the empty string.
        
        `endchars' is a sequence of allowable end-delimiting characters.
        Parsing stops when one of these is encountered.
        
        If `allowcomments' is non-zero, embedded RFC-822 comments
        are allowed within the parsed fragment.
        """
        if self.field[self.pos] != beginchar:
            return ''
        
        slist = ['']
        quote = 0
        self.pos = self.pos + 1
        while self.pos < len(self.field):
            if quote == 1:
                slist.append(self.field[self.pos])
                quote = 0
            elif self.field[self.pos] in endchars:
                self.pos = self.pos + 1
                break
            elif allowcomments and self.field[self.pos] == '(':
                slist.append(self.getcomment())
            elif self.field[self.pos] == '\\':
                quote = 1
            else:
                slist.append(self.field[self.pos])
            self.pos = self.pos + 1
        
        return string.join(slist, '')
    
    def getquote(self):
        """Get a quote-delimited fragment from self's field."""
        return self.getdelimited('"', '"\r', 0)
    
    def getcomment(self):
        """Get a parenthesis-delimited fragment from self's field."""
        return self.getdelimited('(', ')\r', 1)
    
    def getdomainliteral(self):
        """Parse an RFC-822 domain-literal."""
        return self.getdelimited('[', ']\r', 0)
    
    def getatom(self):
        """Parse an RFC-822 atom."""
        atomlist = ['']
        
        while self.pos < len(self.field):
            if self.field[self.pos] in self.atomends:
                break
            else: atomlist.append(self.field[self.pos])
            self.pos = self.pos + 1
        
        return string.join(atomlist, '')
    
    def getphraselist(self):
        """Parse a sequence of RFC-822 phrases.
        
        A phrase is a sequence of words, which are in turn either
        RFC-822 atoms or quoted-strings.
        """
        plist = []
        
        while self.pos < len(self.field):
            if self.field[self.pos] in self.LWS:
                self.pos = self.pos + 1
            elif self.field[self.pos] == '"':
                plist.append(self.getquote())
            elif self.field[self.pos] == '(':
                self.commentlist.append(self.getcomment())
            elif self.field[self.pos] in self.atomends:
                break
            else: plist.append(self.getatom())
        
        return plist


# Parse a date field

_monthnames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
               'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
_daynames = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# The timezone table does not include the military time zones defined
# in RFC822, other than Z.  According to RFC1123, the description in
# RFC822 gets the signs wrong, so we can't rely on any such time
# zones.  RFC1123 recommends that numeric timezone indicators be used
# instead of timezone names.

_timezones = {'UT':0, 'UTC':0, 'GMT':0, 'Z':0, 
              'AST': -400, 'ADT': -300,  # Atlantic standard
              'EST': -500, 'EDT': -400,  # Eastern
              'CST': -600, 'CDT':-500,   # Centreal
              'MST':-700, 'MDT':-600,    # Mountain
              'PST':-800, 'PDT':-700     # Pacific
              }    


def parsedate_tz(data):
    """Convert a date string to a time tuple.
    
    Accounts for military timezones.
    """
    data = string.split(data)
    if data[0][-1] == ',' or data[0] in _daynames:
        # There's a dayname here. Skip it
        del data[0]
    if len(data) == 3: # RFC 850 date, deprecated
        stuff = string.split(data[0], '-')
        if len(stuff) == 3:
            data = stuff + data[1:]
    if len(data) == 4:
        s = data[3]
        i = string.find(s, '+')
        if i > 0:
            data[3:] = [s[:i], s[i+1:]]
        else:
            data.append('') # Dummy tz
    if len(data) < 5:
        return None
    data = data[:5]
    [dd, mm, yy, tm, tz] = data
    if not mm in _monthnames:
        dd, mm, yy, tm, tz = mm, dd, tm, yy, tz
        if not mm in _monthnames:
            return None
    mm = _monthnames.index(mm)+1
    tm = string.splitfields(tm, ':')
    if len(tm) == 2:
        [thh, tmm] = tm
        tss = '0'
    else:
        [thh, tmm, tss] = tm
    try:
        yy = string.atoi(yy)
        dd = string.atoi(dd)
        thh = string.atoi(thh)
        tmm = string.atoi(tmm)
        tss = string.atoi(tss)
    except string.atoi_error:
        return None
    tzoffset=None
    tz=string.upper(tz)
    if _timezones.has_key(tz):
        tzoffset=_timezones[tz]
    else:
        try: 
            tzoffset=string.atoi(tz)
        except string.atoi_error: 
            pass
    # Convert a timezone offset into seconds ; -0500 -> -18000
    if tzoffset:
        if tzoffset < 0:
            tzsign = -1
            tzoffset = -tzoffset
        else:
            tzsign = 1
        tzoffset = tzsign * ( (tzoffset/100)*3600 + (tzoffset % 100)*60)
    tuple = (yy, mm, dd, thh, tmm, tss, 0, 0, 0, tzoffset)
    return tuple


def parsedate(data):
    """Convert a time string to a time tuple."""
    t=parsedate_tz(data)
    if type(t)==type( () ):
        return t[:9]
    else: return t    


def mktime_tz(data):
    """Turn a 10-tuple as returned by parsedate_tz() into a UTC timestamp.
    
    Minor glitch: this first interprets the first 8 elements as a
    local time and then compensates for the timezone difference;
    this may yield a slight error around daylight savings time
    switch dates.  Not enough to worry about for common use.
    
    """
    if data[9] is None:
        # No zone info, so localtime is better assumption than GMT
        return time.mktime(data[:8] + (-1,))
    else:
        t = time.mktime(data[:8] + (0,))
        return t - data[9] - time.timezone


# When used as script, run a small test program.
# The first command line argument must be a filename containing one
# message in RFC-822 format.

if __name__ == '__main__':
    import sys, os
    file = os.path.join(os.environ['HOME'], 'Mail/inbox/1')
    if sys.argv[1:]: file = sys.argv[1]
    f = open(file, 'r')
    m = Message(f)
    print 'From:', m.getaddr('from')
    print 'To:', m.getaddrlist('to')
    print 'Subject:', m.getheader('subject')
    print 'Date:', m.getheader('date')
    date = m.getdate_tz('date')
    if date:
        print 'ParsedDate:', time.asctime(date[:-1]),
        hhmmss = date[-1]
        hhmm, ss = divmod(hhmmss, 60)
        hh, mm = divmod(hhmm, 60)
        print "%+03d%02d" % (hh, mm),
        if ss: print ".%02d" % ss,
        print
    else:
        print 'ParsedDate:', None
    m.rewindbody()
    n = 0
    while f.readline():
        n = n + 1
    print 'Lines:', n
    print '-'*70
    print 'len =', len(m)
    if m.has_key('Date'): print 'Date =', m['Date']
    if m.has_key('X-Nonsense'): pass
    print 'keys =', m.keys()
    print 'values =', m.values()
    print 'items =', m.items()
