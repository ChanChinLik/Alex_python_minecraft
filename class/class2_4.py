from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
while True:
    time.sleep(0.01)
    x,y,z=mc.player.getTilePos()
    a = mc.getBlock(x+1,y-1,z)#取前面之一下的方塊的ID
    b = mc.getBlock(x-1,y-1,z)#取後面之一下的方塊的ID
    c = mc.getBlock(x,y-1,z-1)#取左面之一下的方塊的ID
    d = mc.getBlock(x,y-1,z+1)#取右面之一下的方塊的ID
    if a == 8 or b == 8 or c == 8 or d == 8 or \
        a == 9 or b == 9 or c == 9 or d == 9:
        mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,20)
