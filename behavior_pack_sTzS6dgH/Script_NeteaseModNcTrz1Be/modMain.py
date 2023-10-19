# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseModNcTrz1Be", version="0.0.1")
class Script_NeteaseModNcTrz1Be(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModNcTrz1BeServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModNcTrz1BeServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModNcTrz1BeClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModNcTrz1BeClientDestroy(self):
        pass
