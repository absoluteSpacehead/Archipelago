from typing import Any, Dict
from worlds.AutoWorld import World
from BaseClasses import MultiWorld
from . import items, locations, regions, rules, web_world, names
from . import options as gens_options

class SonicGensWorld(World):
    """
    Sonic Generations (2011)
    """

    game = names.GameName

    web = web_world.SonicGensWebWorld()

    options_dataclass = gens_options.SonicGensOptions
    options: gens_options.SonicGensOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.get_item_names_to_id()

    item_name_groups = items.item_groups

    origin_region_name = names.Regions.WSClassic

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

        self.required_collection_count = -1

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data

    def generate_early(self) -> None:
        if hasattr(self.multiworld, "generation_is_fake"):
            if hasattr(self.multiworld, "re_gen_passthrough"):
                if names.GameName in self.multiworld.re_gen_passthrough:
                    slot_data: Dict[str, Any] = self.multiworld.re_gen_passthrough[names.GameName]
                    self.required_collection_count = slot_data["required_collection_count"]
                
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)
    
    def create_items(self) -> None:
        items.create_all_items(self)
    
    def create_item(self, name: str) -> items.SonicGensItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> dict[str, Any]:
        result: dict[str, Any] = {}

        if self.options.hard_bosses:
            result["hard_bosses"] = True
        
        if self.options.collection_required:
            result["required_collection_count"] = self.required_collection_count

        return result