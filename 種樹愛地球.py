from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
def Tree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,18)
    for i in range(10):
        for j in range(10):
            Tree(x+,y+,z+)
            time.sleep(1)
    
    
   
