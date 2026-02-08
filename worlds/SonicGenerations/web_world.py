from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets
from . import names

class SonicGensWebWorld(WebWorld):
    game = names.GameName

    theme = "partyTime"