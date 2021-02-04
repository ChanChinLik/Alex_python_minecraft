from mcpi.minecraft import Minecraft
mc = Minecraft.create()
ID = mc.getPlayerEntityId("APE_11")
x,y,z = mc.entity.getTilePos(ID)
mc.player.setPos(x,y,z)
mc.postToTitle(ID,"hello") #ipconfig