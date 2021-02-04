from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True: 
    hits = mc.events.pollBlockHits() # 劍打方塊,他可以回傳方塊的坐標
    if len(hits) > 0 : #打到方塊
        hit = hits[0] 
        x,y,z = hit.pos.x , hit.pos.y , hit.pos.z
        mc.setBlock(x,y,z,41)

