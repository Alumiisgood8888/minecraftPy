from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z =mc.player.getTilePos()

try:
    blockType = int(input("18"))
    mc.setBlock(x, y, z, blockType)
except:
    print("only number")