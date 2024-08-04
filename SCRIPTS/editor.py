#╔════════════════════════════╗#
#║  ╔═╗┌┬┐┬┌┬┐┌─┐┬─┐ ┌─┐┬ ┬   ║#
#║  ║╣  │││ │ │ │├┬┘ ├─┘└┬┘   ║#
#║  ╚═╝─┴┘┴ ┴ └─┘┴└─o┴   ┴    ║#
#╚════════════════════════════╝#

""" DELETE THISSSS
Music: bensound.com
License code: DFQMQVQNMQEJHEV5
"""

import Bladex
import BInput
import darfuncs
import Raster
import Scorer
import BUIx
import Language

from GameText import ShowMessage

import math
import string
import os
import sys

sys.path.append("..\\..\\Lib\\Editor")

from editor_aura import Aura
from editor_camera import Camera

from editor_input import InputMode
from editor_input import add_keybind


font_server_behaviour = BUIx.B_FontServer()
font_behaviour = font_server_behaviour.CreateBFont(Language.MapaDeLetras)


STR_COLOR = (255, 230, 120)
INT_COLOR = (255, 255, 255)
FLT_COLOR = (230, 150, 210)
WHITE = (255, 255, 255)
CYAN = (170, 255, 170)
RED = (255, 160, 160)
GREEN = (160, 255, 160)
BLUE = (160, 160, 255)


def euler_from_quaternion(q):
	w, x, y, z = q

	roll = math.atan2(2*(w*x + y*z), 1 - 2*(x**2 + y**2))
	pitch = math.asin(2*(w*y - z*x))
	yaw = math.atan2(2*(w*z + x*y), 1 - 2*(y**2 + z**2))

	return roll, pitch, yaw


def quaternion_rotate(q, angle, axis):
	x, y, z = axis
	norm = math.sqrt(x**2 + y**2 + z**2)
	x, y, z = x/norm, y/norm, z/norm

	sin_half_angle = math.sin(angle / 2)
	cos_half_angle = math.cos(angle / 2)
	rx = x * sin_half_angle
	ry = y * sin_half_angle
	rz = z * sin_half_angle
	rw = cos_half_angle

	qw, qx, qy, qz = q
	new_qw = qw * rw - qx * rx - qy * ry - qz * rz
	new_qx = qw * rx + qx * rw + qy * rz - qz * ry
	new_qy = qw * ry - qx * rz + qy * rw + qz * rx
	new_qz = qw * rz + qx * ry - qy * rx + qz * rw

	return (new_qw, new_qx, new_qy, new_qz)


def step(a, b, dt=1/60.0, smoothness=1.5):
	return a + (b-a)*(10.0/smoothness)*dt


def to_degree(rads):
	degrees = (rads*180)/math.pi
	if degrees < 0:
		degrees = 360 + degrees
	return int(degrees)


def get_bods():
	bodlink = open("../../Lib/Editor/BodList.list", "r")
	lines = bodlink.readlines()
	bodlink.close()

	bod_list = []

	for i in range(len(lines)):
		kind = string.strip(lines[i])
		bod_list.append(kind)

	return bod_list


class RotatoryRings:
	""" Rings that represents the rotation of an object """

	def __init__(self, app):
		self.app = app

		# Ring for Y axis rotation
		self.y_axis_ring = Bladex.CreateEntity("YAxisRing", "AnilloFoso", 0, 0, 0)
		self.y_axis_ring.Scale = 0.75
		self.y_axis_ring.Alpha = 0.0
		self.y_axis_ring.ExclusionGroup = 1
		self.y_axis_ring.CastShadows = 0

		# Ring for X axis rotation
		self.x_axis_ring = Bladex.CreateEntity("XAxisRing", "AnilloFoso", 0, 0, 0)
		self.x_axis_ring.Scale = 0.75
		self.x_axis_ring.Alpha = 0.0
		self.x_axis_ring.ExclusionGroup = 1
		self.x_axis_ring.CastShadows = 0

		# Ring for Z axis rotation
		self.z_axis_ring = Bladex.CreateEntity("ZAxisRing", "AnilloFoso", 0, 0, 0)
		self.z_axis_ring.Scale = 0.75
		self.z_axis_ring.Alpha = 0.0
		self.z_axis_ring.ExclusionGroup = 1
		self.z_axis_ring.CastShadows = 0

		# Set aura on the rings
		self.y_aura = self.set_aura(self.y_axis_ring)
		self.x_aura = self.set_aura(self.x_axis_ring)
		self.z_aura = self.set_aura(self.z_axis_ring)

		# Vars for the aura alpha control
		self.max_aura_alpha = 0.3
		self.target_aura_alpha = 0.3
		self.aura_alpha = 0


	def set_aura(self, entity):
		aura = Bladex.CreateEntity(Bladex.GenerateEntityName(), "Entity Aura", 0, 0, 0)
		aura.SetAuraParams(1, 1, 1, 0, 0, 1)
		entity.Link(aura)
		aura.SetAuraActive(1)
		return aura


	def update_auras(self):
		self.aura_alpha = step(self.aura_alpha, self.target_aura_alpha, self.app.dt)
		self.y_aura.SetAuraGradient(1.0, 0, 0, 1, self.aura_alpha, 0.0, 0, 0, 1, self.aura_alpha, 1.0)
		self.x_aura.SetAuraGradient(1.0, 0, 1, 0, self.aura_alpha, 0.0, 0, 1, 0, self.aura_alpha, 1.0)
		self.z_aura.SetAuraGradient(1.0, 1, 0, 0, self.aura_alpha, 0.0, 1, 0, 0, self.aura_alpha, 1.0)


	def update_rings(self):
		# Update alpha value of ring auras
		self.update_auras()

		if self.app.mode == 0:
			self.target_aura_alpha = 0.0
			self.aura_alpha = 0.0
			return

		c_entity = self.app.current_entity

		if not c_entity:
			return

		# Shorten rotatory ring vars
		y_ring = self.y_axis_ring
		x_ring = self.x_axis_ring
		z_ring = self.z_axis_ring

		# Set alpha to 0.2 when alt is pressed and sets alpha to 0.0 when alt is released
		self.target_aura_alpha = self.max_aura_alpha * self.app.alt

		# Update rings position, orientation and scale
		y_ring.Position = c_entity.Position
		x_ring.Position = c_entity.Position
		z_ring.Position = c_entity.Position

		y_ring.Orientation = c_entity.Orientation
		x_ring.Orientation = quaternion_rotate(c_entity.Orientation, math.pi/2.0, (1, 0, 0))
		z_ring.Orientation = quaternion_rotate(c_entity.Orientation, math.pi/2.0, (0, 1, 0))

		y_ring.Scale = c_entity.Scale * 0.75
		x_ring.Scale = c_entity.Scale * 0.75
		z_ring.Scale = c_entity.Scale * 0.75


class MapEditor:
	def __init__(self):
		self.input_manager = BInput.GetInputManager()

		self.DEBUG_INFO = 0

		self.current_entity = None
		self.current_bod_id = None

		self.entity_mov_speed = 3000
		self.general_speed = 1
		self.clipboard = None

		self.entity_list = []
		self.this_session = -1
		self.saving = 0

		self.time = 0
		self.fps = 60.0
		self.dt = 1/60.0

		self.mode = 0

		self.alt = 0
		self.shift = 0
		self.ctrl = 0

		self.aura = Aura(self, "EditorAuraSelection")
		self.camera = Camera(self)
		self.input = InputMode()
		self.rings = RotatoryRings(self)

		self.BOD_list = get_bods()



	def draw_text(self, x, y, text, color, inter_line=10):
		lines = string.split(str(text), '\n')
		r, g, b = color
		Raster.SetTextColor(r, g, b)

		for i in range(len(lines)):
			line = lines[i]

			Raster.SetPosition(x, y + i*inter_line)
			Raster.WriteText(line)


	def display_information(self):
		""" displays editing information in text format on the game screen """
		if not self.current_entity or not self.mode == 1:
			return

		entity = self.current_entity
		text = "K pasa realmente"

		roll, pitch, yaw = euler_from_quaternion(entity.Orientation)

		#'SetTextBlur', 'SetTextBlurAlpha', 'SetTextBlurColor'

		# Raster.SetTextMode(0..7)
		# Tamaño real:
		# 0 -> Nada
		# 1 -> Sombra del texto
		# 2 -> Texto sin sombra
		# 3 -> Texto con sombra
		# Tamaño escalable:
		# 4 -> Nada
		# 5 -> Sombra del texto
		# 6 -> Texto sin sombra
		# 7 -> Texto con sombra

		e = self.current_entity
		_type = "Static"*e.Static + "Physic"*e.Physic + "Weapon"*e.Weapon + "Arrow"*e.Arrow + "Person"*e.Person

		Raster.SetTextMode(6)
		Raster.SetTextScale(0.5, 0.5)

		Raster.SetFont(font_behaviour.GetPointer())
		Raster.SetTextAlpha(1.0)

		x, y = 10, 10

		self.draw_text(x, y   , "Objeto: %s"%(e.Name), CYAN)

		# Basic info
		self.draw_text(x   , y+10, " - Type\n - Kind\n - Scale\n - Mass\n - Alpha\n - SelfIlum", WHITE)
		self.draw_text(x+35, y+10, ":\n"*6, WHITE)
		self.draw_text(x+40, y+10, str(_type)     , STR_COLOR)
		self.draw_text(x+40, y+20, str(e.Kind)    , STR_COLOR)
		self.draw_text(x+40, y+30, str(e.Scale)   , FLT_COLOR)
		self.draw_text(x+40, y+40, str(e.Mass)    , FLT_COLOR)
		self.draw_text(x+40, y+50, str(e.Alpha)   , FLT_COLOR)
		self.draw_text(x+40, y+60, str(e.SelfIlum), FLT_COLOR)

		# Position info
		self.draw_text(x   , y+80 , " - Position :", WHITE)
		self.draw_text(x+10, y+90 , "- x\n- y\n- z", WHITE)
		self.draw_text(x+20, y+90 , ":\n"*3, WHITE)
		self.draw_text(x+25, y+90 , str(e.Position[0]), RED)
		self.draw_text(x+25, y+100, str(e.Position[1]), GREEN)
		self.draw_text(x+25, y+110, str(e.Position[2]), BLUE)

		# Orientation Info
		self.draw_text(x   , y+130, " - Orientation :", WHITE)
		self.draw_text(x+10, y+140, "- qw\n- qx\n- qy\n- qz", WHITE)
		self.draw_text(x+25, y+140, ":\n"*4, WHITE)
		self.draw_text(x+30, y+140, str(e.Orientation[0]), FLT_COLOR)
		self.draw_text(x+30, y+150, str(e.Orientation[1]), RED)
		self.draw_text(x+30, y+160, str(e.Orientation[2]), GREEN)
		self.draw_text(x+30, y+170, str(e.Orientation[3]), BLUE)

	def typein_func(self, text_id):
		kind = self.kind_from_bod_id(text_id)
		ShowMessage("BOD ID: %s\nKind: %s"%(text_id, kind))

	def on_exit_func(self, canceled):
		if self.mode == 0:
			self.input_manager.SetInputActionsSet("Default")

		if self.mode == 1:
			self.input_manager.SetInputActionsSet("CreativeMode")

		if canceled:
			ShowMessage("Operacion cancelada.")


	def particle_fx(self, obj_name):
		""" Particles for when an entity was copied or created """
		prtl = Bladex.CreateEntity(Bladex.GenerateEntityName(), "Entity Particle System Dobj", 0, 0, 0)
		prtl.ObjectName = obj_name
		prtl.ParticleType = "LargeDust"
		prtl.PPS = 1024
		prtl.YGravity = 200.0
		prtl.Friction = 0.2
		prtl.Velocity = 0, 0, 0
		prtl.RandomVelocity = 80.0
		prtl.RandomVelocity_V=1.0
		prtl.DeathTime = Bladex.GetTime()+2.0/60.0


	def kind_from_bod_id(self, str_bod_id):
		try:
			kind = self.BOD_list[int(str_bod_id)]
		except:
			kind = None

		return kind


	def create_entity2(self, str_bod_id):
		kind = self.kind_from_bod_id(str_bod_id)

		if not kind: return

		if self.current_entity:
			x, y, z = self.current_entity.Position
		else:
			char = Bladex.GetEntity("Player1")
			x, y, z = char.Position

		obj = Bladex.CreateEntity(Bladex.GenerateEntityName(), kind, x, y, z)

		self.current_entity = obj
		self.entity_list.append(obj.Name)
		self.aura.set_on(obj.Name)

		self.camera.focus_on_entity(obj.Name)

		self.particle_fx(obj.Name)

		ShowMessage("Objeto creado: %s\nUsa WASD para mover el objeto."%(kind))


	def create_entity(self):
		self.input.start_input_mode(self.create_entity2, self.typein_func, self.on_exit_func)
		ShowMessage("Type in the BOD ID")


	def move_entity(self, vx, vy, vz):
		if not self.current_entity: return

		speed = (0.1*self.shift + (not self.shift))*self.entity_mov_speed*self.dt*self.general_speed

		x, y, z = self.current_entity.Position
		self.current_entity.Position = x + speed*vx, y + speed*vy, z + speed*vz

	def rotate_entity(self, rx, ry, rz):
		if not self.current_entity:
			return

		speed = (0.1*self.shift + (not self.shift))*math.pi*self.dt*self.general_speed*0.5
		self.current_entity.Rotate(rx, ry, rz, speed)


	def entity_move_up(self):
		if self.alt:
			self.rotate_entity(0, -1, 0)
		else:
			self.move_entity(0, -1, 0)

	def entity_move_down(self):
		if self.alt:
			self.rotate_entity(0, 1, 0)
		else:
			self.move_entity(0, 1, 0)

	def entity_move_north(self):
		if self.alt:
			self.rotate_entity(1, 0, 0)
		else:
			ang = self.camera.h_angle
			dx, dz = -math.cos(ang), -math.sin(ang)
			self.move_entity(dx,  0,  dz)

	def entity_move_south(self):
		if self.ctrl or self.saving:
			if not self.saving:
				self.saving = 1
				self.save_entities()
			return

		if self.alt:
			self.rotate_entity(-1, 0, 0)
		else:
			ang = self.camera.h_angle
			dx, dz = math.cos(ang), math.sin(ang)
			self.move_entity(dx,  0,  dz)

	def entity_move_east(self):
		if self.alt:
			self.rotate_entity(0, 0, 1)
		else:
			ang = self.camera.h_angle
			dx, dz = math.cos(ang + math.pi*0.5), math.sin(ang + math.pi*0.5)
			self.move_entity(dx,  0,  dz)

	def entity_move_west(self):
		if self.alt:
			self.rotate_entity(0, 0, -1)
		else:
			ang = self.camera.h_angle
			dx, dz = math.cos(ang - math.pi*0.5), math.sin(ang - math.pi*0.5)
			self.move_entity(dx,  0,  dz)


	def enter_creative(self):
		self.input_manager.SetInputActionsSet("CreativeMode")
		if self.current_entity:
			self.aura.set_on(self.current_entity.Name)
			self.camera.focus_on_entity(self.current_entity.Name)
		self.mode = 1
		Scorer.SetVisible(0)
		ShowMessage("Modo creativo activado.")

	def exit_creative(self):
		self.input_manager.SetInputActionsSet("Default")
		self.camera.focus_on_player()
		self.aura.take_off()
		self.mode = 0
		Scorer.SetVisible(1)
		ShowMessage("Saliste del modo creativo.")


	def alt_pressed(self):
		self.alt = 1

	def alt_released(self):
		self.alt = 0

	def shift_pressed(self):
		self.shift = 1

	def shift_released(self):
		self.shift = 0

	def ctrl_pressed(self):
		self.ctrl = 1

	def ctrl_released(self):
		self.ctrl = 0


	def paste(self):
		# Crea un objeto idéntico al objeto copiado con la función self.copy
		if not self.clipboard:
			return

		name = Bladex.GenerateEntityName()
		kind = self.clipboard["Kind"]

		if self.current_entity:
			x, y, z = self.current_entity.Position
		else:
			char = Bladex.GetEntity("Player1")
			x, y, z = char.Position

		obj = Bladex.CreateEntity(name, kind, x, y, z)
		obj.Orientation = self.clipboard["Orientation"]
		obj.Scale = self.clipboard["Scale"]

		self.particle_fx(obj.Name)

		self.current_entity = obj
		self.camera.focus_on_entity(obj.Name)
		self.aura.set_on(obj.Name)

		self.entity_list.append(obj.Name)


	def copy(self):
		# Copia los datos del objeto actual
		if not self.current_entity or not self.ctrl:
			ShowMessage("No object to copy.")
			return

		self.clipboard = {
			"Kind"        : self.current_entity.Kind,
			"Orientation" : self.current_entity.Orientation,
			"Scale"       : self.current_entity.Scale
		}

		ShowMessage("Object copied to clipboard!")


	def set_bod_id(self, bod_id):
		if not self.current_entity:
			return

		kind = self.kind_from_bod_id(bod_id)

		if not kind or kind == self.current_entity.Kind: return

		self.aura.take_off()

		# Collect current entity data before it is deleted
		name = self.current_entity.Name
		x, y, z = self.current_entity.Position
		orientation = self.current_entity.Orientation
		scale = self.current_entity.Scale
		alpha = self.current_entity.Alpha

		# Delete the current entity
		Bladex.DeleteEntity(self.current_entity)

		# Create new entity with the old entity data but with a new BOD Kind
		obj = Bladex.CreateEntity(name, kind, x, y, z)
		obj.Orientation = orientation
		obj.Scale = scale
		obj.Alpha = alpha

		# Set the new entity as the current entity
		self.current_entity = obj
		self.aura.set_on(obj.Name)

		ShowMessage("Current BOD: %s\nID: %i"%(kind, bod_id))


	def increment_bod_id(self, increment=1):
		if not self.current_entity:
			return

		current_kind = self.current_entity.Kind
		current_bod_id = self.BOD_list.index(current_kind)

		next_bod_id = (current_bod_id + increment) % len(self.BOD_list)

		self.set_bod_id(next_bod_id)


	def next_bod_id(self):
		self.increment_bod_id(1)

	def previous_bod_id(self):
		self.increment_bod_id(-1)



	def next_entity(self):
		if len(self.entity_list) == 0:
			return

		if self.current_entity:
			name = self.current_entity.Name
			index = self.entity_list.index(name)
		else:
			index = 0

		next_index = (index + 1) % len(self.entity_list)

		next_entity_name = self.entity_list[next_index]

		self.current_entity = Bladex.GetEntity(next_entity_name)
		self.camera.focus_on_entity(next_entity_name)
		self.camera.cut()
		self.aura.set_on(next_entity_name)

		ShowMessage("Enfocando a %s"%(next_entity_name))


	def entity_scale_up(self):
		if not self.current_entity:
			return

		speed = (0.1*self.shift + (not self.shift))*self.general_speed*self.dt*0.5

		self.current_entity.Scale = min(5.0, self.current_entity.Scale + speed)

	def reset_orientation(self):
		if not self.current_entity:
			return

		self.current_entity.Orientation = 1.0, 0.0, 0.0, 0.0
		ShowMessage("Orientacion reestablecida.")


	def save_entities(self):
		""" Generates a objs.py file that contains all the objects
		created with this mod. """

		if len(self.entity_list) == 0:
			ShowMessage("No objects to save.")
			return

		# Generate an empty file to write all code
		file_name = "objs"
		file_count = 0
		file_extension = ".py"
		file_name_format = "%s_%i%s"

		if self.this_session == -1:
			# Find an available file name
			while os.path.exists(file_name_format%(file_name, file_count, file_extension)):
				file_count = file_count+1

			self.this_session = file_count

		file_name = file_name_format%(file_name, self.this_session, file_extension)
		file = open(file_name, "w")
		file.write("import Bladex\n")

		errors = 0

		# Write the code of every object created
		for entity_name in self.entity_list:
			entity = Bladex.GetEntity(entity_name)

			if not entity:
				print "Error: the entity \"%s\" doesn't exists. Couldn't save entity."
				errors = errors+1
				continue

			# Object data
			name = entity.Name
			kind = entity.Kind
			x, y, z = entity.Position
			qw, qx, qy, qz = entity.Orientation
			scale = entity.Scale
			alpha = entity.Alpha
			static = entity.Static

			objtype = "Static"
			if entity.Physic: objtype = "Physic"
			if entity.Weapon: objtype = "Weapon"

			# Object creation code
			line_1 = "\n\n# Entity: %s\n"%(name)
			line_2 = "o = Bladex.CreateEntity(\"%s\", \"%s\", %f, %f, %f)\n"%(name, kind, x, y, z)
			line_3 = "o.Scale = %f\n"%(scale)
			line_4 = "o.Static = %i\n"%(static)
			line_5 = "o.Orientation = %f, %f, %f, %f\n"%(qw, qx, qy, qz)
			line_6 = "o.Alpha = %f\n"%(alpha)

			file.write(line_1)
			file.write(line_2)
			file.write(line_3)
			if static: file.write(line_4)
			file.write(line_5)
			if alpha < 1.0: file.write(line_6)

		file.close()

		if errors == 0:
			ShowMessage("All objects saved successfully!\nOutput file -> %s/%s"%(Bladex.GetCurrentMap(), file_name))
		else:
			ShowMessage("%i objects couldn't be saved, check console for more info.\nOutput file -> %s/%s"%(errors, Bladex.GetCurrentMap(), file_name))


	def delete_entity(self):
		if not self.current_entity:
			return

		name = self.current_entity.Name

		if len(self.entity_list) > 1:
			self.next_entity()
		else:
			self.camera.focus_on_player()
			self.aura.take_off()
			self.current_entity = None

		self.entity_list.remove(name)
		Bladex.DeleteEntity(Bladex.GetEntity(name))

		Bladex.ShowMessage("Entity \"%s\" was deleted"%(name))


	def stop_saving(self):
		self.saving = 0


	def entity_scale_down(self):
		if not self.current_entity:
			return

		speed = (0.1*self.shift + (not self.shift))*self.general_speed*self.dt*0.5

		self.current_entity.Scale = max(0.01, self.current_entity.Scale - speed)


	def load_keybinds(self):
		self.input_manager.SetInputActionsSet("Default")

		# Free cam
		Bladex.AssocKey("Change Mov", "Keyboard", "P")

		# Keybind to enter creative mode
		add_keybind("K", "CreativeModeOn", self.enter_creative, 0)


		#***************** CREATIVE MODE KEYBINDS *******************#
		# Create new input action set for creative mode keybinds
		self.input_manager.AddInputActionsSet("CreativeMode")
		self.input_manager.SetInputActionsSet("CreativeMode")


		# Keybind to exit creative mode
		add_keybind("K", "CreativeModeOff", self.exit_creative, 0)
		add_keybind("Esc", "CreativeModeOff", self.exit_creative, 0)


		# Create Entity keybind
		add_keybind("N", "create_entity", self.create_entity, 0)

		# Delete Entity
		add_keybind("Delete", "delete_entity", self.delete_entity, 0)


		# Entity Movement
		add_keybind("E", "entity_move_up", self.entity_move_up, 1)
		add_keybind("Q", "entity_move_down", self.entity_move_down, 1)
		add_keybind("W", "entity_move_north", self.entity_move_north, 1)

		# this keybind also saves entities when ctrl is pressed
		add_keybind("S", "entity_move_south", self.entity_move_south, 1)
		add_keybind("S", "stop_saving", self.stop_saving, 0, when=0)

		add_keybind("D", "entity_move_east", self.entity_move_east, 1)
		add_keybind("A", "entity_move_west", self.entity_move_west, 1)

		add_keybind("0", "reset_orientation", self.reset_orientation, 0)

		add_keybind("X", "entity_scale_up", self.entity_scale_up, 1)
		add_keybind("Z", "entity_scale_down", self.entity_scale_down, 1)

		add_keybind("Shift", "shift_pressed", self.shift_pressed, 0, when=1)
		add_keybind("Shift", "shift_released", self.shift_released, 0, when=0)

		add_keybind("LAlt", "alt_pressed", self.alt_pressed, 0, when=1)
		add_keybind("LAlt", "alt_released", self.alt_released, 0, when=0)

		add_keybind("LCtrl", "ctrl_pressed", self.ctrl_pressed, 0, when=1)
		add_keybind("LCtrl", "ctrl_released", self.ctrl_released, 0, when=0)

		add_keybind("C", "copy_entity", self.copy, 0)
		add_keybind("V", "paste_entity", self.paste, 0)

		add_keybind("WheelUp", "next_bod_id", self.next_bod_id, 0, device="Mouse")
		add_keybind("WheelDown", "previous_bod_id", self.previous_bod_id, 0, device="Mouse")

		# Camera movement
		add_keybind("B", "toggle_view", self.camera.toggle_view, 0)

		add_keybind("Add", "cam_zoom_in", self.camera.zoom_in, 1)
		add_keybind("Subtract", "cam_zoom_out", self.camera.zoom_out, 1)

		add_keybind("Left", "cam_rotate_left", self.camera.rotate_left, 1)
		add_keybind("Right", "cam_rotate_right", self.camera.rotate_right, 1)
		add_keybind("Up", "cam_rotate_up", self.camera.rotate_up, 1)
		add_keybind("Down", "cam_rotate_down", self.camera.rotate_down, 1)

		add_keybind("Tab", "next_entity", self.next_entity, 0)


	def debug_print(self, msg):
		if self.DEBUG_INFO:
			prefix = "editor.py -> %s"
			print prefix%(str(msg))

	def start(self):
		self.load_keybinds()

		Bladex.SetAfterFrameFunc("EditorMainLoop", self.main_loop)

		# Return to the default input action set
		self.input_manager.SetInputActionsSet("Default")

	def get_time(self, time):
		self.dt = time - self.time
		self.time = time

	def main_loop(self, time):
		self.get_time(time)

		self.display_information()
		self.aura.update()
		self.camera.update()
		self.rings.update_rings()


# Initialize the map editor
map_editor = MapEditor()
map_editor.start()
