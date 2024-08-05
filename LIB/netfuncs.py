import socket
import threading
import pickle
import string
import random
import time
import os
import math
import traceback

import Bladex
import Reference
import ItemTypes
import Actions

import netplayer

# NetState Game configuration file
# This file is deleteable
NET_FILEPATH = '..\\..\\Config\\net_state.cfg'

# The Default configuration of the NetState
# This method needs to be updated soon
DEFAULT_NET_STATE = {
	'PORT': '49500',
	'SERVER': '',
	'NICK': '',
	'NET_STATE': 0,
	'KIND': 'Knight_N'
}

# Used to find the entities that were created to display remote entities
FOREIGN_ENTITY_PREFIX = "_foreign_"

# Never used
HEADER = 8

# Used to fit the data being sent in this amount of bytes
FULL_HEADER = 512

# Used to receive data of foreign entities and update them in this amount of times per second
TPS = 30

# Never used
DT = 1/60.0


class Client:
	def __init__(self, nick='', kind='Knight_N'):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.kind = kind

		self.nick = nick
		if nick == '':
			self.nick = generate_funny_nickname()

		self.local_player = None

		# Actions: A set of actions performed by the player in the most recent frame
		# before this set was sent to the server
		self.actions = {}
		self.char_last_anim = ""
		self.connected = 0
		self.compact_info = 1
		self.last_action = None


	def request_join(self, addr, failure_func, sucksess_funk):
		# Trata de establecer conexión con el servidor
		try:
			self.sock.connect(addr)
		except socket.error:
			failure_func("Socket Error")
			return
		except:
			failure_func("Invalid Address")
			return
		# Conexión establecida!


		# Envía mensaje al servidor pidiendo permiso para ingresar
		self.send_data({'msg':'REQ'})


		# Se queda bloqueado esperando la respuesta del servidor
		sock = self.sock.dup()
		sock.setblocking(0)

		time_init = time.time()

		while 1:
			if time.time() - time_init > 3:
				sock.close()
				self.sock.close()
				failure_func("sock.error")
				return

			try:
				msg = sock.recv(FULL_HEADER)
			except socket.error:
				continue

			break

		# Respuesta recibida!
		# Ya no necesitamos tener estas mugres
		sock.close()
		self.sock.close()

		print("Message received: " + str(msg))


		# Tratando de descifrar los datos recibidos
		try:
			response_data = eval(msg)
		except Exception:
			failure_func("eval.error")
			return
		# Mensaje descifrado con éxito!


		# Iniciando acciones de acuerdo a la respuesta recibida
		msg = response_data['msg']

		print("Response data: "+str(msg))

		if msg == 'denied':
			# Callback to the failure func :(
			failure_func(response_data['content'])
		elif msg == 'granted':
			# Callback to the success func!
			sucksess_funk(response_data['content'])

	def connect(self, addr):
		if self.connected:
			return

		try:
			self.sock.connect(addr)
		except socket.error:
			#ShowMessage("Error connecting")
			Bladex.LoadLevel("Casa")
			return

		self.send_data({'msg':'JOIN'})

		self.on_connect()


	def LoadLevel(self, level):
		self.close()
		self.aux_LoadLevel(level)


	def on_connect(self):
		self.connected = 1

		########## Change Some Funcs
		# Change Bladex LoadLevel func to check when the player is leaving this world
		self.aux_LoadLevel = Bladex.LoadLevel
		Bladex.LoadLevel = self.LoadLevel

		# This is to check when the player drops or throws an object
		self.aux_DropReleaseEventHandler = Actions.DropReleaseEventHandler
		self.aux_ThrowReleaseEventHandler = Actions.ThrowReleaseEventHandler

		Actions.DropReleaseEventHandler = self.DropReleaseEventHandler
		Actions.ThrowReleaseEventHandler = self.ThrowReleaseEventHandler

		# This is to check when the player takes an object
		self.aux_PickupEventHandler = Actions.PickupEventHandler
		Actions.PickupEventHandler = self.PickupEventHandler


		# Send initial player data
		data = {
			'nick': self.nick,
			'kind': self.kind,
			'msg': 'IPD'
		}

		self.send_data(data)

		# Start the data sender, looped by Bladex.AddScheduledFunc
		self.send_player_data()

		# Start the data receiver in another thread
		threading.Thread(target=self.data_receiver).start()


	def send_player_data(self):
		if self.connected:
			Bladex.AddScheduledFunc(Bladex.GetTime()+1/float(TPS), self.send_player_data, ())

		if not self.local_player:
			char = Bladex.GetEntity("Player1")
			if not char:
				return

			self.local_player = char

		char = self.local_player

		inventory = get_char_inv(char)

		x, y, z = char.Position
		pos = (round(x, 2), round(y, 2), round(z, 2))
		ang = round(char.Angle, 2)

		# Compact data system (working well)
		# d: is meant for the "data" of the player that will be sent
		data = {
			'd':(
				pos, ang, char.Life, char.Level,
				(char.Gof, char.Gob, char.Run, char.Sneak),
				self.actions, char.AnimName, inventory
			),
			'msg':'PPD'
		}

		self.actions = {}

		self.send_data(data, self.compact_info)


	def PickupEventHandler(self, entity_name, event_name, force_take=1):
		self.aux_PickupEventHandler(entity_name, event_name, force_take)
		if entity_name == "Player1":
			me = Bladex.GetEntity(entity_name)
			obj_name = me.Data.pickup_entity
			self.actions.update({'pickup':obj_name})


	def DropReleaseEventHandler(self, entity_name, event_name, test_hit=1):
		""" Catch this action for every entity in the world """
		obj = None

		if entity_name == "Player1":
			me = Bladex.GetEntity(entity_name)

			if event_name == "DropLeftEvent":
				obj = Bladex.GetEntity(me.InvLeft)
			else:
				obj = Bladex.GetEntity(me.InvRight)

		self.aux_DropReleaseEventHandler(entity_name, event_name, test_hit)

		if obj:
			name = obj.Name
			kind = obj.Kind
			pos = obj.Position
			orientation = obj.Orientation
			weapon = obj.Weapon
			vel = obj.Velocity
			ang_vel = obj.AngularVelocity

			self.actions.update({'drp':(name, kind, pos, orientation, weapon, vel, ang_vel, 'drp')})


	def ThrowReleaseEventHandler(self, entity_name, event_name):
		""" Catch this action for every entity in the world """
		obj = None

		if entity_name == "Player1":
			me = Bladex.GetEntity(entity_name)

			if event_name == "ThrowLeftEvent":
				if me.InvLeft == "None" or not me.InvLeft:
					return

				obj = Bladex.GetEntity(me.InvLeft)

			else:
				if me.InvRight == "None" or not me.InvRight:
					return

				obj = Bladex.GetEntity(me.InvRight)

		self.aux_ThrowReleaseEventHandler(entity_name, event_name)

		if obj:
			name = obj.Name
			kind = obj.Kind
			pos = obj.Position
			orientation = obj.Orientation
			weapon = obj.Weapon
			vel = obj.Velocity
			ang_vel = obj.AngularVelocity

			self.actions.update({'drp':(name, kind, pos, orientation, weapon, vel, ang_vel, event_name)})



	def send_data(self, data, compact=0):
		str_data = str(data)
		if compact:
			str_data = string.replace(str_data, ' ', '')
		self.send_msg(str_data)


	def send_msg(self, msg):
		msg = msg + ' '*(FULL_HEADER - len(msg))
		try:
			self.sock.send(msg)
		except socket.error:
			self.close()


	def close(self):
		self.connected = 0
		try:
			self.send_data({'msg':'DIS'})
		except socket.error:
			pass
		self.sock.close()


	def data_receiver(self):
		sock = self.sock.dup()
		sock.setblocking(0)

		while self.connected:
			try:
				str_data = sock.recv(FULL_HEADER)
			except socket.error:
				continue

			try:
				data = eval(str_data)
			except Exception:
				continue

			# Handle the data received
			self.process_data(data)


	def process_data(self, data):
		if 'msg' in data.keys():
			msg_type = data['msg']

			if msg_type == 'disconnection':
				nick = data['content']

				gil = Bladex.GetEntity(FOREIGN_ENTITY_PREFIX+nick)
				if not gil: return

				try:
					gil.Data.active = 0
				except:
					pass

				Bladex.AddScheduledFunc(Bladex.GetTime(), gil.SubscribeToList, ("Pin",))

				#ShowMessage(nick + " left the game")

			return

		for nick in data.keys():
			player_data = data[nick]
			Bladex.AddScheduledFunc(Bladex.GetTime(), self.update_netplayer, (nick, player_data,))


	def update_netplayer(self, nick, player_data):
		if len(player_data) <= 1:
			return

		# Unpack the player data
		pos, ang, life, level, mov, acts, anm, inv = player_data['d']


		# Create a entity named like the foriegn player
		x, y, z = pos
		entity_name = FOREIGN_ENTITY_PREFIX+nick
		pers = Bladex.GetEntity(entity_name)
		if not pers:
			kind = player_data['kind']
			pers = Bladex.CreateEntity(entity_name, kind, x, y, z, "Person")
			pers.Data = netplayer.NetPlayer(pers, nick)


		# Sets the target position and angle to be updated smoothly by the
		# netplayer.NetPlayer.main_loop() function. (pers.Data)
		pers.Data.target_pos = pos
		pers.Data.target_ang = ang
		pers.Data.target_anm = anm


		# Update life and level
		pers.Life = life
		pers.Level = level


		# Update char movement status
		gof, gob, run, snk = mov
		pers.Gof = gof
		pers.Gob = gob
		pers.Run = run
		pers.Sneak = snk



		# Update inventory
		received_inv = inv
		pers_inv = get_char_inv(pers, kinds=0)

		inv = pers.GetInventory()

		for slot in ['l', 'r', 'lb', 'rb']:
			update_inv2(pers, inv, pers_inv, received_inv, slot)


		# Manage actions
		if acts == self.last_action:
			# Prevent duplicated actions like throwing the same object twice
			return

		self.last_action = acts

		if 'drp' in acts.keys():
			self.action_drp(pers, inv, acts['drp'])

		if 'pickup' in acts.keys():
			obj_name = acts['pickup']
			del acts['pickup']
			self.action_pickup(obj_name)


	def action_drp(self, pers, inv, drp_data):
		""" Drop/Throw Action Manager. For when a non local player throws
		or drops an object. """

		name, kind, wpos, orientation, weapon, vel, ang_vel, event_name = drp_data

		obj = Bladex.GetEntity(name)

		if not obj:
			if weapon:
				obj = Bladex.CreateEntity(name, kind, 0, 0, 0, "Weapon")
				ItemTypes.ItemDefaultFuncs(obj)
			else:
				obj = Bladex.CreateEntity(name, kind, 0, 0, 0)
		else:
			if obj.Kind != kind or obj.Parent:
				if weapon:
					obj = Bladex.CreateEntity(name+"2", kind, 0, 0, 0, "Weapon")
					ItemTypes.ItemDefaultFuncs(obj)
				else:
					obj = Bladex.CreateEntity(name+"2", kind, 0, 0, 0)


		obj.Position = wpos
		obj.Orientation = orientation

		if event_name[:5] == "Throw":

			try:
				obj_class = eval("ItemTypes."+kind)
			except:
				obj_class = None

			if obj.Data and "ThrowReleaseEventHandler" in dir(obj_class):
				prev_obj = Bladex.GetEntity(pers.InvRight)

				if prev_obj:
					inv.LinkRightHand('')
					prev_obj.SubscribeToList('Pin')

				inv.LinkRightHand(obj.Name)

				pers.Position = pos
				pers.Angle = ang

				pers.AddAnmEventFunc(event_name, obj.Data.ThrowReleaseEventHandler)

			else:
				obj.MessageEvent(Reference.MESSAGE_START_WEAPON, 0, 0)
				obj.MessageEvent(Reference.MESSAGE_START_TRAIL, 0, 0)

				obj.Impulse(0, 0, 0)

				obj.Velocity = vel
				obj.AngularVelocity = ang_vel

				Bladex.AddScheduledFunc(Bladex.GetTime()+2.0, Actions.ThrownWeaponStopFunc, (obj.Name,))

		else:

			Bladex.AddScheduledFunc(Bladex.GetTime()+0.01, drop_obj, (obj,))


	def action_pickup(self, obj_name):
		""" Pickup Action manager. For when a non local player picks up an object. """

		pickup_entity = Bladex.GetEntity(obj_name)

		if not pickup_entity:
			return

		object_flag = Reference.GiveObjectFlag(obj_name)

		if object_flag == Reference.OBJ_KEY:
			# If a non local player picks up a key, then, add it to the local player inventory too.
			inv = self.local_player.GetInventory()
			inv.AddKey(obj_name)

			self.local_player.Data.RegisterObjectAsTaken(obj_name)

			from Scorer import NewObjectAtInventory

			new_key_sound = Bladex.GetSound("NewKeySound")
			new_key_sound.PlayStereo()

			NewObjectAtInventory(obj_name)

		else:
			pickup_entity.Stop()
			pickup_entity.Position = 0, 1000000, 0


	def disconnect(self):
		self.load_level("Casa")



def update_inv2(pers, inv, pers_inv, received_inv, slot):
	my_obj = Bladex.GetEntity(pers_inv[slot])
	target_kind = received_inv[slot]
	active_weapon_kind = received_inv['aw']

	if my_obj:
		my_kind = my_obj.Kind

		if slot == 'r' and my_obj.Name[-6:] != '_inv_r':
			return

		if my_kind == target_kind:
			return

		if slot == 'r' and target_kind == '' and active_weapon_kind != '':
			return

		if slot == 'l':
			inv.LinkLeftHand('')
		if slot == 'r':
			inv.LinkRightHand('')
		if slot == 'lb':
			inv.LinkLeftBack('')
		if slot == 'rb':
			inv.LinkRightBack('')

		my_obj.SubscribeToList('Pin')

	if target_kind == '':
		return

	new_obj = Bladex.CreateEntity(pers.Name+'_inv_'+slot, target_kind, 0, 0, 0, 'Weapon')

	object_flag = Reference.GiveObjectFlag(new_obj.Name)

	if object_flag != Reference.OBJ_KEY:
		ItemTypes.ItemDefaultFuncs(new_obj)

	if slot == 'l':
		inv.LinkLeftHand(new_obj.Name)
	if slot == 'r':
		inv.LinkRightHand(new_obj.Name)
	if slot == 'lb':
		inv.LinkLeftBack(new_obj.Name)
	if slot == 'rb':
		inv.LinkRightBack(new_obj.Name)



def get_kind(name):
	if not name:
		return ''

	kind = ''
	w = Bladex.GetEntity(name)
	if w:
		if w.Person:
			return ''

		return w.Kind

	return kind


def get_char_inv(pers, kinds=1):
	inventory = {'aw':'', 'as':'', 'l':'', 'r':'', 'lb':'', 'rb':''}

	if not pers:
		return inventory

	inv = pers.GetInventory()

	if kinds:
		inventory['aw'] = get_kind(inv.GetActiveWeapon())
		inventory['as'] = get_kind(inv.GetActiveShield())
		inventory['l'] = get_kind(pers.InvLeft)
		inventory['r'] = get_kind(pers.InvRight)
		inventory['lb'] = get_kind(pers.InvLeftBack)
		inventory['rb'] = get_kind(pers.InvRightBack)

	if not kinds:
		inventory['aw'] = inv.GetActiveWeapon()
		inventory['as'] = inv.GetActiveShield()
		inventory['l'] = pers.InvLeft
		inventory['r'] = pers.InvRight
		inventory['lb'] = pers.InvLeftBack
		inventory['rb'] = pers.InvRightBack


	return inventory


def drop_obj(obj):
	obj.Impulse(0, 0, 0)

	obj.Velocity = vel
	obj.AngularVelocity = ang_vel




def get_net_state():
	if not os.path.exists(NET_FILEPATH):
		f = open(NET_FILEPATH, 'w')
		f.write(str(DEFAULT_NET_STATE))
		f.close()
		return DEFAULT_NET_STATE

	f = open(NET_FILEPATH, 'r')

	try:
		net_state = eval(f.read())
	except Exception:
		net_state = DEFAULT_NET_STATE

	f.close()

	return net_state


def set_net_keystate(key, value):
	net_state = get_net_state()
	net_state[key] = value
	set_net_state(net_state)


def set_net_state(net_state):
	f = open(NET_FILEPATH, 'w')
	f.write(str(net_state))
	f.close()



def gen_rand_name(prefix, length=10):
	rand_name = prefix

	for i in range(length):
		rand_name = rand_name + random.choice(string.letters+string.digits)

	print(rand_name)

	return rand_name


def ShowMessage(message="", r=255, g=255, b=255):
	"""
	Scorer.wGameText.SetText(message)
	Scorer.wGameText.SetAlpha(1.0)
	Scorer.wGameText.SetColor(r,g,b)
	Scorer.wFrame.RecalcLayout()
	"""
	pass


def generate_funny_nickname():
    adjectives = [
        "Silly", "Goofy", "Wacky", "Zany", "Quirky", "Loopy", "Nutty", "Funky", "Cheeky", "Bizarre"
    ]
    nouns = [
        "Banana", "Pancake", "Noodle", "Pickle", "Muffin", "Marshmallow", "Doodle", "Gizmo", "Whisker", "Wombat"
    ]

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    nickname = adjective + noun

    number = random.randint(0, 100)
    funny_nickname = nickname + str(number)

    return funny_nickname
