from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region, Entrance
from . import names

if TYPE_CHECKING:
    from .world import SonicGensWorld

def create_region(name: str, world: SonicGensWorld) -> Region:
    return Region(name, world.player, world.multiworld)

def create_entrance(eFrom: Region, eTo:Region):
    name:str = names.create_entrance_name(eFrom.name, eTo.name)
    
    res: Entrance = eFrom.connect(eTo, name)
    
    return res

# TODO: mission regions, one per era. not priority unless i decide i hate myself enough for move rando because then access to all missions will depend on whatever the levels in that era require
def create_and_connect_regions(world: SonicGensWorld) -> None:
    wsce    = create_region(names.Regions.WSClassic, world)
    wsde    = create_region(names.Regions.WSDreamcast, world)
    wsme    = create_region(names.Regions.WSModern, world)

    ghz1    = create_region(names.Regions.GHZ1, world)
    ghz2    = create_region(names.Regions.GHZ2, world)
    cpz1    = create_region(names.Regions.CPZ1, world)
    cpz2    = create_region(names.Regions.CPZ2, world)
    ssz1    = create_region(names.Regions.SSZ1, world)
    ssz2    = create_region(names.Regions.SSZ2, world)
    bms     = create_region(names.Regions.BMS, world)
    bde     = create_region(names.Regions.BDE, world)
    sph1    = create_region(names.Regions.SPH1, world)
    sph2    = create_region(names.Regions.SPH2, world)
    cte1    = create_region(names.Regions.CTE1, world)
    cte2    = create_region(names.Regions.CTE2, world)
    ssh1    = create_region(names.Regions.SSH1, world)
    ssh2    = create_region(names.Regions.SSH2, world)
    bsd     = create_region(names.Regions.BSD, world)
    bpc     = create_region(names.Regions.BPC, world)
    csc1    = create_region(names.Regions.CSC1, world)
    csc2    = create_region(names.Regions.CSC2, world)
    euc1    = create_region(names.Regions.EUC1, world)
    euc2    = create_region(names.Regions.EUC2, world)
    pla1    = create_region(names.Regions.PLA1, world)
    pla2    = create_region(names.Regions.PLA2, world)
    bsl     = create_region(names.Regions.BSL, world)
    bne     = create_region(names.Regions.BNE, world)
    blb     = create_region(names.Regions.BLB, world)

    world.multiworld.regions += [wsce, wsde, wsme, ghz1, ghz2, cpz1, cpz2, ssz1, ssz2, bms, bde, sph1, sph2, cte1, cte2, ssh1, ssh2, bsd, bpc, csc1, csc2, euc1, euc2, pla1, pla2, bsl, bne, blb]

    create_entrance(wsce, ghz1)
    create_entrance(wsce, ghz2)
    create_entrance(wsce, cpz1)
    create_entrance(wsce, cpz2)
    create_entrance(wsce, ssz1)
    create_entrance(wsce, ssz2)
    create_entrance(wsce, bms)
    create_entrance(wsce, bde)
    create_entrance(wsce, wsde)

    create_entrance(wsde, sph1)
    create_entrance(wsde, sph2)
    create_entrance(wsde, cte1)
    create_entrance(wsde, cte2)
    create_entrance(wsde, ssh1)
    create_entrance(wsde, ssh2)
    create_entrance(wsde, bsd)
    create_entrance(wsde, bpc)
    create_entrance(wsde, wsme)

    create_entrance(wsme, csc1)
    create_entrance(wsme, csc2)
    create_entrance(wsme, euc1)
    create_entrance(wsme, euc2)
    create_entrance(wsme, pla1)
    create_entrance(wsme, pla2)
    create_entrance(wsme, bsl)
    create_entrance(wsme, bne)
    create_entrance(wsme, blb)