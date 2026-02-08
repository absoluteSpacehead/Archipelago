from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule

from . import names

if TYPE_CHECKING:
    from .world import SonicGensWorld

def set_all_rules(world: SonicGensWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_location_rules(world: SonicGensWorld) -> None:
    set_rule(world.get_location(names.Locations.EPurple), lambda state: state.can_reach_region(names.Regions.BMS, world.player))
    set_rule(world.get_location(names.Locations.EGreen), lambda state: state.can_reach_region(names.Regions.BDE, world.player))
    set_rule(world.get_location(names.Locations.EYellow), lambda state: state.can_reach_region(names.Regions.BSD, world.player))
    set_rule(world.get_location(names.Locations.EBlue), lambda state: state.can_reach_region(names.Regions.BPC, world.player))
    set_rule(world.get_location(names.Locations.ERed), lambda state: state.can_reach_region(names.Regions.PLA2, world.player)) # TODO: do you get this regardless of what your last level in modern era is?
    set_rule(world.get_location(names.Locations.EWhite), lambda state: state.can_reach_region(names.Regions.BSL, world.player))
    set_rule(world.get_location(names.Locations.ECyan), lambda state: state.can_reach_region(names.Regions.BNE, world.player))

def set_completion_condition(world: SonicGensWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.can_reach_location(names.Locations.ClearBLB, world.player)