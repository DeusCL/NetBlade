import Bladex

# ***********************************
# *      Asignacion de sonidos      *
# ***********************************
AsignarSonidosRagnarCalled=0

def AsignarSonidosRagnar(Personaje):
	

	from AniSoundRgnX import *

	per=Bladex.GetEntity(Personaje)

	# Sonidos de eventos

	per.AddEventSound('shield_block', GolpeArmaEscudoRgn)
	per.AddEventSound('weapon_01_block', GolpeArmaArmaRgn)
	per.AddEventSound('impale', TajoEmpalanteRgn)
	per.AddEventSound('slash', TajoCortanteRgn)
	per.AddEventSound('mutilate', TajoMutilacionRgn)
	per.AddEventSound('crush', GolpeContundenteRgn)
	
	global AsignarSonidosRagnarCalled
	if AsignarSonidosRagnarCalled:
		return
	AsignarSonidosRagnarCalled=1



	# Sonidos de animaciones

	per.AddAnimSound('Rgn_g_21', EsfuerzoCorto3Rgn, 0.2000)
	per.AddAnimSound('Rgn_g_21', EsfuerzoCorto2Rgn, 0.6778)
	per.AddAnimSound('Rgn_g_21', SesgadoCortoAgudo, 0.1778)
	per.AddAnimSound('Rgn_g_21', SesgadoCortoAgudo, 0.6444)
	per.AddAnimSound('Rgn_g_17', EsfuerzoCorto3Rgn, 0.5970)
	per.AddAnimSound('Rgn_g_17', SesgadoCorto, 0.7460)
	per.AddAnimSound('Rgn_g_escape', EsfuerzoRgnMediano, 0.3529)
	per.AddAnimSound('Rgn_g_escape', SesgadoLargoAgudo, 0.5765)
	per.AddAnimSound('Rgn_g_d_r', EsfuerzoRgnMediano, 0.5059)
	per.AddAnimSound('Rgn_g_d_r', EsfuerzoCorto2Rgn, 0.5059)
	per.AddAnimSound('Rgn_g_d_r', SesgadoCortoAgudo, 0.5294)
	per.AddAnimSound('Rgn_g_d_l', EsfuerzoRgnMediano, 0.4725)
	per.AddAnimSound('Rgn_g_d_l', EsfuerzoCorto3Rgn, 0.4725)
	per.AddAnimSound('Rgn_g_d_l', SesgadoCortoAgudo, 0.5165)
	per.AddAnimSound('Rgn_g_03', EsfuerzoCorto5Rgn, 0.2388)
	per.AddAnimSound('Rgn_g_03', SesgadoLargoAgudo, 0.2836)
	per.AddAnimSound('Rgn_g_01', EsfuerzoGolpeAtrasRgn, 0.0820)
	per.AddAnimSound('Rgn_g_01', SesgadoLargoAgudo, 0.0984)
	per.AddAnimSound('Rgn_g_02', EsfuerzoCorto2Rgn, 0.2687)
	per.AddAnimSound('Rgn_g_02', SesgadoLargoAgudo, 0.2836)
	per.AddAnimSound('Rgn_g_06', EsfuerzoGolpeAtrasRgn, 0.1000)
	per.AddAnimSound('Rgn_g_06', SesgadoLargo, 0.4450)
	per.AddAnimSound('Rgn_g_07', EsfuerzoCorto3Rgn, 0.1642)
	per.AddAnimSound('Rgn_g_07', SesgadoLargoAgudo, 0.3284)
	per.AddAnimSound('Rgn_g_08', EsfuerzoCorto1Rgn, 0.3950)
	per.AddAnimSound('Rgn_g_08', SesgadoLargoAgudo, 0.4100)
	per.AddAnimSound('Rgn_g_09', EsfuerzoCorto2Rgn, 0.2900)
	per.AddAnimSound('Rgn_g_09', SesgadoCorto, 0.3080)
	per.AddAnimSound('Rgn_g_11', EsfuerzoGolpeLateralRgn, 0.4200)
	per.AddAnimSound('Rgn_g_11', SesgadoLargoGrave, 0.4700)
	per.AddAnimSound('Rgn_g_12', EsfuerzoGolpeLateralRgn, 0.4200)
	per.AddAnimSound('Rgn_g_12', SesgadoLargoGrave, 0.4700)
	per.AddAnimSound('Rgn_g_14', EsfuerzoGolpeLateralRgn, 0.1890)
	per.AddAnimSound('Rgn_g_14', SesgadoLargo, 0.3880)
	per.AddAnimSound('Rgn_g_15', EsfuerzoCorto5Rgn, 0.4900)
	per.AddAnimSound('Rgn_g_15', SesgadoLargo, 0.5000)
	per.AddAnimSound('Rgn_g_16', EsfuerzoGolpeAtrasRgn, 0.2480)
	per.AddAnimSound('Rgn_g_16', SesgadoLargo, 0.4900)
	per.AddAnimSound('Rgn_g_18', EsfuerzoGolpeFrontalRgn, 0.1100)
	per.AddAnimSound('Rgn_g_18', SesgadoLargo, 0.4000)
	per.AddAnimSound('Rgn_g_19', EsfuerzoCorto3Rgn, 0.4000)
	per.AddAnimSound('Rgn_g_19', SesgadoCortoAgudo, 0.4200)
	per.AddAnimSound('Rgn_g_20', EsfuerzoCorto1Rgn, 0.1570)
	per.AddAnimSound('Rgn_g_20', SesgadoCortoAgudo, 0.2270)
	per.AddAnimSound('Rgn_g_20', EsfuerzoCorto2Rgn, 0.3600)
	per.AddAnimSound('Rgn_g_20', SesgadoCorto, 0.3700)
	per.AddAnimSound('Rgn_g_20', SesgadoCortoAgudo, 0.3000)
	per.AddAnimSound('Rgn_g_22', EsfuerzoGolpeAtrasRgn, 0.3250)
	per.AddAnimSound('Rgn_g_22', SesgadoLargo, 0.4700)
	per.AddAnimSound('Rgn_g_22', SesgadoLargoAgudo, 0.5600)
	per.AddAnimSound('Rgn_g_22', SesgadoCorto, 0.8230)
	per.AddAnimSound('Rgn_g_26', EsfuerzoGolpeCabezaRgn, 0.3660)
	per.AddAnimSound('Rgn_g_26', SesgadoLargo, 0.4210)
	per.AddAnimSound('Rgn_g_26', SesgadoLargoAgudo, 0.6000)
	per.AddAnimSound('Rgn_g_26', EsfuerzoCorto5Rgn, 0.8540)
	per.AddAnimSound('Rgn_g_27', EsfuerzoGolpeArribaRgn, 0.2590)
	per.AddAnimSound('Rgn_g_27', SesgadoLargoAgudo, 0.6330)
	per.AddAnimSound('Rgn_g_27', SesgadoLargoGrave, 0.8600)
	per.AddAnimSound('Rgn_g_31', EsfuerzoCorto1Rgn, 0.2880)
	per.AddAnimSound('Rgn_g_31', SesgadoLargoAgudo, 0.2940)
	per.AddAnimSound('Rgn_g_31', EsfuerzoCorto2Rgn, 0.4390)
	per.AddAnimSound('Rgn_g_31', SesgadoLargoGrave, 0.4480)
	per.AddAnimSound('Rgn_g_31', EsfuerzoCorto3Rgn, 0.6550)



	per.AddAnimSound("Kgt_dth_n00", MuerteRagnar1, 0.1200)
	#per.AddAnimSound("Kgt_dth_n00", AndarRagnar1, 0.2000)
	#per.AddAnimSound("Kgt_dth_n00", AndarRagnar2, 0.4000)
	#per.AddAnimSound("Kgt_dth_n00", AndarRagnar1, 0.6000)
	#per.AddAnimSound("Kgt_dth_n00", AndarRagnar1, 0.7500)
	per.AddAnimSound("Kgt_dth_n00", CaidaRagnar1, 0.8000)
	per.AddAnimSound("Kgt_dth_n01", MuerteRagnar2, 0.1100)
	#per.AddAnimSound("Kgt_dth_n01", AndarRagnar1, 0.2200)
	#per.AddAnimSound("Kgt_dth_n01", AndarRagnar2, 0.4200)
	#per.AddAnimSound("Kgt_dth_n01", AndarRagnar1, 0.6200)
	#per.AddAnimSound("Kgt_dth_n01", AndarRagnar2, 0.7500)
	per.AddAnimSound("Kgt_dth_n01", CaidaRagnar1, 0.7800)
	per.AddAnimSound("Kgt_dth_n02", MuerteRagnar3, 0.1200)
	#per.AddAnimSound("Kgt_dth_n02", AndarRagnar1, 0.2200)
	#per.AddAnimSound("Kgt_dth_n02", AndarRagnar2, 0.4200)
	#per.AddAnimSound("Kgt_dth_n02", AndarRagnar1, 0.6200)
	#per.AddAnimSound("Kgt_dth_n02", AndarRagnar2, 0.7500)
	per.AddAnimSound("Kgt_dth_n02", CaidaRagnar1, 0.8000)
	per.AddAnimSound("Kgt_dth_n03", MuerteRagnar4, 0.1200)
	#per.AddAnimSound("Kgt_dth_n03", AndarRagnar1, 0.2200)
	#per.AddAnimSound("Kgt_dth_n03", AndarRagnar2, 0.4200)
	#per.AddAnimSound("Kgt_dth_n03", AndarRagnar1, 0.6200)
	#per.AddAnimSound("Kgt_dth_n03", AndarRagnar2, 0.7500)
	per.AddAnimSound("Kgt_dth_n03", CaidaRagnar1, 0.7550)
	per.AddAnimSound("Kgt_dth_n04", MuerteRagnar4, 0.1100)
	#per.AddAnimSound("Kgt_dth_n04", AndarRagnar1, 0.2200)
	#per.AddAnimSound("Kgt_dth_n04", AndarRagnar2, 0.4200)
	#per.AddAnimSound("Kgt_dth_n04", AndarRagnar1, 0.6200)
	#per.AddAnimSound("Kgt_dth_n04", AndarRagnar2, 0.7500)
	per.AddAnimSound("Kgt_dth_n04", CaidaRagnar1, 0.7600)
	per.AddAnimSound("Kgt_dth_n05", MuerteRagnar4, 0.1100)
	#per.AddAnimSound("Kgt_dth_n05", AndarRagnar1, 0.2200)
	#per.AddAnimSound("Kgt_dth_n05", AndarRagnar2, 0.4200)
	#per.AddAnimSound("Kgt_dth_n05", AndarRagnar1, 0.6200)
	#per.AddAnimSound("Kgt_dth_n05", AndarRagnar2, 0.7500)
	per.AddAnimSound("Kgt_dth_n05", CaidaRagnar1, 0.7700)
	per.AddAnimSound("Kgt_dth_n06", MuerteRagnar2, 0.1200)
	#per.AddAnimSound("Kgt_dth_n06", AndarRagnar2, 0.2200)
	#per.AddAnimSound("Kgt_dth_n06", AndarRagnar1, 0.4200)
	#per.AddAnimSound("Kgt_dth_n06", AndarRagnar2, 0.6200)
	#per.AddAnimSound("Kgt_dth_n06", AndarRagnar1, 0.7500)
	per.AddAnimSound("Kgt_dth_n06", CaidaRagnar1, 0.7900)
	per.AddAnimSound("Kgt_dth_c1", DesangreRagnar1, 0.1250)
	#per.AddAnimSound("Kgt_dth_c1", AndarRagnar1, 0.2250)
	#per.AddAnimSound("Kgt_dth_c1", AndarRagnar1, 0.3000)
	#per.AddAnimSound("Kgt_dth_c1", AndarRagnar2, 0.3800)
	#per.AddAnimSound("Kgt_dth_c1", AndarRagnar1, 0.4500)
	#per.AddAnimSound("Kgt_dth_c1", AndarRagnar1, 0.5000)
	#per.AddAnimSound("Kgt_dth_c1", AndarRagnar1, 0.6000)
	#per.AddAnimSound("Kgt_dth_c1", AndarRagnar2, 0.6800)
	#per.AddAnimSound("Kgt_dth_c1", AndarRagnar1, 0.7200)
	per.AddAnimSound("Kgt_dth_c1", CaidaRagnar1, 0.7800)
	per.AddAnimSound("Kgt_dth_c1", DesangreRagnar1, 0.2500)
	per.AddAnimSound("Kgt_dth_c2", DesangreRagnar1, 0.1250)
	per.AddAnimSound("Kgt_dth_c2", DesangreRagnar1, 0.2500)
	#per.AddAnimSound("Kgt_dth_c2", AndarRagnar1, 0.2250)
	#per.AddAnimSound("Kgt_dth_c2", AndarRagnar1, 0.3000)
	#per.AddAnimSound("Kgt_dth_c2", AndarRagnar2, 0.3800)
	#per.AddAnimSound("Kgt_dth_c2", AndarRagnar2, 0.4500)
	#per.AddAnimSound("Kgt_dth_c2", AndarRagnar1, 0.5000)
	#per.AddAnimSound("Kgt_dth_c2", AndarRagnar1, 0.6000)
	#per.AddAnimSound("Kgt_dth_c2", AndarRagnar2, 0.6800)
	#per.AddAnimSound("Kgt_dth_c2", AndarRagnar1, 0.7200)
	per.AddAnimSound("Kgt_dth_c2", CaidaRagnar1, 0.7720)
	per.AddAnimSound("Kgt_dth_c2", CaidaRagnar2, 0.8720)
	per.AddAnimSound("Kgt_dth_c3", DesangreRagnar1, 0.1250)
	per.AddAnimSound("Kgt_dth_c3", DesangreRagnar1, 0.2500)
	#per.AddAnimSound("Kgt_dth_c3", AndarRagnar1, 0.2250)
	#per.AddAnimSound("Kgt_dth_c3", AndarRagnar1, 0.3000)
	#per.AddAnimSound("Kgt_dth_c3", AndarRagnar2, 0.3800)
	##per.AddAnimSound("Kgt_dth_c3", AndarRagnar2, 0.4500)
	#per.AddAnimSound("Kgt_dth_c3", AndarRagnar1, 0.5000)
	#per.AddAnimSound("Kgt_dth_c3", AndarRagnar1, 0.6000)
	#per.AddAnimSound("Kgt_dth_c3", AndarRagnar2, 0.6800)
	##per.AddAnimSound("Kgt_dth_c3", AndarRagnar1, 0.7200)
	per.AddAnimSound("Kgt_dth_c3", CaidaRagnar1, 0.7220)
	per.AddAnimSound("Kgt_dth_c4", DesangreRagnar1, 0.1250)
	per.AddAnimSound("Kgt_dth_c4", DesangreRagnar1, 0.2500)
	#per.AddAnimSound("Kgt_dth_c4", AndarRagnar1, 0.2250)
	#per.AddAnimSound("Kgt_dth_c4", AndarRagnar1, 0.3000)
	#per.AddAnimSound("Kgt_dth_c4", AndarRagnar2, 0.3800)
	#per.AddAnimSound("Kgt_dth_c4", AndarRagnar2, 0.4500)
	#per.AddAnimSound("Kgt_dth_c4", AndarRagnar1, 0.5000)
	#per.AddAnimSound("Kgt_dth_c4", AndarRagnar1, 0.6000)
	#per.AddAnimSound("Kgt_dth_c4", AndarRagnar2, 0.6800)
	per.AddAnimSound("Kgt_dth_c4", CaidaRagnar1, 0.7000)
	per.AddAnimSound("Kgt_dth_c4", CaidaRagnar2, 0.8720)
	per.AddAnimSound("Kgt_dth_c5", DesangreRagnar1, 0.1250)
	per.AddAnimSound("Kgt_dth_c5", DesangreRagnar1, 0.2500)
	#per.AddAnimSound("Kgt_dth_c5", AndarRagnar1, 0.2250)
	#per.AddAnimSound("Kgt_dth_c5", AndarRagnar1, 0.3000)
	#per.AddAnimSound("Kgt_dth_c5", AndarRagnar2, 0.3800)
	#per.AddAnimSound("Kgt_dth_c5", AndarRagnar2, 0.4500)
	#per.AddAnimSound("Kgt_dth_c5", AndarRagnar1, 0.5000)
	#per.AddAnimSound("Kgt_dth_c5", AndarRagnar1, 0.6000)
	#per.AddAnimSound("Kgt_dth_c5", AndarRagnar2, 0.6800)
	#per.AddAnimSound("Kgt_dth_c5", AndarRagnar1, 0.7200)
	per.AddAnimSound("Kgt_dth_c5", CaidaRagnar1, 0.7720)
	per.AddAnimSound("Kgt_dth_c5", CaidaRagnar2, 0.5500)
	per.AddAnimSound("Kgt_dth_c6", DesangreRagnar1, 0.1250)
	per.AddAnimSound("Kgt_dth_c6", DesangreRagnar1, 0.2500)
	#per.AddAnimSound("Kgt_dth_c6", AndarRagnar1, 0.2250)
	#per.AddAnimSound("Kgt_dth_c6", AndarRagnar1, 0.3000)
	#per.AddAnimSound("Kgt_dth_c6", AndarRagnar2, 0.3800)
	#per.AddAnimSound("Kgt_dth_c6", AndarRagnar2, 0.4500)
	#per.AddAnimSound("Kgt_dth_c6", AndarRagnar1, 0.5000)
	#per.AddAnimSound("Kgt_dth_c6", AndarRagnar1, 0.6000)
	#per.AddAnimSound("Kgt_dth_c6", AndarRagnar2, 0.6800)
	#per.AddAnimSound("Kgt_dth_c6", AndarRagnar1, 0.7200)
	per.AddAnimSound("Kgt_dth_c6", CaidaRagnar1, 0.7700)

	per.AddAnimSound("Rgn_hurt_jog", HeridaRagnar1, 0.3000)
	per.AddAnimSound("Rgn_hurt_neck", HeridaRagnar2, 0.3000)
	per.AddAnimSound("Rgn_hurt_breast", HeridaRagnar3, 0.3000)
	per.AddAnimSound("Rgn_hurt_back", HeridaRagnar1, 0.3000)
	per.AddAnimSound("Rgn_hurt_r_arm", HeridaRagnar2, 0.3000)
	per.AddAnimSound("Rgn_hurt_l_arm", HeridaRagnar3, 0.3000)
	per.AddAnimSound("Rgn_hurt_r_leg", HeridaRagnar1, 0.3000)
	per.AddAnimSound("Rgn_hurt_l_leg", HeridaRagnar2, 0.3000)
	per.AddAnimSound("Rgn_hurt_f_head", HeridaRagnar3, 0.3000)
	per.AddAnimSound("Rgn_hurt_f_neck", HeridaRagnar1, 0.3000)
	per.AddAnimSound("Rgn_hurt_f_breast", HeridaRagnar2, 0.3000)
	per.AddAnimSound("Rgn_hurt_f_back", HeridaRagnar3, 0.3000)
	per.AddAnimSound("Rgn_hurt_f_r_arm", HeridaRagnar1, 0.3000)
	per.AddAnimSound("Rgn_hurt_f_l_arm", HeridaRagnar2, 0.3000)
	per.AddAnimSound("Rgn_hurt_f_r_leg", HeridaRagnar3, 0.3000)
	per.AddAnimSound("Rgn_hurt_f_l_leg", HeridaRagnar1, 0.3000)
	per.AddAnimSound("Rgn_hurt_f_lite", HeridaRagnar2, 0.3000)
	per.AddAnimSound("Rgn_hurt_f_big", HeridaRagnar3, 0.3000)
	per.AddAnimSound("Rgn_hurt_head", HeridaRagnar1, 0.3000)


	per.AddAnimSound("Rgn_laugh", RisaRagnar, 0.1235)
	per.AddAnimSound("Rgn_insult", InsultoRagnar, 0.1234)