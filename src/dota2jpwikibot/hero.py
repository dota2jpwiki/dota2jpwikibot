from typing import Dict
import gamefile

_ignores = [
    "Version",
    "npc_dota_hero_base",
    "npc_dota_hero_target_dummy",
]


class Hero:
    data = {}
    display_name = ""

    def __init__(self, data, display_name):
        self.data = data
        self.display_name = display_name


_heroes: Dict[str, Hero] = {}


for id in gamefile.npc_heroes:
    if id in _ignores:
        continue
    base = gamefile.npc_heroes["npc_dota_hero_base"].copy()
    base.update(gamefile.npc_heroes[id])
    _heroes[id] = Hero(base, "Missing")


def get_hero(hero_name):
    return _heroes[hero_name]


def hero_id_list():
    return filter(lambda h: h not in _ignores, _heroes.keys())
