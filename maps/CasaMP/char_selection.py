"""
Objetivos:


1. Leer datos de personajes desde un archivo
	1.1. Crear monigote del personaje seleccionado
	1.2. Colocar objetos, armas y escudos del personaje seleccionado


Datos de los personajes:
	ID:
		- Nombre
		- Heroe
		- Skin
		- Nivel
		- Nivel Parcial
		- Vida
		- [Armas]
		- [Escudos]
		- [Flechas]
		- [Objetos]
		- [Runas]
		- [Llaves Mágicas]

"""

import GameText
import Raster
import BUIx
import Language

import pickle
import os
import math


FILE_NAME = "chars.p"

font_server_behaviour = BUIx.B_FontServer()
font_behaviour = font_server_behaviour.CreateBFont(Language.MapaDeLetrasHi)


def store_char_data():
	chars_data = {
		"Deus02":{
			"hero":"Knight_N",
			"level":2,
			"life":235
			},
		"UserTest":{
			"hero":"Dwarf_N",
			"level":1,
			"life":34
			},
		"bro_whAtXD":{
			"hero":"Amazon_N",
			"level":10,
			"life":1433
			},
		"Etesech":{
			"hero":"Barbarian_N",
			"level":8,
			"life":809
			}
		}

	print("Trying to store the test data...")

	file = open(FILE_NAME, "wb")
	pickle.dump(chars_data, file, 1)
	file.close()

	print("Data has been dumped! <-----------------")

	GameText.ShowMessage("Personajes guardados!")



class CharManager:
	def __init__(self):
		self.chars_data = None
		self.char_names = None

		self.current_char_index = 0
		self.current_char_entity = None
		self.current_char_data = None

		self.stand_pos = 20674.394289, -2364.734302, -19704.582245
		self.stand_angle = 3.1415926535/2.0
		self.preview_person_name = "CharPreview"

		self.cam_tpos = 20674.394289, -2064.734302, -19704.582245
		self.cam = Bladex.GetEntity("Camera")

		self.heroes = self.create_heroes()


	def draw_char_info(self, time):
		if not self.char_names:
			return

		Raster.SetFont(font_behaviour.GetPointer())
		Raster.SetTextScale(0.25, 0.25)
		Raster.SetTextMode(6)

		# Write nickname above the current selected char
		char_name = self.char_names[self.current_char_index]
		char_data = self.current_char_data

		# If char_data is None, means that the player is focusing the empty space betwen chars
		# that is used to create a new character.
		if char_data and self.current_char_entity:
			px, py, pz = self.current_char_entity.Position

			tw, th = Bladex.GetTextWH(char_name)
			tx, ty = Bladex.GetScreenXY((px, py-1000, pz))
			tx, ty = tx - (tw*512)/2.0, ty - (th*512)/2.0

			Bladex.WriteText(tx, ty, char_name)



		# Draw a black background rectangle
		w, h = Raster.GetSize()
		w_factor = 0.35

		Raster.SetFillColor(0, 0, 0)
		Raster.SetAlpha(0.5)
		Raster.SolidRectangle(0, 0, w*w_factor, 150)
		Raster.SolidRectangle(0, h-40, w, h)
		Raster.SetFillColor(220, 140, 0)
		Raster.SolidRectangle(w*w_factor, 0, w*w_factor + 2, 150)
		Raster.SolidRectangle(0, 150, w*w_factor + 2, 152)



		# Draw text with char info.
		Raster.SetTextScale(0.4, 0.4)

		Raster.SetPosition(w*w_factor*0.5 - 50, 10)
		Raster.WriteText("CHAR INFO")

		if char_data:
			Raster.SetPosition(12, 40)
			Raster.WriteText("Nick: %s"%(char_name))

			Raster.SetPosition(12, 60)
			Raster.WriteText("Level: %i"%(char_data["level"]))

			Raster.SetPosition(12, 80)
			Raster.WriteText("Life: %i"%(char_data["life"]))

		else:
			Raster.SetPosition(12, 40)
			Raster.WriteText("Create a new character.")



		# Fading text at the bottom of the screen saying "PRESS ENTER TO SELECT THIS CHARACTER"
		freq = 1
		a = (math.cos(time*freq*3.1415926535) + 1)/2.0
		Raster.SetTextAlpha(0.3 + a*0.7)

		if char_data:
			Raster.SetTextColor(78, 184, 231)
			Raster.SetPosition(w*0.5 - 150, h-35)
			Raster.WriteText("PRESS ENTER TO SELECT THIS CHARACTER")
		else:
			Raster.SetTextColor(100, 255, 100)
			Raster.SetPosition(w*0.5 - 157, h-35)
			Raster.WriteText("PRESS ENTER TO CREATE A NEW CHARACTER")


		# Static text, below the fading text, saying "< PRESS ARROWS TO CHOOSE A CHARACTER >"
		Raster.SetTextAlpha(1.0)
		Raster.SetTextScale(0.25, 0.25)
		Raster.SetTextColor(215, 215, 215)
		Raster.SetPosition(w*0.5 - 105, h-15)

		if len(self.char_names) > 1:
			Raster.WriteText("<   PRESS ARROWS TO CHOOSE A CHARACTER   >")


	def create_heroes(self):
		chars = {}

		for kind in ["Knight_N", "Amazon_N", "Dwarf_N", "Barbarian_N"]:
			char = Bladex.CreateEntity(kind+"_char", kind, 0, -2000, 0, "Person")
			char.Angle = self.stand_angle
			char.SelfIlum = 1.0
			char.SetOnFloor()

			chars[kind] = char

		chars["[NONE]"] = None

		return chars


	def next_char(self):
		self.place_char(self.current_char_index+1)

	def prev_char(self):
		self.place_char(self.current_char_index-1)

	def place_char(self, index=0):
		if not self.chars_data:
			return

		data_keys = self.chars_data.keys()

		if not self.char_names:
			self.char_names = data_keys

		elif len(self.char_names) != len(data_keys):
			self.char_names = data_keys

		self.current_char_index = index % len(self.char_names)

		char_name = self.char_names[self.current_char_index]

		# Hide the current char
		if self.current_char_entity:
			self.current_char_entity.Position = 0, -2000, 0
			self.current_char_entity.SetOnFloor()

		if char_name == "[NONE]":
			self.current_char_data = None
			self.current_char_entity = None
			return

		char_data = self.chars_data[char_name]
		char_kind = char_data["hero"]
		self.current_char_data = char_data

		hero = self.heroes[char_kind]

		hero.SetTmpAnmFlags(1, 1, 1, 0, 5, 1, 0)
		hero.Wuea = 2
		hero.LaunchAnmType("Rlx")
		hero.Position = self.stand_pos
		hero.SetOnFloor()

		self.current_char_entity = hero


	def select_this_char(self):
		if not self.current_char_data:
			print("ok, bueno....")
		else:
			print("k t importa?")



	def load_char_data(self):
		print("Trying to read the player data...")

		if not os.path.exists(FILE_NAME):
			print("No %s file was found."%(FILE_NAME))
			return

		file = open(FILE_NAME, "rb")
		self.chars_data = pickle.load(file)
		file.close()

		self.chars_data["[NONE]"] = {}

		print("%d chars loaded!"%(len(self.chars_data)))

	def adjust_camera(self):
		tx, ty, tz = self.cam.TPos

		dx, dy, dz = self.cam_tpos




	def mainloop(self, time):
		self.draw_char_info(time)

		self.adjust_camera()


# Create the person manager class
char_manager = CharManager()

# Unpickle the stored chars
char_manager.load_char_data()

# Place an entity person to preview a character
char_manager.place_char()

Bladex.SetAfterFrameFunc("UpdateCharManager", char_manager.mainloop)


def step(a, b, smoothness=1.5, dt=1/60.0):
	return a + (b-a)*(10.0/smoothness)*dt


def set_camera_pos():
	#Disable the camera
	cam = Bladex.GetEntity("Camera")
	cam.ETarget = ""
	cam.TType = 0
	cam.SType = 0

	cam.Position = 16936, -2001, -20077
	cam.TPos = 20674.394289, -2064.734302, -19704.582245


Bladex.AddScheduledFunc(Bladex.GetTime(),set_camera_pos,())




# Selection Music
MUSIC_VOL = 1

Bladex.AddMusicEventMP3("music_char_selection", "../../Sounds/seleccion-personaje.MP3", 2.0, 1.0, MUSIC_VOL, 10000, 1, -1)
Bladex.AddScheduledFunc(Bladex.GetTime(), Bladex.ExeMusicEvent, (Bladex.GetMusicEvent("music_char_selection"),))




# Controls
Bladex.AddInputAction("store_char_data", 0)
Bladex.AssocKey("store_char_data", "Keyboard", "K", 0)
Bladex.AddBoundFunc("store_char_data", store_char_data)

Bladex.AddInputAction("next_char", 0)
Bladex.AssocKey("next_char", "Keyboard", "Right", 0)
Bladex.AddBoundFunc("next_char", char_manager.next_char)

Bladex.AddInputAction("prev_char", 0)
Bladex.AssocKey("prev_char", "Keyboard", "Left", 0)
Bladex.AddBoundFunc("prev_char", char_manager.prev_char)

Bladex.AddInputAction("select_this_char", 0)
Bladex.AssocKey("select_this_char", "Keyboard", "Enter", 0)
Bladex.AddBoundFunc("select_this_char", char_manager.select_this_char)