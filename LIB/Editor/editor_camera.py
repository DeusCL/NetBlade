import Bladex

from math import sin
from math import cos
from math import pi

class Camera:
	def __init__(self, app):
		self.app = app

		self.smoothness = 1.5
		self.pos = 0, 0, 0
		self.tpos = 0, 0, 0

		self.invert_x = 0
		self.invert_y = 0

		# Config of every entity visited
		self.entities_conf = {}

		# Camera angle to the target position in radians
		self.h_angle = 0
		self.target_h_angle = 0
		self.v_angle = pi*0.5
		self.target_v_angle = pi*0.5

		# Distance of the camera to the target
		self.dist = 5000

		self.target_tpos = (0, 0, 0)
		self.target_entity = None

		self.camera = Bladex.GetEntity("Camera")

		self.active = 0


	def rotate_left(self):
		if not self.active: return
		invert = -1*self.invert_x + 1*(not self.invert_x)
		self.target_h_angle = self.target_h_angle - 3.141592*self.app.dt*2*0.45*invert

	def rotate_right(self):
		if not self.active: return
		invert = -1*self.invert_x + 1*(not self.invert_x)
		self.target_h_angle = self.target_h_angle + 3.141592*self.app.dt*2*0.45*invert

	def rotate_up(self):
		if not self.active: return
		invert = -1*self.invert_y + 1*(not self.invert_y)
		self.target_v_angle = min(3.14, self.target_v_angle + 3.141592*self.app.dt*2*0.45*invert)

	def rotate_down(self):
		if not self.active: return
		invert = -1*self.invert_y + 1*(not self.invert_y)
		self.target_v_angle = max(0.01, self.target_v_angle - 3.141592*self.app.dt*2*0.45*invert)

	def zoom_out(self, dist=4000):
		if not self.active: return
		self.dist = min(10000, self.dist + dist*self.app.dt)

	def zoom_in(self, dist=4000):
		if not self.active: return
		self.dist = max(500, self.dist - dist*self.app.dt)

	def step(self, a, b):
		return a + (b-a)*(10.0/self.smoothness)*self.app.dt


	def focus_on_entity(self, entity_name):
		entity = Bladex.GetEntity(entity_name)
		if not entity:
			self.app.debug_print("Camera(): focus_on_entity(self, entity_name) -> \"%s\" no existe."%(str(entity_name)))
			return

		if not entity_name in self.entities_conf.keys():
			self.entities_conf[entity_name] = {"h_angle":0, "v_angle":0, "dist":5000}
		else:
			self.h_angle = self.entities_conf[entity_name]["h_angle"]
			self.v_angle = self.entities_conf[entity_name]["v_angle"]
			self.dist = self.entities_conf[entity_name]["dist"]

			self.target_h_angle = self.h_angle
			self.target_v_angle = self.v_angle

		char = Bladex.GetEntity("Player1")
		char.Freeze()

		cam = Bladex.GetEntity("Camera")
		cam.ETarget = ""
		cam.TType = 0
		cam.SType = 0

		self.target_entity = entity
		self.tpos = cam.TPos
		self.active = 1

		self.app.debug_print("Camara virtual fijada en el objeto \"%s\""%(str(entity_name)))


	def focus_on_player(self):
		char = Bladex.GetEntity("Player1")
		char.UnFreeze()

		cam = Bladex.GetEntity("Camera")
		cam.ETarget = "Player1"
		cam.SetPersonView("Player1")
		cam.Cut()

		self.active = 0

	def toggle_view(self):
		if self.active:
			self.focus_on_player()

		else:
			self.focus_on_entity(self.app.current_entity.Name)

	def is_free(self, x, y, z):
		if Bladex.GetSector(x, y, z):
			return 1 # Free
		return 0 # Not Free

	def cut(self):
		if self.target_entity:
			tx, ty, tz = self.target_entity.Position
		else:
			tx, ty, tz = self.target_tpos

		x = tx + self.dist*cos(self.h_angle)*sin(self.v_angle)
		z = tz + self.dist*sin(self.h_angle)*sin(self.v_angle)
		y = ty + self.dist*cos(self.v_angle)

		self.tpos = tx, ty, tz
		self.camera.Position = x, y, z

	def update_angle(self):
		# Calculate camera position according to the angle
		cx, cy, cz = self.camera.Position
		h_ang = self.h_angle
		v_ang = self.v_angle
		dist = self.dist

		self.h_angle = self.step(h_ang, self.target_h_angle)
		self.v_angle = self.step(v_ang, self.target_v_angle)

		if self.target_entity:
			tx, ty, tz = self.target_entity.Position
		else:
			tx, ty, tz = self.target_tpos


		tests = 20
		for i in range(tests):
			new_dist = dist * ((i+1)/float(tests))

			ox = tx + new_dist*cos(self.h_angle)*sin(self.v_angle)
			oy = ty + new_dist*cos(self.v_angle)
			oz = tz + new_dist*sin(self.h_angle)*sin(self.v_angle)

			if self.is_free(ox, oy, oz) or i == 0:
				x, y, z = ox, oy, oz
			else:
				break

		cx = self.step(cx, x)
		cy = self.step(cy, y)
		cz = self.step(cz, z)

		self.camera.Position = cx, cy, cz


	def update_target_position(self):
		# Initial camera target position
		ctx, cty, ctz = self.tpos

		if self.target_entity:
			# Entity target position
			ex, ey, ez = self.target_entity.Position
		else:
			# Simple target position
			ex, ey, ez = self.target_tpos

		# Camera tpos movement
		ctx, cty, ctz = self.step(ctx, ex), self.step(cty, ey), self.step(ctz, ez)

		self.tpos = ctx, cty, ctz
		self.camera.TPos = self.tpos


	def update_entity_config(self):
		if not self.target_entity:
			return

		name = self.target_entity.Name

		# Update current entity focus config
		self.entities_conf[self.target_entity.Name] = {
			"h_angle" : self.h_angle, 
			"v_angle" : self.v_angle,
			"dist"    : self.dist
		}


	def update(self):
		if not self.active:
			return

		self.update_angle()
		self.update_target_position()
		self.update_entity_config()
