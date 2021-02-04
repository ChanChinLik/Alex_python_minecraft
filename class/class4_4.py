from mcpi.minecraft import Minecraft
from time import sleep 
from random import randint
mc = Minecraft.create()
while True:
    randint(0,10)
    sleep(0.2)
    mc.executeCommand("time add 300")