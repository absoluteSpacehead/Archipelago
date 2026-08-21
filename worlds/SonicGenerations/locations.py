from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items, names, regions

if TYPE_CHECKING:
    from .world import SonicGensWorld

LOCATION_NAME_TO_ID = {
    names.Locations.EGreen:     1,
    names.Locations.EPurple:    2,
    names.Locations.EBlue:      3,
    names.Locations.EYellow:    4,
    names.Locations.ERed:       5,
    names.Locations.ECyan:      6,
    names.Locations.EWhite:     7,

    names.Locations.BKGHZ:      50,
    names.Locations.BKCPZ:      51,
    names.Locations.BKSSZ:      52,
    names.Locations.BKSPH:      53,
    names.Locations.BKCTE:      54,
    names.Locations.BKSSH:      55,
    names.Locations.BKCSC:      56,
    names.Locations.BKEUC:      57,
    names.Locations.BKPLA:      58,

    names.Locations.ClearGHZ1:  100,
    names.Locations.ClearGHZ2:  101,
    names.Locations.ClearCPZ1:  102,
    names.Locations.ClearCPZ2:  103,
    names.Locations.ClearSSZ1:  104,
    names.Locations.ClearSSZ2:  105,
    names.Locations.ClearSPH1:  106,
    names.Locations.ClearSPH2:  107,
    names.Locations.ClearCTE1:  108,
    names.Locations.ClearCTE2:  109,
    names.Locations.ClearSSH1:  110,
    names.Locations.ClearSSH2:  111,
    names.Locations.ClearCSC1:  112,
    names.Locations.ClearCSC2:  113,
    names.Locations.ClearEUC1:  114,
    names.Locations.ClearEUC2:  115,
    names.Locations.ClearPLA1:  116,
    names.Locations.ClearPLA2:  117,
    names.Locations.ClearBMS:   118,
    names.Locations.ClearBSD:   119,
    names.Locations.ClearBSL:   120,
    names.Locations.ClearBDE:   121,
    names.Locations.ClearBPC:   122,
    names.Locations.ClearBNE:   123,
    names.Locations.ClearBLB:   124,

    names.Locations.ClearGHZ11: 125,
    names.Locations.ClearGHZ12: 126,
    names.Locations.ClearGHZ13: 127,
    names.Locations.ClearGHZ14: 128,
    names.Locations.ClearGHZ15: 129,
    names.Locations.ClearGHZ21: 130,
    names.Locations.ClearGHZ22: 131,
    names.Locations.ClearGHZ23: 132,
    names.Locations.ClearGHZ24: 133,
    names.Locations.ClearGHZ25: 134,

    names.Locations.ClearCPZ11: 135,
    names.Locations.ClearCPZ12: 136,
    names.Locations.ClearCPZ13: 137,
    names.Locations.ClearCPZ14: 138,
    names.Locations.ClearCPZ15: 139,
    names.Locations.ClearCPZ21: 140,
    names.Locations.ClearCPZ22: 141,
    names.Locations.ClearCPZ23: 142,
    names.Locations.ClearCPZ24: 143,
    names.Locations.ClearCPZ25: 144,

    names.Locations.ClearSSZ11: 145,
    names.Locations.ClearSSZ12: 146,
    names.Locations.ClearSSZ13: 147,
    names.Locations.ClearSSZ14: 148,
    names.Locations.ClearSSZ15: 149,
    names.Locations.ClearSSZ21: 150,
    names.Locations.ClearSSZ22: 151,
    names.Locations.ClearSSZ23: 152,
    names.Locations.ClearSSZ24: 153,
    names.Locations.ClearSSZ25: 154,

    names.Locations.ClearSPH11: 155,
    names.Locations.ClearSPH12: 156,
    names.Locations.ClearSPH13: 157,
    names.Locations.ClearSPH14: 158,
    names.Locations.ClearSPH15: 159,
    names.Locations.ClearSPH21: 160,
    names.Locations.ClearSPH22: 161,
    names.Locations.ClearSPH23: 162,
    names.Locations.ClearSPH24: 163,
    names.Locations.ClearSPH25: 164,

    names.Locations.ClearCTE11: 165,
    names.Locations.ClearCTE12: 166,
    names.Locations.ClearCTE13: 167,
    names.Locations.ClearCTE14: 168,
    names.Locations.ClearCTE15: 169,
    names.Locations.ClearCTE21: 170,
    names.Locations.ClearCTE22: 171,
    names.Locations.ClearCTE23: 172,
    names.Locations.ClearCTE24: 173,
    names.Locations.ClearCTE25: 174,

    names.Locations.ClearSSH11: 175,
    names.Locations.ClearSSH12: 176,
    names.Locations.ClearSSH13: 177,
    names.Locations.ClearSSH14: 178,
    names.Locations.ClearSSH15: 179,
    names.Locations.ClearSSH21: 180,
    names.Locations.ClearSSH22: 181,
    names.Locations.ClearSSH23: 182,
    names.Locations.ClearSSH24: 183,
    names.Locations.ClearSSH25: 184,

    names.Locations.ClearCSC11: 185,
    names.Locations.ClearCSC12: 186,
    names.Locations.ClearCSC13: 187,
    names.Locations.ClearCSC14: 188,
    names.Locations.ClearCSC15: 189,
    names.Locations.ClearCSC21: 190,
    names.Locations.ClearCSC22: 191,
    names.Locations.ClearCSC23: 192,
    names.Locations.ClearCSC24: 193,
    names.Locations.ClearCSC25: 194,

    names.Locations.ClearEUC11: 195,
    names.Locations.ClearEUC12: 196,
    names.Locations.ClearEUC13: 197,
    names.Locations.ClearEUC14: 198,
    names.Locations.ClearEUC15: 199,
    names.Locations.ClearEUC21: 200,
    names.Locations.ClearEUC22: 201,
    names.Locations.ClearEUC23: 202,
    names.Locations.ClearEUC24: 203,
    names.Locations.ClearEUC25: 204,

    names.Locations.ClearPLA11: 205,
    names.Locations.ClearPLA12: 206,
    names.Locations.ClearPLA13: 207,
    names.Locations.ClearPLA14: 208,
    names.Locations.ClearPLA15: 209,
    names.Locations.ClearPLA21: 210,
    names.Locations.ClearPLA22: 211,
    names.Locations.ClearPLA23: 212,
    names.Locations.ClearPLA24: 213,
    names.Locations.ClearPLA25: 214,
    
    names.Locations.ClearBMS1:  215,
    names.Locations.ClearBSD1:  216,
    names.Locations.ClearBSL1:  217,
    names.Locations.ClearBDE1:  218,
    names.Locations.ClearBPC1:  219,
    names.Locations.ClearBNE1:  220,
    names.Locations.ClearBLB1:  221,
}

def get_location_names_with_ids(locations: list[str]) -> dict[str, int | None]:
    return {name: LOCATION_NAME_TO_ID[name] for name in locations}

class SonicGensLocation(Location):
    game = names.GameName

def create_all_locations(world: SonicGensWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: SonicGensWorld) -> None:
    world.get_region(names.Regions.WSClassic).add_locations(get_location_names_with_ids([names.Locations.EPurple, names.Locations.EGreen, names.Locations.BKGHZ, names.Locations.BKCPZ, names.Locations.BKSSZ]), SonicGensLocation)
    world.get_region(names.Regions.WSDreamcast).add_locations(get_location_names_with_ids([names.Locations.EYellow, names.Locations.EBlue, names.Locations.BKSPH, names.Locations.BKCTE, names.Locations.BKSSH]), SonicGensLocation)
    world.get_region(names.Regions.WSModern).add_locations(get_location_names_with_ids([names.Locations.EWhite, names.Locations.ECyan, names.Locations.ERed, names.Locations.BKCSC, names.Locations.BKEUC, names.Locations.BKPLA]), SonicGensLocation)

    ghz1 = world.get_region(names.Regions.GHZ1)
    ghz2 = world.get_region(names.Regions.GHZ2)
    cpz1 = world.get_region(names.Regions.CPZ1)
    cpz2 = world.get_region(names.Regions.CPZ2)
    ssz1 = world.get_region(names.Regions.SSZ1)
    ssz2 = world.get_region(names.Regions.SSZ2)
    bms = world.get_region(names.Regions.BMS)
    bde = world.get_region(names.Regions.BDE)
    sph1 = world.get_region(names.Regions.SPH1)
    sph2 = world.get_region(names.Regions.SPH2)
    cte1 = world.get_region(names.Regions.CTE1)
    cte2 = world.get_region(names.Regions.CTE2)
    ssh1 = world.get_region(names.Regions.SSH1)
    ssh2 = world.get_region(names.Regions.SSH2)
    bsd = world.get_region(names.Regions.BSD)
    bpc = world.get_region(names.Regions.BPC)
    csc1 = world.get_region(names.Regions.CSC1)
    csc2 = world.get_region(names.Regions.CSC2)
    euc1 = world.get_region(names.Regions.EUC1)
    euc2 = world.get_region(names.Regions.EUC2)
    pla1 = world.get_region(names.Regions.PLA1)
    pla2 = world.get_region(names.Regions.PLA2)
    bsl = world.get_region(names.Regions.BSL)
    bne = world.get_region(names.Regions.BNE)
    blb = world.get_region(names.Regions.BLB)

    ghz1.add_locations(get_location_names_with_ids([names.Locations.ClearGHZ1]), SonicGensLocation)
    ghz2.add_locations(get_location_names_with_ids([names.Locations.ClearGHZ2]), SonicGensLocation)
    cpz1.add_locations(get_location_names_with_ids([names.Locations.ClearCPZ1]), SonicGensLocation)
    cpz2.add_locations(get_location_names_with_ids([names.Locations.ClearCPZ2]), SonicGensLocation)
    ssz1.add_locations(get_location_names_with_ids([names.Locations.ClearSSZ1]), SonicGensLocation)
    ssz2.add_locations(get_location_names_with_ids([names.Locations.ClearSSZ2]), SonicGensLocation)
    bms.add_locations(get_location_names_with_ids([names.Locations.ClearBMS]), SonicGensLocation)
    bde.add_locations(get_location_names_with_ids([names.Locations.ClearBDE]), SonicGensLocation)
    sph1.add_locations(get_location_names_with_ids([names.Locations.ClearSPH1]), SonicGensLocation)
    sph2.add_locations(get_location_names_with_ids([names.Locations.ClearSPH2]), SonicGensLocation)
    cte1.add_locations(get_location_names_with_ids([names.Locations.ClearCTE1]), SonicGensLocation)
    cte2.add_locations(get_location_names_with_ids([names.Locations.ClearCTE2]), SonicGensLocation)
    ssh1.add_locations(get_location_names_with_ids([names.Locations.ClearSSH1]), SonicGensLocation)
    ssh2.add_locations(get_location_names_with_ids([names.Locations.ClearSSH2]), SonicGensLocation)
    bsd.add_locations(get_location_names_with_ids([names.Locations.ClearBSD]), SonicGensLocation)
    bpc.add_locations(get_location_names_with_ids([names.Locations.ClearBPC]), SonicGensLocation)
    csc1.add_locations(get_location_names_with_ids([names.Locations.ClearCSC1]), SonicGensLocation)
    csc2.add_locations(get_location_names_with_ids([names.Locations.ClearCSC2]), SonicGensLocation)
    euc1.add_locations(get_location_names_with_ids([names.Locations.ClearEUC1]), SonicGensLocation)
    euc2.add_locations(get_location_names_with_ids([names.Locations.ClearEUC2]), SonicGensLocation)
    pla1.add_locations(get_location_names_with_ids([names.Locations.ClearPLA1]), SonicGensLocation)
    pla2.add_locations(get_location_names_with_ids([names.Locations.ClearPLA2]), SonicGensLocation)
    bsl.add_locations(get_location_names_with_ids([names.Locations.ClearBSL]), SonicGensLocation)
    bne.add_locations(get_location_names_with_ids([names.Locations.ClearBNE]), SonicGensLocation)
    blb.add_locations(get_location_names_with_ids([names.Locations.ClearBLB]), SonicGensLocation)

    if world.options.hard_bosses:
        bms.add_locations(get_location_names_with_ids([names.Locations.ClearBMS1]), SonicGensLocation)
        bde.add_locations(get_location_names_with_ids([names.Locations.ClearBDE1]), SonicGensLocation)
        bsd.add_locations(get_location_names_with_ids([names.Locations.ClearBSD1]), SonicGensLocation)
        bpc.add_locations(get_location_names_with_ids([names.Locations.ClearBPC1]), SonicGensLocation)
        bsl.add_locations(get_location_names_with_ids([names.Locations.ClearBSL1]), SonicGensLocation)
        bne.add_locations(get_location_names_with_ids([names.Locations.ClearBNE1]), SonicGensLocation)
        blb.add_locations(get_location_names_with_ids([names.Locations.ClearBLB1]), SonicGensLocation)

    if world.options.challenges:
        ghz1.add_locations(get_location_names_with_ids([names.Locations.ClearGHZ11, names.Locations.ClearGHZ12, names.Locations.ClearGHZ13, names.Locations.ClearGHZ14, names.Locations.ClearGHZ15]), SonicGensLocation)
        ghz2.add_locations(get_location_names_with_ids([names.Locations.ClearGHZ21, names.Locations.ClearGHZ22, names.Locations.ClearGHZ23, names.Locations.ClearGHZ24, names.Locations.ClearGHZ25]), SonicGensLocation)
        cpz1.add_locations(get_location_names_with_ids([names.Locations.ClearCPZ11, names.Locations.ClearCPZ12, names.Locations.ClearCPZ13, names.Locations.ClearCPZ14, names.Locations.ClearCPZ15]), SonicGensLocation)
        cpz2.add_locations(get_location_names_with_ids([names.Locations.ClearCPZ21, names.Locations.ClearCPZ22, names.Locations.ClearCPZ23, names.Locations.ClearCPZ24, names.Locations.ClearCPZ25]), SonicGensLocation)
        ssz1.add_locations(get_location_names_with_ids([names.Locations.ClearSSZ11, names.Locations.ClearSSZ12, names.Locations.ClearSSZ13, names.Locations.ClearSSZ14, names.Locations.ClearSSZ15]), SonicGensLocation)
        ssz2.add_locations(get_location_names_with_ids([names.Locations.ClearSSZ21, names.Locations.ClearSSZ22, names.Locations.ClearSSZ23, names.Locations.ClearSSZ24, names.Locations.ClearSSZ25]), SonicGensLocation)
        sph1.add_locations(get_location_names_with_ids([names.Locations.ClearSPH11, names.Locations.ClearSPH12, names.Locations.ClearSPH13, names.Locations.ClearSPH14, names.Locations.ClearSPH15]), SonicGensLocation)
        sph2.add_locations(get_location_names_with_ids([names.Locations.ClearSPH21, names.Locations.ClearSPH22, names.Locations.ClearSPH23, names.Locations.ClearSPH24, names.Locations.ClearSPH25]), SonicGensLocation)
        cte1.add_locations(get_location_names_with_ids([names.Locations.ClearCTE11, names.Locations.ClearCTE12, names.Locations.ClearCTE13, names.Locations.ClearCTE14, names.Locations.ClearCTE15]), SonicGensLocation)
        cte2.add_locations(get_location_names_with_ids([names.Locations.ClearCTE21, names.Locations.ClearCTE22, names.Locations.ClearCTE23, names.Locations.ClearCTE24, names.Locations.ClearCTE25]), SonicGensLocation)
        ssh1.add_locations(get_location_names_with_ids([names.Locations.ClearSSH11, names.Locations.ClearSSH12, names.Locations.ClearSSH13, names.Locations.ClearSSH14, names.Locations.ClearSSH15]), SonicGensLocation)
        ssh2.add_locations(get_location_names_with_ids([names.Locations.ClearSSH21, names.Locations.ClearSSH22, names.Locations.ClearSSH23, names.Locations.ClearSSH24, names.Locations.ClearSSH25]), SonicGensLocation)
        csc1.add_locations(get_location_names_with_ids([names.Locations.ClearCSC11, names.Locations.ClearCSC12, names.Locations.ClearCSC13, names.Locations.ClearCSC14, names.Locations.ClearCSC15]), SonicGensLocation)
        csc2.add_locations(get_location_names_with_ids([names.Locations.ClearCSC21, names.Locations.ClearCSC22, names.Locations.ClearCSC23, names.Locations.ClearCSC24, names.Locations.ClearCSC25]), SonicGensLocation)
        euc1.add_locations(get_location_names_with_ids([names.Locations.ClearEUC11, names.Locations.ClearEUC12, names.Locations.ClearEUC13, names.Locations.ClearEUC14, names.Locations.ClearEUC15]), SonicGensLocation)
        euc2.add_locations(get_location_names_with_ids([names.Locations.ClearEUC21, names.Locations.ClearEUC22, names.Locations.ClearEUC23, names.Locations.ClearEUC24, names.Locations.ClearEUC25]), SonicGensLocation)
        pla1.add_locations(get_location_names_with_ids([names.Locations.ClearPLA11, names.Locations.ClearPLA12, names.Locations.ClearPLA13, names.Locations.ClearPLA14, names.Locations.ClearPLA15]), SonicGensLocation)
        pla2.add_locations(get_location_names_with_ids([names.Locations.ClearPLA21, names.Locations.ClearPLA22, names.Locations.ClearPLA23, names.Locations.ClearPLA24, names.Locations.ClearPLA25]), SonicGensLocation)

def create_events(world: SonicGensWorld) -> None:
    pass