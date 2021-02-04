from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def planttree(x,y,z,mc):
    mc.setBlocks(x+1,y+5,z+1,x-1,y+3,z-1,35,5)
    mc.setBlocks(x,y+4,z,x,y,z,17)

x,y,z = mc.player.getPos()
for i in range(0,10): #(start,end,step)
    for j in range(0,10):
        for h in range(0,10):
            planttree(x+i*5,y+j*5,z+j*5,mc)
