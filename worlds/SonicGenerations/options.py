from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Toggle

class HardBosses(Toggle):
    """
    Should hard mode bosses be included?
    This will change the goal to Time Eater (Hard Mode).
    
    Adds 7 locations.
    """

    display_name = "Hard Mode Bosses"

class Challenges(Toggle):
    """
    Should challenges be included?
    This does not add locations for the bells, only for challenge completion.

    Adds 90 locations.
    """

    display_name = "Challenges"

@dataclass
class SonicGensOptions(PerGameCommonOptions):
    hard_bosses: HardBosses
    challenges: Challenges

option_groups = []
option_presets = []