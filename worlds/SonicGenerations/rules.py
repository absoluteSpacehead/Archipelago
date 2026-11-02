from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Entrance
from rule_builder.rules import Rule, CanReachLocation, HasAll, OptionFilter, Has, CanReachRegion
from . import names
from .options import CollectionRequired

if TYPE_CHECKING:
    from .world import SonicGensWorld

CAN_CLEAR_WSCE_STAGES   = CanReachLocation(names.Locations.ClearSSZ1) & CanReachLocation(names.Locations.ClearSSZ2)
HAS_WSCE_KEYS           = HasAll(names.Items.BKGHZ, names.Items.BKCPZ, names.Items.BKSSZ)
CAN_CLEAR_BDE           = CanReachLocation(names.Locations.ClearBDE)
CAN_CLEAR_WSDE_STAGES   = CanReachLocation(names.Locations.ClearSSH1) & CanReachLocation(names.Locations.ClearSSH2)
HAS_WSDE_KEYS           = HasAll(names.Items.BKSPH, names.Items.BKCTE, names.Items.BKSSH)
CAN_CLEAR_BPC           = CanReachLocation(names.Locations.ClearBPC)
CAN_CLEAR_WSDE_STAGES   = CanReachLocation(names.Locations.ClearPLA1) & CanReachLocation(names.Locations.ClearPLA2)
HAS_WSME_KEYS           = HasAll(names.Items.BKCSC, names.Items.BKEUC, names.Items.BKPLA)
CAN_CLEAR_BNE           = CanReachLocation(names.Locations.ClearBNE)
HAS_EMERALDS            = HasAll(names.Items.EGreen, names.Items.EPurple, names.Items.EBlue, names.Items.EYellow, names.Items.ERed, names.Items.ECyan, names.Items.EWhite)
CAN_GOAL                = CanReachRegion(names.Regions.BLB)

def set_location_rule(name: str, rule: Rule, world: SonicGensWorld) -> None:
    world.set_rule(world.get_location(name), rule)

def set_entrance_rule(from_name: str, to_name: str, rule: Rule, world: SonicGensWorld) -> None:
    entrance: Entrance = world.get_entrance(names.create_entrance_name(from_name, to_name))
    world.set_rule(entrance, rule)

def set_all_rules(world: SonicGensWorld) -> None:
    set_all_location_rules(world)
    set_all_entrance_rules(world)
    world.set_completion_rule(CAN_GOAL)

def set_all_entrance_rules(world: SonicGensWorld) -> None:
    set_entrance_rule(names.Regions.WSClassic, names.Regions.BMS, CAN_CLEAR_WSCE_STAGES, world)
    set_entrance_rule(names.Regions.WSClassic, names.Regions.BDE, HAS_WSCE_KEYS, world)
    set_entrance_rule(names.Regions.WSClassic, names.Regions.WSDreamcast, CAN_CLEAR_BDE, world)

    set_entrance_rule(names.Regions.WSDreamcast, names.Regions.BSD, CAN_CLEAR_WSDE_STAGES, world)
    set_entrance_rule(names.Regions.WSDreamcast, names.Regions.BPC, HAS_WSDE_KEYS, world)
    set_entrance_rule(names.Regions.WSDreamcast, names.Regions.WSModern, CAN_CLEAR_BPC, world)

    set_entrance_rule(names.Regions.WSModern, names.Regions.BSL, CAN_CLEAR_WSDE_STAGES, world)
    set_entrance_rule(names.Regions.WSModern, names.Regions.BNE, HAS_WSME_KEYS, world)
    set_entrance_rule(names.Regions.WSModern, names.Regions.BLB, CAN_CLEAR_BNE & HAS_EMERALDS & (OptionFilter(CollectionRequired, False) | Has(names.Items.CollectionItem, world.required_collection_count)), world)

def set_all_location_rules(world: SonicGensWorld) -> None:
    set_location_rule(names.Locations.EPurple, CAN_CLEAR_WSCE_STAGES, world)
    set_location_rule(names.Locations.EGreen, HAS_WSCE_KEYS, world)
    set_location_rule(names.Locations.EYellow, CAN_CLEAR_WSDE_STAGES, world)
    set_location_rule(names.Locations.EBlue, HAS_WSDE_KEYS, world)
    set_location_rule(names.Locations.ERed, CAN_CLEAR_WSDE_STAGES, world)
    set_location_rule(names.Locations.EWhite, CAN_CLEAR_WSDE_STAGES, world)
    set_location_rule(names.Locations.ECyan, HAS_WSME_KEYS, world)