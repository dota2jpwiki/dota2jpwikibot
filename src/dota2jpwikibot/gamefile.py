import vpk
import vdf


gamedir = "G:/SteamLibrary/steamapps/common/dota 2 beta/"

npc_heroes = {}

# Load the vpk file
print("Loading vpk file...")
with vpk.open(gamedir + "game/dota/pak01_dir.vpk") as pak:
    # Load the vdf files
    print("Loading vdf files...")
    with pak.get_file("scripts/npc/npc_heroes.txt") as data:
        npc_heroes = vdf.loads(data.read().decode("utf-8"))["DOTAHeroes"]
