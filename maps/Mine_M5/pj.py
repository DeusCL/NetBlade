import Actions
import AniSound
import Reference
import Basic_Funcs
import Sparks
import ItemTypes
import CharStats

import random
import netfuncs

net_state = netfuncs.get_net_state()

kind = net_state['KIND']

char = Bladex.CreateEntity("Player1", kind, 0, 0, 0, "Person")
char.Data = Basic_Funcs.PlayerPerson(char)

char.Level = 19
char.Life = CharStats.GetCharMaxLife(char.Kind, char.Level)

armas = 1


if armas:
	if char.Kind == "Knight_N":
		o = Bladex.CreateEntity(netfuncs.gen_rand_name("WeaponInvPrb_"), "BladeSword2", 0, 0, 0, "Weapon")
		ItemTypes.ItemDefaultFuncs(o)
		Actions.TakeObject(char.Name, o.Name)

		o = Bladex.CreateEntity(netfuncs.gen_rand_name("EscudoInvPrb_"), "Escudo2", 0, 0, 0, "Weapon")
		ItemTypes.ItemDefaultFuncs(o)
		Actions.TakeObject(char.Name, o.Name)


	elif char.Kind == "Amazon_N":
		o = Bladex.CreateEntity(netfuncs.gen_rand_name("WeaponInvPrb_"), "Crosspear", 0, 0, 0, "Weapon")
		Actions.TakeObject(char.Name, o.Name)
		ItemTypes.ItemDefaultFuncs(o)
		
		o = Bladex.CreateEntity(netfuncs.gen_rand_name("WeaponInvPrb_"), "FireBo", 0, 0, 0, "Weapon")
		Actions.TakeObject(char.Name, o.Name)
		ItemTypes.ItemDefaultFuncs(o)


	elif char.Kind == "Barbarian_N":
		o = Bladex.CreateEntity(netfuncs.gen_rand_name("WeaponInvPrb_"), "FlatSword", 0, 0, 0, "Weapon")
		Actions.TakeObject(char.Name, o.Name)
		ItemTypes.ItemDefaultFuncs(o)


	elif char.Kind == "Dwarf_N":
		o = Bladex.CreateEntity(netfuncs.gen_rand_name("WeaponInvPrb_"), "Garrote2", 0, 0, 0, "Weapon")
		Actions.TakeObject(char.Name, o.Name)
		ItemTypes.ItemDefaultFuncs(o)

		o = Bladex.CreateEntity(netfuncs.gen_rand_name("EscudoInvPrb_"), "Escudo2", 0, 0, 0, "Weapon")
		Actions.TakeObject(char.Name, o.Name)
		ItemTypes.ItemDefaultFuncs(o)

		o = Bladex.CreateEntity(netfuncs.gen_rand_name("EscudoInvPrb_"), "Escudo2", 0, 0, 0, "Weapon")
		Actions.TakeObject(char.Name, o.Name)
		ItemTypes.ItemDefaultFuncs(o)

