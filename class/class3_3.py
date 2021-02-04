from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getPos() #getPos()
    time.sleep(1)
    x = x+random.uniform(1,30)
    y = y+random.uniform(1,30)
    z = z+random.uniform(1,30)
    mc.spawnEntity(x+1,y,z,93)