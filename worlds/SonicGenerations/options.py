from dataclasses import dataclass
from Options import Range, PerGameCommonOptions, Toggle

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

class RedStarRings(Toggle):
    """
    Should Red Star Rings be included?

    Adds 90 locations.
    """

    display_name = "Red Star Rings"
    
    default = 1

class CollectionRequired(Toggle):
    """
    Should a percentage of collection items be required to goal?

    Forces collection items into the pool as progression, rather than being part of the random filler selection.
    """

    display_name = "Collection Required"

class RequiredCollectionPercent(Range):
    """
    Percentage of the 90 collection items required to goal.

    Only the required items, plus however many additional items are set, will be added.
    """

    display_name = "Required Collection Percentage"

    range_start = 1
    range_end = 100
    default = 50

class AdditionalCollectionItems(Range):
    """
    Number of extra collection items above the required percentage to add to the pool.

    Caps out at either 90 items or the number of unfilled locations and does nothing when they are not required.
    """

    display_name = "Additional Collection Items"

    range_start = 0
    range_end = 90
    default = 15

@dataclass
class SonicGensOptions(PerGameCommonOptions):
    hard_bosses: HardBosses
    challenges: Challenges
    red_star_rings: RedStarRings
    collection_required: CollectionRequired
    required_collection_percent: RequiredCollectionPercent
    additional_collection_items: AdditionalCollectionItems

option_groups = []
option_presets = []