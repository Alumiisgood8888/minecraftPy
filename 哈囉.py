from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=5
while t<14:
    mc.postToChat("哈囉!")
    t=t+2