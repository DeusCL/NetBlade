import math
import string

import Bladex # type: ignore
import CombosFX
import Actions
import AniSound # type: ignore
import ItemTypes # type: ignore
import Raster # type: ignore

import BUIx
import Language # type: ignore

font_server_behaviour = BUIx.B_FontServer()
font_behaviour = font_server_behaviour.CreateBFont(Language.MapaDeLetrasHi)


class NetPlayer:
	def __init__(self, me, nick = "$None"):
		print("netplayer.py -> Creating new NetPlayer: "+str(me.Name))

		me.SendTriggerSectorMsgs = 1

		self.pers = me
		self.name = me.Name

		self.nick = nick

		# Bladex classic B_PyEntity Data attributes:
		self.Poisoned = 0
		self.ThrowForce = 10

		# New attributes:
		self.target_pos = 0, 0, 0
		self.target_ang = 0
		self.target_anm = ""

		self.smoothness = 1
		self.active = 1

		# Start core funcs
		self.start_core_funcs()
		self.reset_sounds()

		Bladex.SetAfterFrameFunc("NickDraw", self.draw_nick)

		Bladex.AddScheduledFunc(Bladex.GetTime(), self.main_loop, ())

		print("netplayer.py -> NetPlayer created successfully!")


	def start_core_funcs(self):
		me = self.pers

		me.AddAnmEventFunc("Start_Weapon", Actions.Start_Weapon)
		me.AddAnmEventFunc("Stop_Weapon", Actions.Stop_Weapon)
		me.AddAnmEventFunc("Start_Trail", Actions.Start_Trail)
		me.AddAnmEventFunc("Stop_Trail", Actions.Stop_Trail)

		if me.CharTypeExt in ("Kgt", "Bar", "Amz", "Dwf"):
			exec_string = "CombosFX."+me.CharTypeExt+"CombosFX(me.Name)"
			exec(exec_string)


	def reset_sounds(self):
		me = self.pers
		kind = me.Kind[:len(me.Kind)-2]

		if kind == "Barbarian":
			AniSound.AsignarSonidosBarbaro(self.name)

		if kind == "Knight":
			AniSound.AsignarSonidosCaballero(self.name)

		if kind == "Dwarf":
			AniSound.AsignarSonidosEnano(self.name)

		if kind == "Amazon":
			AniSound.AsignarSonidosAmazona(self.name)


	def pos_ang_update(self, smoothness=1, dt=1/60.0):
		if not self.pers:
			return

		# Suavizar posición del jugador
		x, y, z = self.pers.Position
		px, py, pz = self.target_pos

		x = smooth_step(x, px, smoothness)
		y = smooth_step(y, py, smoothness)
		z = smooth_step(z, pz, smoothness)

		self.pers.Position = x, y, z

		# Suavizar el ángulo del jugador
		dif = self.target_ang - self.pers.Angle
		if dif > math.pi:
			dif = dif - 2*math.pi
		elif dif < -math.pi:
			dif = dif + 2*math.pi

		self.pers.Angle = self.pers.Angle + dif*(10/smoothness)*dt


	def anm_update(self):
		#lower_anm = string.lower(self.target_anm)
		#lower_pers_anm = string.lower(self.pers.AnimName)

		#if lower_anm[:3] == 'drp' and lower_pers_anm[:3] != 'drp':
			#print("Drop Release Event Handler Performance!!!!!!!!!!!")

			#if lower_anm[-1:] == 'l':
			#	Actions.TryDropLeft(self.pers.Name)
			#	event_name = "DropLeftEvent"

			#elif lower_anm[-1:] == 'r':
			#	Actions.TryDropRight(self.pers.Name)
			#	event_name = "DropRightEvent"

			# Replace the anm event func added by Actions
			#self.pers.DelAnmEventFunc(event_name)
			#self.pers.AddAnmEventFunc(event_name, drop_func)

			#pass


		if self.target_anm != self.pers.AnimName:
			self.pers.Wuea = 2
			self.pers.LaunchAnmType(self.target_anm)


	def draw_nick(self, time):
		# Check if the person and nick are valid and active
		if not self.pers or self.nick == "$None" or not self.active:
			return

		# Get the camera and person positions
		cam = Bladex.GetEntity("Camera")
		cx, cy, cz = cam.Position
		x, y, z = self.pers.Position

		# Check if the tag is behind the camera
		if is_tag_behind_camera(cam.Position, cam.TPos, self.pers.Position):
			return

		# Calculate distance and scaling factor
		dx, dy, dz = cx - x, cy - y, cz - z
		dist = math.sqrt(dx * dx + dy * dy + dz * dz) / 1000.0
		factor_scale = 4.0 / (dist + 1.0)
		scale = 0.25

		# Set text properties
		Raster.SetTextColor(231, 231, 231)
		Raster.SetFont(font_behaviour.GetPointer())
		Raster.SetTextScale(scale * factor_scale, scale * factor_scale)
		Raster.SetTextMode(6)

		# Get screen dimensions and text size
		screen = Bladex.GetScreenRect()
		tw, th = Bladex.GetTextWH(self.nick)
		tx, ty = Bladex.GetScreenXY((x, y - 1000, z))

		# Check if text is within screen bounds
		if tx > 0.5 or ty > 0.5 or tx + tw < -0.5 or ty + th < -0.5:
			return

		# Adjust text position
		tw = tw * factor_scale * 256
		th = th * factor_scale * 256
		tx = tx - tw
		ty = ty - th

		# Draw the text on the screen
		Bladex.WriteText(tx, ty, self.nick)


	def main_loop(self):
		if self.active:
			Bladex.AddScheduledFunc(Bladex.GetTime(), self.main_loop, ())

		self.pos_ang_update()
		self.anm_update()


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


def gen_name():
	return Bladex.GenerateEntityName()


def drop_func(entity_name, event_name, test_hit=1):
	""" The Net-Version of DropReleaseEventHandler """

	me = Bladex.GetEntity(entity_name)

	try:
		obj_to_drop = me.Data.obj_to_drop
	except AttributeError:
		return

	if obj_to_drop == "":
		return

	inv = me.GetInventory()

	obj = Bladex.CreateEntity(gen_name(), obj_to_drop, 0, 0, 0, "Weapon")
	ItemTypes.ItemDefaultFuncs(obj)

	impulse = me.Rel2AbsVector(-1000.0, -1500.0, 0.0)

	if event_name == "DropLeftEvent":
		if me.InvLeft:
			inv.LinkLeftHand('')
			my_obj = Bladex.GetEntity(me.InvLeft)
			my_obj.SubscribeToList('Pin')

		inv.LinkLeftHand(obj.Name)

		me.Unlink(obj)
		inv.LinkLeftHand('')

		impulse = me.Rel2AbsVector(500.0, -750.0, 0.0)

	else:
		if me.InvRight:
			inv.LinkRightHand('')
			my_obj = Bladex.GetEntity(me.InvRight)
			my_obj.SubscribeToList('Pin')

		inv.LinkRightHand(obj.Name)

		me.Unlink(obj)
		inv.LinkRightHand('')

		impulse = me.Rel2AbsVector(-1000.0, -1500.0, 0.0)

	obj.Impulse(impulse[0],impulse[1],impulse[2])
	obj.ExcludeHitFor(me)

	me.DelAnmEventFunc(event_name)




def smooth_step(start_value, target_value, smoothness=10, dt=1/60.0):
	return start_value + (target_value-start_value)*(10/smoothness)*dt





def is_tag_behind_camera(camera_pos, lookat_pos, tag_pos):
	"""
	Determine if a name tag is behind the camera.

	Given the position of the camera, the position the camera is looking at, 
	and the position of a name tag, this function determines whether the name tag 
	is behind the camera.
	"""

	camera_x, camera_y, camera_z = camera_pos
	lookat_x, lookat_y, lookat_z = lookat_pos
	tag_x, tag_y, tag_z = tag_pos

	# Calculate direction vector from camera to look-at position
	D_c_x = lookat_x - camera_x
	D_c_y = lookat_y - camera_y
	D_c_z = lookat_z - camera_z

	# Calculate the magnitude of the direction vector
	D_c_mag = math.sqrt(D_c_x**2 + D_c_y**2 + D_c_z**2)

	# Normalize the direction vector
	D_c_norm_x = D_c_x / D_c_mag
	D_c_norm_y = D_c_y / D_c_mag
	D_c_norm_z = D_c_z / D_c_mag

	# Calculate vector from camera to tag position
	V_ct_x = tag_x - camera_x
	V_ct_y = tag_y - camera_y
	V_ct_z = tag_z - camera_z

	# Calculate dot product
	dot_product = (D_c_norm_x * V_ct_x +
				   D_c_norm_y * V_ct_y +
				   D_c_norm_z * V_ct_z)

	# Check if the tag is behind the camera
	if dot_product < 0:
		return 1
	else:
		return 0

