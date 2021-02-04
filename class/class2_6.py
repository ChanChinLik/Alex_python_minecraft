from mcpi.minecraft import Minecraft
mc = Minecraft.create()
username = input("username?")
message = input()
mc.postToChat("<"+username+"> "+message)