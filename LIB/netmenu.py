import netfuncs
import Bladex



def get_input_nick():
	net_state = netfuncs.get_net_state()
	return net_state['NICK']


def set_input_nick(txt):
	netfuncs.set_net_keystate('NICK', txt)


def get_input_ip():
	net_state = netfuncs.get_net_state()
	return net_state['SERVER']


def set_input_ip(txt):
	netfuncs.set_net_keystate('SERVER', txt)


def get_input_port():
	net_state = netfuncs.get_net_state()
	return str(net_state['PORT'])


def set_input_port(txt):
	try:
		port = int(txt)
	except ValueError:
		return

	netfuncs.set_net_keystate('PORT', port)


def request_failed(content):
	""" Callback function from netfuncs.Client.request_join
	This is called when the player tries to join a specified address and got
	rejected, denied, failed or something. """

	print("Supreme F in the chat: "+str(content))


def request_granted(content):
	""" Callback function from netfuncs.Client.request_join
	This is called when the player tries to join a specified address and
	succedeed. """
	netfuncs.set_net_keystate('NET_STATE', 1)

	Bladex.LoadLevel(content)


def connect_to_server(option):
	""" Option to connect to server, called from the script Menu in the
	Multiplayer option """

	net_state = netfuncs.get_net_state()
	addr = (net_state['SERVER'], net_state['PORT'])

	if net_state['NET_STATE']:
		Bladex.LoadLevel(Bladex.GetCurrentMap())

	client = netfuncs.Client()
	client.request_join(addr, request_failed, request_granted)

