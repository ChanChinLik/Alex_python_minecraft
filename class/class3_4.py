from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
for i in range(50):
    mc.setBlock(x-i,y-1,z,1)