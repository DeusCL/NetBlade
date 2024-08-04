import Reference

Bladex.RemoveScheduledFunc("anim:runner")

Bladex.SetTimeSpeed(0.1)

pers.SetTmpAnmFlags(1, 1, 1, 0, 5, 1, 0)
pers.Wuea = Reference.WUEA_ENDED
pers.LaunchAnmType("Rlx")

pers.Position = 0, -4000, 0
pers.SetOnFloor()

#"bng_mov" parameter
BM_IDC=0
BM_NONE=1
BM_XYZ=2
BM_XZ=3
BM_2ANM=4
BM_SCRIPT=5

#"headf" parameter
HEADF_ENG=0
HEADF_ANM=1
HEADF_ANM2SEE=2
HEADF_ANM2ENG=3


#(WUEA, MOD_Y, SOLF, COPY_ROT, BNG_MOV, HEADF)
def run_anm(pers):
	pers.Wuea = Reference.WUEA_NONE
	pers.SetTmpAnmFlags(0,0,0,0, 1, 1, 1)
	pers.LaunchAnmType("Wlk")#Wlk_no_Kgt


Bladex.AddScheduledFunc(Bladex.GetTime()+0.1, run_anm, (pers,), "anim:runner")

