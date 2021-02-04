from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time 
x,y,z= mc.player.getTilePos() #取坐標
while True:
    time.sleep(1)# Delay 
    color = random.randint(0,15)
    mc.setBlocks(x+5,y,z+5,x-5,y,z-5,35,color)