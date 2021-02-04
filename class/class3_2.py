from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True: 
    hits = mc.events.pollProjectileHits() # 弓箭打方塊,他可以回傳方塊的坐標
    if len(hits) > 0 : #打到方塊
        hit = hits[0] 
        x,y,z = hit.pos.x , hit.pos.y , hit.pos.z
       # mc.player.setPos(x,y,z)
       #mc.setBlocks(x+1,y+1,z+1,x-1,y-1,z-1,46)
       # mc.setBlock(x,y+2,z,152)
        mc.createExplosion(x,y,z,50)
        