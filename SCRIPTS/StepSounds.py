


def Init():
    import Bladex



    # *********************************
    # *    Default                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-piedra-1.wav', 'PasoDefault1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("default",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-2.wav', 'PasoDefault2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("default",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-3.wav', 'PasoDefault3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("default",s)






    # *********************************
    # *    DefaultEnemigos                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-piedra-1.wav', 'PasoDefaultEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("defaultEnemigos",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-2.wav', 'PasoDefaultEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("defaultEnemigos",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-3.wav', 'PasoDefaultEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("defaultEnemigos",s)






    # *********************************
    # *      Hierba                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/07-PAS51.wav', 'PasoHierba1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Hierba",s)

    s=Bladex.CreateSound('../../sounds/07-PAS52.wav', 'PasoHierba2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Hierba",s)

    s=Bladex.CreateSound('../../sounds/07-PAS53.wav', 'PasoHierba3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Hierba",s)

    s=Bladex.CreateSound('../../sounds/07-PAS54.wav', 'PasoHierba4')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Hierba",s)






    # *********************************
    # *      HierbaEnemigos                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/07-PAS51.wav', 'PasoHierbaEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("HierbaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/07-PAS52.wav', 'PasoHierbaEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("HierbaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/07-PAS53.wav', 'PasoHierbaEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("HierbaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/07-PAS54.wav', 'PasoHierbaEnemigos4')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("HierbaEnemigos",s)





    # *********************************
    # *      HierbaEqueleto                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-paso-hueso-hierba3.wav', 'PasoHierbaEsqueleto1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("HierbaEsqueleto",s)

    s=Bladex.CreateSound('../../sounds/M-paso-hueso-hierba4.wav', 'PasoHierbaEsqueleto2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("HierbaEsqueleto",s)


    # *********************************
    # *      HierbaMinotauro                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-mino-hierba.wav', 'PasoHierbaMinotauro1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("HierbaMinotauro",s)

    s=Bladex.CreateSound('../../sounds/paso-mino-hierba4.wav', 'PasoHierbaMinotauro2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("HierbaMinotauro",s)






    # *********************************
    # *     SigiloSobreHierba                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/07-PAS51.wav', 'SigiloSobreHierba1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreHierba",s)

    s=Bladex.CreateSound('../../sounds/07-PAS52.wav', 'SigiloSobreHierba2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreHierba",s)

    s=Bladex.CreateSound('../../sounds/07-PAS53.wav', 'SigiloSobreHierba3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreHierba",s)

    s=Bladex.CreateSound('../../sounds/07-PAS54.wav', 'SigiloSobreHierba4')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreHierba",s)






    # *********************************
    # *     Metal                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALR1.wav', 'PasoMetal1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Metal",s)

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALR2.wav', 'PasoMetal2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Metal",s)

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALL1.wav', 'PasoMetal3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Metal",s)

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALL2.wav', 'PasoMetal4')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Metal",s)







    # *********************************
    # *     MetalEnemigos                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALR1.wav', 'PasoMetalEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MetalEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALR2.wav', 'PasoMetalEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MetalEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALL1.wav', 'PasoMetalEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MetalEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALL2.wav', 'PasoMetalEnemigos4')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MetalEnemigos",s)








    # *********************************
    # *    SigiloSobreMetal                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALR1.wav', 'PasoSigiloSobreMetal1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMetal",s)

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALR2.wav', 'PasoSigiloSobreMetal2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMetal",s)

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALL1.wav', 'PasoSigiloSobreMetal3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMetal",s)

    s=Bladex.CreateSound('../../sounds/M-07-PASOSMETALL2.wav', 'PasoSigiloSobreMetal4')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMetal",s)






    # *********************************
    # *    Barro                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO1.wav', 'PasoBarro1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Barro",s)

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO3.wav', 'PasoBarro2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Barro",s)

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO6.wav', 'PasoBarro3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Barro",s)

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO7.wav', 'PasoBarro4')
    s.SendNotify=1
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Barro",s)







    # *********************************
    # *    BarroEnemigos                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO1.wav', 'PasoBarroEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("BarroEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO3.wav', 'PasoBarroEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("BarroEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO6.wav', 'PasoBarroEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("BarroEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO7.wav', 'PasoBarroEnemigos4')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("BarroEnemigos",s)







    # *********************************
    # *   SigiloSobreBarro                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO1.wav', 'PasoSigiloSobreBarro1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreBarro",s)

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO3.wav', 'PasoSigiloSobreBarro2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreBarro",s)

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO6.wav', 'PasoSigiloSobreBarro3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreBarro",s)

    s=Bladex.CreateSound('../../sounds/M-PASOBARRO7.wav', 'PasoSigiloSobreBarro4')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreBarro",s)






    # *********************************
    # *     Tierra                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-07-pas45.wav', 'PasoTierra1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Tierra",s)

    s=Bladex.CreateSound('../../sounds/M-07-pas46.wav', 'PasoTierra2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Tierra",s)

    s=Bladex.CreateSound('../../sounds/M-07-pas47.wav', 'PasoTierra3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Tierra",s)

    s=Bladex.CreateSound('../../sounds/M-07-pas48.wav', 'PasoTierra4')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Tierra",s)






    # *********************************
    # *     TierraEnemigos                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-07-pas45.wav', 'PasoTierraEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("TierraEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-07-pas46.wav', 'PasoTierraEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("TierraEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-07-pas47.wav', 'PasoTierraEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("TierraEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-07-pas48.wav', 'PasoTierraEnemigos4')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("TierraEnemigos",s)

        # *********************************
    # *     TierraMinotauro                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-mino-tierra.wav', 'PasoTierraMinotauro1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("TierraMinotauro",s)

    s=Bladex.CreateSound('../../sounds/paso-mino-tierra2.wav', 'PasoTierraMinotauro2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("TierraMinotauro",s)



    # *********************************
    # *    SigiloSobreTierra                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-07-pas45.wav', 'PasoSigiloSobreTierra1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreTierra",s)

    s=Bladex.CreateSound('../../sounds/M-07-pas46.wav', 'PasoSigiloSobreTierra2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreTierra",s)

    s=Bladex.CreateSound('../../sounds/M-07-pas47.wav', 'PasoSigiloSobreTierra3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreTierra",s)

    s=Bladex.CreateSound('../../sounds/M-07-pas48.wav', 'PasoSigiloSobreTierra4')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreTierra",s)






    # *********************************
    # *     Arena                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-paso3tie.wav', 'PasoArena1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Arena",s)

    s=Bladex.CreateSound('../../sounds/M-paso2tie.wav', 'PasoArena2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Arena",s)

    s=Bladex.CreateSound('../../sounds/M-paso3hie.wav', 'PasoArena3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Arena",s)

    s=Bladex.CreateSound('../../sounds/M-pasostie.wav', 'PasoArena4')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Arena",s)






    # *********************************
    # *     ArenaEnemigos                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-paso3tie.wav', 'PasoArenaEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("ArenaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-paso2tie.wav', 'PasoArenaEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("ArenaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-paso3hie.wav', 'PasoArenaEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("ArenaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-pasostie.wav', 'PasoArenaEnemigos4')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("ArenaEnemigos",s)



    # *********************************
    # *     ArenaMinotauro                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-mino-arena.wav', 'PasoArenaMinotauro1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("ArenaMinotauro",s)

    s=Bladex.CreateSound('../../sounds/paso-mino-arena2.wav', 'PasoArenaMinotauro2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("ArenaMinotauro",s)




    # *********************************
    # *    SigiloSobreArena                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-paso3tie.wav', 'PasoSigiloSobreArena1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreArena",s)

    s=Bladex.CreateSound('../../sounds/M-paso2tie.wav', 'PasoSigiloSobreArena2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreArena",s)

    s=Bladex.CreateSound('../../sounds/M-paso3hie.wav', 'PasoSigiloSobreArena3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreArena",s)

    s=Bladex.CreateSound('../../sounds/M-pasostie.wav', 'PasoSigiloSobreArena4')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreArena",s)






    # *********************************
    # *    Grava                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAL1.wav', 'PasoGrava1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Grava",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAL2.wav', 'PasoGrava2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Grava",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAL3.wav', 'PasoGrava3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Grava",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVA-R1.wav', 'PasoGrava4')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Grava",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAR2.wav', 'PasoGrava5')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Grava",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAR3.wav', 'PasoGrava6')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Grava",s)









    # *********************************
    # *    GravaEnemigos                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAL1.wav', 'PasoGravaEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("GravaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAL2.wav', 'PasoGravaEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("GravaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAL3.wav', 'PasoGravaEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("GravaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVA-R1.wav', 'PasoGravaEnemigos4')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("GravaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAR2.wav', 'PasoGravaEnemigos5')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("GravaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAR3.wav', 'PasoGravaEnemigos6')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("GravaEnemigos",s)



     # *********************************
    # *    GravaMinotauro                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-mino-grava.wav', 'PasoGravaMinotauro1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("GravaMinotauro",s)

    s=Bladex.CreateSound('../../sounds/paso-mino-grava2.wav', 'PasoGravaMinotauro2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("GravaMinotauro",s)




    # *********************************
    # *    SigiloSobreGrava                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAL1.wav', 'PasoSigiloSobreGrava1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreGrava",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAL2.wav', 'PasoSigiloSobreGrava2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreGrava",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAL3.wav', 'PasoSigiloSobreGrava3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreGrava",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVA-R1.wav', 'PasoSigiloSobreGrava4')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreGrava",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAR2.wav', 'PasoSigiloSobreGrava5')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreGrava",s)

    s=Bladex.CreateSound('../../sounds/M-07-CARR-GRAVAR3.wav', 'PasoSigiloSobreGrava6')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreGrava",s)








    # *********************************
    # *      Piedra                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-piedra-1.wav', 'PasoPiedra1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Piedra",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-2.wav', 'PasoPiedra2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Piedra",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-3.wav', 'PasoPiedra3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Piedra",s)





    # *********************************
    # *      PiedraEnemigos                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-piedra-1.wav', 'PasoPiedraEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PiedraEnemigos",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-2.wav', 'PasoPiedraEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PiedraEnemigos",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-3.wav', 'PasoPiedraEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PiedraEnemigos",s)



    # *********************************
    # *      PiedraMinotauro                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-mino-piedra.wav', 'PasoPiedraMinotauro1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PiedraMinotauro",s)

    s=Bladex.CreateSound('../../sounds/paso-mino-piedra3.wav', 'PasoPiedraMinotauro2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PiedraMinotauro",s)






    # *********************************
    # *     SigiloSobrePiedra                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-piedra-1.wav', 'PasoSigiloSobrePiedra1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobrePiedra",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-2.wav','PasoSigiloSobrePiedra2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobrePiedra",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-3.wav',' PasoSigiloSobrePiedra3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobrePiedra",s)








    # *********************************
    # *      PiedraEsqueleto                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-paso-hueso-piedra2.wav', 'PasoPiedraEsqueleto1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PiedraEsqueleto",s)

    s=Bladex.CreateSound('../../sounds/M-paso-hueso-piedra3.wav', 'PasoPiedraEsqueleto2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PiedraEsqueleto",s)





    # *********************************
    # *      PiedraGolem                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-golem-4.wav', 'PasoPiedraGolem1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=10000
    s.MaxDistance=30000
    Bladex.AddStepSound("PiedraGolem",s)

    s=Bladex.CreateSound('../../sounds/paso-golem-5.wav', 'PasoPiedraGolem2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=10000
    s.MaxDistance=30000
    Bladex.AddStepSound("PiedraGolem",s)

    s=Bladex.CreateSound('../../sounds/paso-golem-6.wav', 'PasoPiedraGolem3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=10000
    s.MaxDistance=30000
    Bladex.AddStepSound("PiedraGolem",s)









    # *********************************
    # *      PiedraCaos                 *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-6-PASOS-ARMAD-GRANDR4.wav', 'PasoPiedraCaos1')
    s.SendNotify=0
    s.Volume=0.3
    s.MinDistance=10000
    s.MaxDistance=30000
    Bladex.AddStepSound("PiedraCaos",s)

    s=Bladex.CreateSound('../../sounds/M-6-PASOS-ARMAD-GRANDR5.wav', 'PasoPiedraCaos2')
    s.SendNotify=0
    s.Volume=0.3
    s.MinDistance=10000
    s.MaxDistance=30000
    Bladex.AddStepSound("PiedraCaos",s)

    s=Bladex.CreateSound('../../sounds/M-6-PASOS-ARMAD-GRANDR8.wav', 'PasoPiedraCaos3')
    s.SendNotify=0
    s.Volume=0.3
    s.MinDistance=10000
    s.MaxDistance=30000
    Bladex.AddStepSound("PiedraCaos",s)






    # *********************************
    # *      MaderaTablas                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-madera-1.wav', 'PasoMaderaTablas1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("MaderaTablas",s)

    s=Bladex.CreateSound('../../sounds/paso-madera-2.wav', 'PasoMaderaTablas2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("MaderaTablas",s)

    s=Bladex.CreateSound('../../sounds/paso-madera-3.wav', 'PasoMaderaTablas3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("MaderaTablas",s)






    # *********************************
    # *      MaderaTablasEnemigos                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-madera-1.wav', 'PasoMaderaTablasEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaTablasEnemigos",s)

    s=Bladex.CreateSound('../../sounds/paso-madera-2.wav', 'PasoMaderaTablasEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaTablasEnemigos",s)




    s=Bladex.CreateSound('../../sounds/paso-madera-3.wav', 'PasoMaderaTablasEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaTablasEnemigos",s)




     # *********************************
    # *      MaderaTablasMinotauro                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-mino-madera.wav', 'PasoMaderaTablasMinotauro1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaTablasMinotauro",s)

    s=Bladex.CreateSound('../../sounds/paso-mino-madera2.wav', 'PasoMaderaTablasMinotauro2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaTablasMinotauro",s)




    # *********************************
    # *      SigiloSobreMaderaTablas                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-madera-1.wav', 'PasoSigiloSobreMaderaTablas1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMaderaTablas",s)

    s=Bladex.CreateSound('../../sounds/paso-madera-2.wav', 'PasoSigiloSobreMaderaTablas2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMaderaTablas",s)

    s=Bladex.CreateSound('../../sounds/paso-madera-3.wav', 'PasoSigiloSobreMaderaTablas3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMaderaTablas",s)





    # *********************************
    # *      MaderaPodrida                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-PASOASTILLADO-1.wav', 'PasoMaderaPodrida1')
    s.SendNotify=1
    s.Volume=0.9
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("MaderaPodrida",s)

    s=Bladex.CreateSound('../../sounds/M-PASOASTILLADO-2.wav', 'PasoMaderaPodrida2')
    s.SendNotify=1
    s.Volume=0.9
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("MaderaPodrida",s)

    s=Bladex.CreateSound('../../sounds/M-PASOASTILLADO-3.wav', 'PasoMaderaPodrida3')
    s.SendNotify=1
    s.Volume=0.9
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("MaderaPodrida",s)





    # *********************************
    # *      MaderaPodridaEnemigos                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-PASOASTILLADO-1.wav', 'PasoMaderaPodridaEnemigos1')
    s.SendNotify=0
    s.Volume=0.9
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaPodridaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-PASOASTILLADO-2.wav', 'PasoMaderaPodridaEnemigos2')
    s.SendNotify=0
    s.Volume=0.9
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaPodridaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-PASOASTILLADO-3.wav', 'PasoMaderaPodridaEnemigos3')
    s.SendNotify=0
    s.Volume=0.9
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaPodridaEnemigos",s)





    # *********************************
    # *      SigiloSobreMaderaPodrida                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-PASOASTILLADO-1.wav', 'PasoSigiloSobreMaderaPodrida1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMaderaPodrida",s)

    s=Bladex.CreateSound('../../sounds/M-PASOASTILLADO-2.wav', 'PasoSigiloSobreMaderaPodrida2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMaderaPodrida",s)

    s=Bladex.CreateSound('../../sounds/M-PASOASTILLADO-3.wav', 'PasoSigiloSobreMaderaPodrida3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMaderaPodrida",s)








    # *********************************
    # *      Madera                 *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-Pasomadera-.wav', 'PasoMadera1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Madera",s)

    s=Bladex.CreateSound('../../sounds/M-Pasomaderal.wav', 'PasoMadera2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Madera",s)

    s=Bladex.CreateSound('../../sounds/M-Pasomaderar.wav', 'PasoMadera3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Madera",s)






    # *********************************
    # *      MaderaEnemigos                 *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-Pasomadera-.wav', 'PasoMaderaEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-Pasomaderal.wav', 'PasoMaderaEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-Pasomaderar.wav', 'PasoMaderaEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaEnemigos",s)




    # *********************************
    # *      MaderaMinotauro                 *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-mino-maderar.wav', 'PasoMaderaMinotauro1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaMinotauro",s)

    s=Bladex.CreateSound('../../sounds/paso-mino-maderar2.wav', 'PasoMaderaMinotauro2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaMinotauro",s)





    # *********************************
    # *      SigiloSobreMadera                 *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-Pasomadera-.wav', 'PasoSigiloSobreMadera1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMadera",s)

    s=Bladex.CreateSound('../../sounds/M-Pasomaderal.wav', 'PasoSigiloSobreMadera2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMadera",s)

    s=Bladex.CreateSound('../../sounds/M-Pasomaderar.wav', 'PasoSigiloSobreMadera3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreMadera",s)






    # *********************************
    # *      MaderaEqueleto                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-paso-hueso-madera3.wav', 'PasoMaderaEsqueleto1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaEsqueleto",s)

    s=Bladex.CreateSound('../../sounds/M-paso-hueso-madera5.wav', 'PasoMaderaEsqueleto2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("MaderaEsqueleto",s)






    # *********************************
    # *      Agua                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAL1.wav', 'PasoAgua1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Agua",s)

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAL2.wav', 'PasoAgua2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Agua",s)

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAR1.wav', 'PasoAgua3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Agua",s)

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAR2.wav', 'PasoAgua4')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Agua",s)








    # *********************************
    # *      AguaEnemigos                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAL1.wav', 'PasoAguaEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("AguaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAL2.wav', 'PasoAguaEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("AguaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAR1.wav', 'PasoAguaEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("AguaEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAR2.wav', 'PasoAguaEnemigos4')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("AguaEnemigos",s)




    # *********************************
    # *      AguaMinotauro                  *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAPORMUSLOS1.wav', 'PasoAguaMinotauro1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("AguaMinotauro",s)

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAPORMUSLOS2.wav', 'PasoAguaMinotauro2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("AguaMinotauro",s)





    # *********************************
    # *      SigiloSobreAgua                   *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAL1.wav', 'PasoSigiloSobreAgua1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreAgua",s)

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAL2.wav', 'PasoSigiloSobreAgua2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreAgua",s)

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAR1.wav', 'PasoSigiloSobreAgua3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreAgua",s)

    s=Bladex.CreateSound('../../sounds/M-MOVENAGUAR2.wav', 'PasoSigiloSobreAgua4')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreAgua",s)





    # *********************************
    # *    Nieve     *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-00-NIEVEL1.wav', 'PasoNieve1')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Nieve",s)

    s=Bladex.CreateSound('../../sounds/M-00-NIEVEL2.wav', 'PasoNieve2')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Nieve",s)

    s=Bladex.CreateSound('../../sounds/M-00-NIEVER1.wav', 'PasoNieve3')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Nieve",s)

    s=Bladex.CreateSound('../../sounds/M-00-NIEVER2.wav', 'PasoNieve4')
    s.SendNotify=1
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=7000
    Bladex.AddStepSound("Nieve",s)





    # *********************************
    # *    NieveEnemigos     *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-00-NIEVEL1.wav', 'PasoNieveEnemigos1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("NieveEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-00-NIEVEL2.wav', 'PasoNieveEnemigos2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("NieveEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-00-NIEVER1.wav', 'PasoNieveEnemigos3')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("NieveEnemigos",s)

    s=Bladex.CreateSound('../../sounds/M-00-NIEVER2.wav', 'PasoNieveEnemigos4')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("NieveEnemigos",s)




    # *********************************
    # *    NieveMinotauro     *
    # *********************************

    s=Bladex.CreateSound('../../sounds/paso-mino-nieve.wav', 'PasoNieveMinotauro1')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("NieveMinotauro",s)

    s=Bladex.CreateSound('../../sounds/paso-mino-nieve3.wav', 'PasoNieveMinotauro2')
    s.SendNotify=0
    s.Volume=0.7
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("NieveMinotauro",s)








    # *********************************
    # *    SigiloSobreNieve     *
    # *********************************

    s=Bladex.CreateSound('../../sounds/M-00-NIEVEL1.wav', 'PasoSigiloSobreNieve1')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreNieve",s)

    s=Bladex.CreateSound('../../sounds/M-00-NIEVEL2.wav', 'PasoSigiloSobreNieve2')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreNieve",s)

    s=Bladex.CreateSound('../../sounds/M-00-NIEVER1.wav', 'PasoSigiloSobreNieve3')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreNieve",s)

    s=Bladex.CreateSound('../../sounds/M-00-NIEVER2.wav', 'PasoSigiloSobreNieve4')
    s.SendNotify=0
    s.Volume=0.5
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("SigiloSobreNieve",s)






    # *********************************
    # *    PasoAguaArmadura     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-agua-arm11.wav', 'PasoAguaArmadura1')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoAguaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-agua-arm22.wav', 'PasoAguaArmadura2')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoAguaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-agua-arm33.wav', 'PasoAguaArmadura3')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoAguaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-agua-arm44.wav', 'PasoAguaArmadura4')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoAguaArmadura",s)






    # *********************************
    # *    PasoArenaArmadura     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-arena-arm11.wav', 'PasoArenaArmadura1')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoArenaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-arena-arm-22.wav', 'PasoArenaArmadura2')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoArenaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-arena-arm-33.wav', 'PasoArenaArmadura3')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoArenaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-arena-arm44.wav', 'PasoArenaArmadura4')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoArenaArmadura",s)








    # *********************************
    # *    PasoAstilladoArmadura     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/pasoastillado-arm11.wav', 'PasoAstilladoArmadura1')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoAstilladoArmadura",s)

    s=Bladex.CreateSound('../../sounds/pasoastillado-arm22.wav', 'PasoAstilladoArmadura2')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoAstilladoArmadura",s)

    s=Bladex.CreateSound('../../sounds/pasoastillado-arm33.wav', 'PasoAstilladoArmadura3')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoAstilladoArmadura",s)






    # *********************************
    # *    PasoBarroArmadura     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-barro-arm11.wav', 'PasoBarroArmadura1')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoBarroArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-barro-arm22.wav', 'PasoBarroArmadura2')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoBarroArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-barro-arm33.wav', 'PasoBarroArmadura3')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoBarroArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-barro-arm44.wav', 'PasoBarroArmadura4')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoBarroArmadura",s)







    # *********************************
    # *    PasoGravaArmadura     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-grava-arm11.wav', 'PasoGravaArmadura1')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoGravaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-grava-arm22.wav', 'PasoGravaArmadura2')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoGravaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-grava-arm33.wav', 'PasoGravaArmadura3')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoGravaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-grava-arm44.wav', 'PasoGravaArmadura4')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoGravaArmadura",s)






    # *********************************
    # *    PasoHierbaArmadura     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-hierba-arm-11.wav', 'PasoHierbaArmadura1')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoHierbaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-hierba-arm-22.wav', 'PasoHierbaArmadura2')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoHierbaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-hierba-arm-33.wav', 'PasoHierbaArmadura3')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoHierbaArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-hierba-arm-44.wav', 'PasoHierbaArmadura4')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoHierbaArmadura",s)







    # *********************************
    # *    PasoMaderaTablasArmadura     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-maderatablas-arm11.wav', 'PasoMaderaTablasArmadura1')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoMaderaTablasArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-maderatablas-arm22.wav', 'PasoMaderaTablasArmadura2')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoMaderaTablasArmadura",s)






    # *********************************
    # *    PasoMetalArmadura     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-metal-arm-11.wav', 'PasoMetalArmadura1')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoMetalArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-metal-arm-22.wav', 'PasoMetalArmadura2')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoMetalArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-metal-arm-33.wav', 'PasoMetalArmadura3')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoMetalArmadura",s)







    # *********************************
    # *    PasoNieveArmadura     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-nieve-arm11.wav', 'PasoNieveArmadura1')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoNieveArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-nieve-arm22.wav', 'PasoNieveArmadura2')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoNieveArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-nieve-arm33.wav', 'PasoNieveArmadura3')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoNieveArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-nieve-arm44.wav', 'PasoNieveArmadura4')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoNieveArmadura",s)







    # *********************************
    # *    PasoTierraArmadura     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-tierra-arm11.wav', 'PasoTierraArmadura1')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoTierraArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-tierra-arm22.wav', 'PasoTierraArmadura2')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoTierraArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-tierra-arm33.wav', 'PasoTierraArmadura3')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoTierraArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-tierra-arm44.wav', 'PasoTierraArmadura4')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoTierraArmadura",s)







    # *********************************
    # *    PasoPiedraArmadura     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-piedra-arm-11.wav', 'PasoPiedraArmadura1')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoPiedraArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-arm-22.wav', 'PasoPiedraArmadura2')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoPiedraArmadura",s)

    s=Bladex.CreateSound('../../sounds/paso-piedra-arm-33.wav', 'PasoPiedraArmadura3')
    s.SendNotify=0
    s.Volume=0.4
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoPiedraArmadura",s)







    # *********************************
    # *    PasoLava     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-lava1.wav', 'PasoLava1')
    s.SendNotify=0
    s.Volume=1
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoLavaGolem",s)

    s=Bladex.CreateSound('../../sounds/paso-lava2.wav', 'PasoLava2')
    s.SendNotify=0
    s.Volume=1
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoLavaGolem",s)


    # *********************************
    # *    PasoBarroGolem     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-golem-barro1.wav', 'PasoBarroGolem1')
    s.SendNotify=0
    s.Volume=1
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoBarroGolem",s)

    s=Bladex.CreateSound('../../sounds/paso-golem-barro2.wav', 'PasoBarroGolem2')
    s.SendNotify=0
    s.Volume=1
    s.MinDistance=5000
    s.MaxDistance=15000
    Bladex.AddStepSound("PasoBarroGolem",s)


       # *********************************
    # *    PasoGdm     *
    # *********************************
    s=Bladex.CreateSound('../../sounds/paso-Gdm11.wav', 'PasoGdm1')
    s.SendNotify=0
    s.Volume=1
    s.MinDistance=1000
    s.MaxDistance=25000
    Bladex.AddStepSound("PasoGdm",s)

    s=Bladex.CreateSound('../../sounds/paso-Gdm22.wav', 'PasoGdm2')
    s.SendNotify=0
    s.Volume=1
    s.MinDistance=1000
    s.MaxDistance=25000
    Bladex.AddStepSound("PasoGdm",s)











    #************************************************************************************
    # TIPOS DE PASOS
    #************************************************************************************

    Bladex.AddMaterialStepSound("default","default","default")
    Bladex.AddMaterialStepSound("PisadaSigilo","Piedra","SigiloSobrePiedra")
    Bladex.AddMaterialStepSound("default","Piedra","Piedra")
    Bladex.AddMaterialStepSound("PisadaSigilo","Metal","SigiloSobreMetal")
    Bladex.AddMaterialStepSound("default","Metal","Metal")
    Bladex.AddMaterialStepSound("default","Barro","Barro")
    Bladex.AddMaterialStepSound("PisadaSigilo","Barro","SigiloSobreBarro")
    Bladex.AddMaterialStepSound("default","Tierra","Tierra")
    Bladex.AddMaterialStepSound("PisadaSigilo","Tierra","SigiloSobreTierra")
    Bladex.AddMaterialStepSound("default","Arena","Arena")
    Bladex.AddMaterialStepSound("PisadaSigilo","Arena","SigiloSobreArena")
    Bladex.AddMaterialStepSound("default","Grava","Grava")
    Bladex.AddMaterialStepSound("PisadaSigilo","Grava","SigiloSobreGrava")
    Bladex.AddMaterialStepSound("default","MaderaTablas","MaderaTablas")
    Bladex.AddMaterialStepSound("PisadaSigilo","MaderaTablas","SigiloSobreMaderaTablas")
    Bladex.AddMaterialStepSound("default","MaderaPodrida","MaderaPodrida")
    Bladex.AddMaterialStepSound("PisadaSigilo","MaderaPodrida","SigiloSobreMaderaPodrida")
    Bladex.AddMaterialStepSound("default","Madera","Madera")
    Bladex.AddMaterialStepSound("PisadaSigilo","Madera","SigiloSobreMadera")
    Bladex.AddMaterialStepSound("default","Nieve","Nieve")
    Bladex.AddMaterialStepSound("PisadaSigilo","Nieve","SigiloSobreNieve")
    Bladex.AddMaterialStepSound("default","Hierba","Hierba")
    Bladex.AddMaterialStepSound("PisadaSigilo","Hierba","SigiloSobreHierba")
    Bladex.AddMaterialStepSound("default","Water","Agua")
    Bladex.AddMaterialStepSound("PisadaSigilo","Water","SigiloSobreAgua")
    Bladex.AddMaterialStepSound("default","madera ligera","Madera")
    Bladex.AddMaterialStepSound("PisadaSigilo","madera ligera","SigiloSobreMadera")
    Bladex.AddMaterialStepSound("PisadaEsqueleto","Hierba","HierbaEsqueleto")
    Bladex.AddMaterialStepSound("PisadaEsqueleto","Madera","MaderaEsqueleto")
    Bladex.AddMaterialStepSound("PisadaEsqueleto","Piedra","PiedraEsqueleto")
    Bladex.AddMaterialStepSound("PisadaCaos","default","PiedraCaos")
    Bladex.AddMaterialStepSound("PisadaGolem","default","PiedraGolem")
    Bladex.AddMaterialStepSound("PisadaEnemigos","Hierba","HierbaEnemigos")
    Bladex.AddMaterialStepSound("PisadaEnemigos","Madera","MaderaEnemigos")
    Bladex.AddMaterialStepSound("PisadaEnemigos","MaderaPodrida","MaderaPodridaEnemigos")
    Bladex.AddMaterialStepSound("PisadaEnemigos","MaderaTablas","MaderaTablasEnemigos")
    Bladex.AddMaterialStepSound("PisadaEnemigos","Tierra","TierraEnemigos")
    Bladex.AddMaterialStepSound("PisadaEnemigos","Metal","MetalEnemigos")
    Bladex.AddMaterialStepSound("PisadaEnemigos","Piedra","PiedraEnemigos")
    Bladex.AddMaterialStepSound("PisadaEnemigos","Grava","GravaEnemigos")
    Bladex.AddMaterialStepSound("PisadaEnemigos","Arena","ArenaEnemigos")
    Bladex.AddMaterialStepSound("PisadaEnemigos","Agua","AguaEnemigos")
    Bladex.AddMaterialStepSound("PisadaEnemigos","Nieve","NieveEnemigos")
    Bladex.AddMaterialStepSound("PisadaEnemigos","Barro","BarroEnemigos")

    Bladex.AddMaterialStepSound("PisadaArmadura","Hierba","PasoHierbaArmadura")
    Bladex.AddMaterialStepSound("PisadaArmadura","Madera","PasoMaderaArmadura")
    Bladex.AddMaterialStepSound("PisadaArmadura","MaderaPodrida","PasoAstilladoArmadura")
    Bladex.AddMaterialStepSound("PisadaArmadura","MaderaTablas","PasoMaderaTablasArmadura")
    Bladex.AddMaterialStepSound("PisadaArmadura","Tierra","PasoTierraArmadura")
    Bladex.AddMaterialStepSound("PisadaArmadura","Metal","PasoMetalArmadura")
    Bladex.AddMaterialStepSound("PisadaArmadura","Piedra","PasoPiedraArmadura")
    Bladex.AddMaterialStepSound("PisadaArmadura","Grava","PasoGravaArmadura")
    Bladex.AddMaterialStepSound("PisadaArmadura","Arena","PasoArenaArmadura")
    Bladex.AddMaterialStepSound("PisadaArmadura","Agua","PasoAguaArmadura")
    Bladex.AddMaterialStepSound("PisadaArmadura","Nieve","PasoNieveArmadura")
    Bladex.AddMaterialStepSound("PisadaArmadura","Barro","PasoBarroArmadura")
    Bladex.AddMaterialStepSound("PisadaLavaGolem","default","PasoLavaGolem")
    Bladex.AddMaterialStepSound("PisadaBarroGolem","default","PasoBarroGolem")
    Bladex.AddMaterialStepSound("PisadaMinotauro","Hierba","NieveMinotauro")
    Bladex.AddMaterialStepSound("PisadaMinotauro","Madera","MaderaMinotauro")
    Bladex.AddMaterialStepSound("PisadaMinotauro","MaderaTablas","MaderaTablasMinotauro")
    Bladex.AddMaterialStepSound("PisadaMinotauro","Tierra","TierraMinotauro")
    Bladex.AddMaterialStepSound("PisadaMinotauro","Piedra","PiedraMinotauro")
    Bladex.AddMaterialStepSound("PisadaMinotauro","Grava","GravaMinotauro")
    Bladex.AddMaterialStepSound("PisadaMinotauro","Arena","ArenaMinotauro")
    Bladex.AddMaterialStepSound("PisadaMinotauro","Agua","AguaMinotauro")
    Bladex.AddMaterialStepSound("PisadaGdm","default","PasoGdm")





    #************************************************************************************
    # PASOS POR ACCIONES
    #************************************************************************************

    Bladex.AddActionStepSound("Knight","SNK_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","SNK_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","SNK_no","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","SNK_s","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","Rlx_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","Rlx_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","Rlx_no","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","Rlx_s","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","WBK_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","WBK_no","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","WBK_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","WBK_s","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","Attack_rlx_s","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","Attack_f_s","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","Attack_b_s","PisadaSigilo")
    Bladex.AddActionStepSound("Knight","default","default")
    Bladex.AddActionStepSound("Bar","default","default")
    Bladex.AddActionStepSound("Bar","WBK_s","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","WBK_no","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","WBK_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","WBK_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","Rlx_s","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","Rlx_no","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","Rlx_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","Rlx_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","SNK_s","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","SNK_no","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","SNK_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","SNK_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","Attack_b_s","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","Attack_f_s","PisadaSigilo")
    Bladex.AddActionStepSound("Bar","Attack_rlx_s","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","SNK_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","SNK_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","SNK_no","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","SNK_s","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","Rlx_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","Rlx_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","Rlx_no","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","Rlx_s","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","WBK_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","WBK_no","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","WBK_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","WBK_s","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","Attack_rlx_s","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","Attack_f_s","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","Attack_b_s","PisadaSigilo")
    Bladex.AddActionStepSound("Dwf","default","default")
    Bladex.AddActionStepSound("Amz","SNK_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","SNK_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","SNK_no","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","SNK_s","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","Rlx_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","Rlx_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","Rlx_no","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","Rlx_s","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","WBK_2h","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","WBK_no","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","WBK_1h","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","WBK_s","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","Attack_rlx_s","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","Attack_f_s","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","Attack_b_s","PisadaSigilo")
    Bladex.AddActionStepSound("Amz","default","default")
    Bladex.AddActionStepSound("default","default","default")
    Bladex.AddActionStepSound("Skl","default","PisadaEsqueleto")
    Bladex.AddActionStepSound("Chk","default","PisadaCaos")
    Bladex.AddActionStepSound("Glm_st","default","PisadaGolem")
    Bladex.AddActionStepSound("Ank","default","PisadaGdm")
    Bladex.AddActionStepSound("Dgk","default","PisadaArmadura")
    #Bladex.AddActionStepSound("Dkn","default","PisadaEnemigos")
    Bladex.AddActionStepSound("Dok","default","PisadaEnemigos")
    Bladex.AddActionStepSound("Gdm","default","PisadaGdm")
    Bladex.AddActionStepSound("Glm_cl","default","PisadaBarroGolem")
    Bladex.AddActionStepSound("Glm_lv","default","PisadaLavaGolem")
    Bladex.AddActionStepSound("Glm_mt","default","PisadaCaos")
    Bladex.AddActionStepSound("Gok","default","PisadaEnemigos")
    Bladex.AddActionStepSound("Lch","default","PisadaEnemigos")
    Bladex.AddActionStepSound("Ldm","default","PisadaEnemigos")
    Bladex.AddActionStepSound("Min","default","PisadaGdm")
    #Bladex.AddActionStepSound("Ork","default","PisadaEnemigos")
    #Bladex.AddActionStepSound("Rgn","default","PisadaEnemigos")
    Bladex.AddActionStepSound("Slm","default","PisadaEnemigos")
    #Bladex.AddActionStepSound("Tkn","default","PisadaEnemigos")
    Bladex.AddActionStepSound("Trl","default","PisadaEnemigos")
    Bladex.AddActionStepSound("Vmp","default","PisadaEnemigos")
    Bladex.AddActionStepSound("Cos","default","PisadaEnemigos")


    Bladex.AddActionStepSound("Knight_Traitor","default","PisadaArmadura")
    Bladex.AddActionStepSound("Ork","default","PisadaArmadura")
    Bladex.AddActionStepSound("Rgn","default","PisadaArmadura")
    Bladex.AddActionStepSound("Dkn","default","PisadaArmadura")
    Bladex.AddActionStepSound("Zkn","default","PisadaArmadura")
