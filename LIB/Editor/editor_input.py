import Bladex
import BInput

def add_keybind(key, keybind_name, func, press_type = 0, device="Keyboard", when=1):
	Bladex.AddInputAction(keybind_name, press_type)
	Bladex.AssocKey(keybind_name, device, key, when)
	Bladex.AddBoundFunc(keybind_name, func)

class InputMode:
	def __init__(self):
		self.input_manager = BInput.GetInputManager()
		self.input_string = ""

		self.enter_func = None
		self.typein_func = None
		self.on_exit_func = None

		self.load_keybinds()

	def append_char(self, char):
		self.input_string = self.input_string + str(char)

		if self.typein_func:
			try:
				self.typein_func(self.input_string)
			except:
				print "editor.py, InputMode: Warning. TypeIn function not working."

	def input_1(self):
		self.append_char("1")

	def input_2(self):
		self.append_char("2")

	def input_3(self):
		self.append_char("3")

	def input_4(self):
		self.append_char("4")

	def input_5(self):
		self.append_char("5")

	def input_6(self):
		self.append_char("6")

	def input_7(self):
		self.append_char("7")

	def input_8(self):
		self.append_char("8")

	def input_9(self):
		self.append_char("9")

	def input_0(self):
		self.append_char("0")

	def input_enter(self):
		if not self.enter_func:
			print "editor.py, InputMode: Warning. Input enter function is None."
			return

		try:
			self.enter_func(self.input_string)
		except:
			print "editor.py, InputMode: Error calling the input enter function."

		self.stop_input_mode(0)

	def input_delete(self):
		if self.input_string == "":
			return

		self.input_string = self.input_string[:len(self.input_string)-1]
		self.append_char("")


	def start_input_mode(self, enter_func=None, typein_func=None, on_exit_func=None):
		self.enter_func = enter_func
		self.typein_func = typein_func
		self.on_exit_func = on_exit_func

		self.input_manager.SetInputActionsSet("InputMode")

	def stop_input_mode(self, canceled=1):
		self.clear()
		if self.on_exit_func:
			try:
				self.on_exit_func(canceled)
			except:
				print "editor.py, InputMode: Error calling the on exit function."

	def clear(self):
		self.input_string = ""

	def load_keybinds(self):
		self.input_manager.AddInputActionsSet("InputMode")
		self.input_manager.SetInputActionsSet("InputMode")

		add_keybind("1", "input_1", self.input_1, 0)
		add_keybind("2", "input_2", self.input_2, 0)
		add_keybind("3", "input_3", self.input_3, 0)
		add_keybind("4", "input_4", self.input_4, 0)
		add_keybind("5", "input_5", self.input_5, 0)
		add_keybind("6", "input_6", self.input_6, 0)
		add_keybind("7", "input_7", self.input_7, 0)
		add_keybind("8", "input_8", self.input_8, 0)
		add_keybind("9", "input_9", self.input_9, 0)
		add_keybind("0", "input_0", self.input_0, 0)

		add_keybind("Enter", "input_enter", self.input_enter, 0)
		add_keybind("Esc", "stop_input_mode", self.stop_input_mode, 0)
		add_keybind("Backspace", "input_delete", self.input_delete, 0)
