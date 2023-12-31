# -*- coding: utf-8 -*-
from Preset.Model.PartBase import PartBase
from Preset.Model.GameObject import registerGenericClass

import mod.server.extraServerApi as serverApi

@registerGenericClass("BucketArrowPart")
class BucketArrowPart(PartBase):
	def __init__(self):
		PartBase.__init__(self)
		# 零件名称
		self.name = "空零件"

	def InitClient(self):
		"""
		@description 客户端的零件对象初始化入口
		"""
		PartBase.InitClient(self)
		self.ListenForEvent(
			serverApi.GetEngineNamespace() ,
			serverApi.GetEngineSystemName() ,
			"ProjectileDoHitEffectEvent",
			self,
			self.OnProjectileDoHitEffectEvent
		)

	def InitServer(self):
		"""
		@description 服务端的零件对象初始化入口
		"""
		PartBase.InitServer(self)

	def TickClient(self):
		"""
		@description 客户端的零件对象逻辑驱动入口
		"""
		PartBase.TickClient(self)

	def TickServer(self):
		"""
		@description 服务端的零件对象逻辑驱动入口
		"""
		PartBase.TickServer(self)

	def DestroyClient(self):
		"""
		@description 客户端的零件对象销毁逻辑入口
		"""
		PartBase.DestroyClient(self)

	def DestroyServer(self):
		"""
		@description 服务端的零件对象销毁逻辑入口
		"""
		PartBase.DestroyServer(self)

	def OnProjectileDoHitEffectEvent(self, args):
		pass
		print(args)