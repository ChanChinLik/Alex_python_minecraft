from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    try:
        num = int(input("What do you want?"))
        break
    except:
        print("Error")
x,y,z= mc.player.getTilePos() 
mc.setBlock(x,y,z,num)

    
