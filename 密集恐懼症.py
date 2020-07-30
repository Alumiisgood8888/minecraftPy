from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
number = 1
for i in range(8):
    for i in range(number):
        mc.spawnEntity(x,y,z,60)
    number = number*2