from mcpi.minecraft import Minecraft
mc = Minecraft.create()
a=0
x,y,z=mc.player.getTilePos()
while a<20:
    mc.setBlocks(x-10,y,z,x+10,y+10,z+1,19)
    z=z+5
    a=a+1