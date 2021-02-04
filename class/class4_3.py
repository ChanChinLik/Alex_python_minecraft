from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
Blen = 4
for j in range(4): #4time 
    for i in range(4):# 4time 4x4 =16 for i in range(16)
        num = random.randint(1,4)
        if num == 1:
            mc.setBlocks(x,y,z,x+Blen,y,z,1) # 前向
            x = x + Blen
        elif num == 2: 
            mc.setBlocks(x,y,z,x-Blen,y,z,1) #後向
            x = x - Blen
        elif num == 3: 
            mc.setBlocks(x,y,z,x,y,z+Blen,1) #left向
            z = z + Blen
        else:
            mc.setBlocks(x,y,z,x,y,z-Blen,1) #right向
            z = z - Blen
"""增加上和下"""