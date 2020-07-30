from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
while True:
    mc.executeCommand("time set 1000")
    time.sleep(2)