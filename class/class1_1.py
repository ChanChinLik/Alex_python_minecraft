from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
mc.player.setTilePos(100,100,100)
print(mc.player.getTilePos())