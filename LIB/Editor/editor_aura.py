import Bladex
import math

class Aura:
	""" Clase Aura para un aura parpadeante que se aplica a un objeto con el fin de poder
	identificar dicho objeto con mayor facilidad. """

	def __init__(self, app, name):
		self.app = app

		self.name = name
		self.size = 10
		self.alpha = 0.3

		aura = Bladex.CreateEntity("SelectedItemAura", "Entity Aura", 0, 0, 0)
		aura.SetAuraParams(self.size, 1, 1, 0, 0, 1)
		aura.SetAuraGradient(2, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 2.0)

		self.aura = aura


	def take_off(self):
		self.aura.SetAuraActive(0)

		if not self.aura.Parent:
			return

		parent = Bladex.GetEntity(self.aura.Parent)

		try:
			parent.Unlink(self.aura)
		except:
			self.app.debug_print("Error unlinking aura from entity \"%s\""%(parent.Name))
		else:
			self.app.debug_print("Aura unlinked from entity \"%s\" successfully"%(parent.Name))


	def set_on(self, obj_name):
		self.take_off()

		try:
			obj = Bladex.GetEntity(obj_name)
			obj.Link(self.aura)
		except:
			print "editor.py error -> Aura.set_on(self, obj_entity)"
			print "\tNo se pudo aplicar el aura en el objeto \"%s\""%(obj_name)
		else:
			self.aura.SetAuraActive(1)
			self.app.debug_print("Aura linked to %s successfully."%(obj_name))


	def update(self):
		if self.aura.Parent:
			time = self.app.time
			alpha = (math.sin(time*8)+1)/2
			self.aura.SetAuraParams(self.size, alpha*self.alpha, 1, 0, 0, 1)

			if self.app.alt:
				# Yellow aura
				self.aura.SetAuraGradient(2, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 2.0)
			else:
				# Green aura
				self.aura.SetAuraGradient(2, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 2.0)


