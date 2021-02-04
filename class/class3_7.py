from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
base = int(input())
height = (base//2) + 1
for i in range(height):
    x = pos.x + i
    y = pos.y + i
    z = pos.z + i
    x2 = pos.x + base - i
    z2 = pos.z + base - i
    print(x,y,z,x2,y,z2)
    mc.setBlocks(x,y,z,x2,y,z2,24)
