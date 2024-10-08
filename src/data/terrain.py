from settings import *
from utils.colour import *


GRASS_COLOUR = GREEN.desaturate(0.5)
WATER_COLOUR = BLUE.desaturate(0.3).brighten(0.4)

class TerrainType:
    def __init__(self, name: str, slowdown_factor: int, defence_bonus: int, bg_colour, icon_text, text_colour)  -> None:
        self.name = name
        self.displayName = name.title()

        self.slowdown_factor = slowdown_factor  # in DT, this factor is different for diff. move types. especially no slowdown for flying units
        self.defence_bonus = defence_bonus  # maybe weaken bonus for flying units

        self.bg_colour = bg_colour
        self.icon_text = icon_text
        self.text_colour = text_colour
    

    def __repr__(self) -> str:
        if self.name == "grass": return " "  # probably temporary
        return self.name[0].upper()


terrains = dict()

terrains["forest"] = TerrainType(
    name="forest",

    slowdown_factor=2,
    defence_bonus=2,

    bg_colour=GRASS_COLOUR.darken(),
    icon_text="/\\ /\\",
    text_colour=GRASS_COLOUR.darken(0.2),
)

terrains["grass"] = TerrainType(
    name="grass",

    slowdown_factor=0,
    defence_bonus=1,

    bg_colour=GRASS_COLOUR,
    icon_text="",
    text_colour=WHITE,
)

terrains["sea"] = TerrainType(
    name="sea",

    slowdown_factor=999,
    defence_bonus=0,

    bg_colour=WATER_COLOUR,
    icon_text="~ ~",
    text_colour=WATER_COLOUR.darken()
)

