from mcpi.minecraft import Minecraft
mc = Minecraft.create()
listoa = []
listob = []
listoc = []
for i in range(1,4):
    listoa.append(i*1)
    listob.append(i*2)
    listoc.append(i*3)
x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,2,str(listoa),str(listob),str(listoc))