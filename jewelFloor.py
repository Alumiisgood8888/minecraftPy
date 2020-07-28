from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.setBlocks(x-1000,y-1,z-1000,x+1000,y-1,z+1000,2)