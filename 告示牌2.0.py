from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
message=[]
a=1
while a<5:
    message = input("message")
    message.append("message")
    a=a+1
mc.setSign(x,y,z,63,9,"messages")