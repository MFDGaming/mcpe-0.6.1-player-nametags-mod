from sdk import Patch, Mod
from os import getcwd, sep

mod = Mod()

patches = [
    Patch(0x108260, b"\x00\xbf") # nop
]

for patch in patches:
    mod.add_patch(patch)

mod.save(getcwd() + sep + "player_nametags.mod")

