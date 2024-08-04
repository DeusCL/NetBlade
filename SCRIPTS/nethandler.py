import netfuncs # type: ignore
import random

# If the game is opened for the first time and the current map is "Casa"
# that means that

def check_net_state():
	if Bladex.GetCurrentMap() == "Casa": # type: ignore
		netfuncs.set_net_keystate('NET_STATE', 0)
		return

	net_state = netfuncs.get_net_state()

	if not net_state['NET_STATE']:
		return

	addr = (net_state['SERVER'], net_state['PORT'])

	nick = net_state['NICK']
	kind = net_state['KIND']

	client = netfuncs.Client(nick, kind)
	client.connect(addr)


check_net_state()

