import Actions
import Sparks
import ItemTypes
import CharStats
import random
import netfuncs
import AniSound
import Reference
import Basic_Funcs
import Sparks
import Breakings


net_state = netfuncs.get_net_state()

kind = net_state['KIND']

char = Bladex.CreateEntity("Player1", kind, -111000,7500,80000, "Person")
char.Data = Basic_Funcs.PlayerPerson(char)
char.Angle = 0
char.Level = 0
char.Life = CharStats.GetCharMaxLife(char.Kind, char.Level)

char.SendTriggerSectorMsgs = 1


