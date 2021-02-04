from mcpi.minecraft import Minecraft
from random import randint
mc = Minecraft.create()
x,y,z = mc.player.getTilePos() #16x16
com = randint(0,15)
for i in range(16):
    for j in range(16):
        color = randint(0,15)
        mc.setBlock(x+i,y-1,z+j,35,color) 

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if com == data:
            mc.postToChat("You are Win")
            break
        elif com > data :
            mc.postToChat("this is big number")
        else:
            mc.postToChat("this is small number")
        """if 你打的方塊color比Com的color較大的時候要給玩家提示說你打的號碼太大
              你打的方塊color比Com的color較小的時候要給玩家提示說你打的號碼太小
        """
        
