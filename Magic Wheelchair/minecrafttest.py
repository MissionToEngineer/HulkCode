from mcpi import minecraft
from mcpi import block
from time import sleep

mc = minecraft.Minecraft.create()

mc.postToChat("Hello world")

x, y, z = mc.player.getPos()

#mc.player.setPos(x, y+10, z)
#mc.setBlock(x+1, y, z, block.GOLD_ORE.id)
#mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 1)
flower = 38

while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y+2, z, block.TNT.id, 1)
    sleep(0.1)