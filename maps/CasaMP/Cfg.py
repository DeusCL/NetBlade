import Bladex
import LoadBar

LoadBar.DemoProgressBar(70, "Blade_progress3.jpg")

execfile("../../Scripts/sys_init.py")

Bladex.ReadLevel("casa.lvl")

execfile("../../Scripts/BladeInit.py")

execfile("sonidos.py")
execfile("Sonidospuntuales.py")

execfile("sol.py")
execfile("agua.py")
execfile("objs.py")

execfile("char_selection.py")

import Scorer
Scorer.SetVisible(0)
Bladex.SetListenerPosition(2)