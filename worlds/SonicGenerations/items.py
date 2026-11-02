from __future__ import annotations
from typing import TYPE_CHECKING, NamedTuple
from BaseClasses import Item, ItemClassification
from . import names
import math

if TYPE_CHECKING:
    from .world import SonicGensWorld

class ItemInfo(NamedTuple):
    id: int
    classification: ItemClassification

ITEM_NAME_TO_INFO = {
    names.Items.EGreen:         ItemInfo(1, ItemClassification.progression),
    names.Items.EPurple:        ItemInfo(2, ItemClassification.progression),
    names.Items.EBlue:          ItemInfo(3, ItemClassification.progression),
    names.Items.EYellow:        ItemInfo(4, ItemClassification.progression),
    names.Items.ERed:           ItemInfo(5, ItemClassification.progression),
    names.Items.ECyan:          ItemInfo(6, ItemClassification.progression),
    names.Items.EWhite:         ItemInfo(7, ItemClassification.progression),

    names.Items.Nothing:        ItemInfo(8, ItemClassification.filler),

    names.Items.CollectionItem: ItemInfo(9, ItemClassification.filler),

    names.Items.BKGHZ:          ItemInfo(50, ItemClassification.progression),
    names.Items.BKCPZ:          ItemInfo(51, ItemClassification.progression),
    names.Items.BKSSZ:          ItemInfo(52, ItemClassification.progression),
    names.Items.BKSPH:          ItemInfo(53, ItemClassification.progression),
    names.Items.BKCTE:          ItemInfo(54, ItemClassification.progression),
    names.Items.BKSSH:          ItemInfo(55, ItemClassification.progression),
    names.Items.BKCSC:          ItemInfo(56, ItemClassification.progression),
    names.Items.BKEUC:          ItemInfo(57, ItemClassification.progression),
    names.Items.BKPLA:          ItemInfo(58, ItemClassification.progression)
}

item_groups: dict[str, set[str]] = {
    names.Groups.ChaosEmeralds: {
        names.Items.EGreen,
        names.Items.EPurple,
        names.Items.EBlue,
        names.Items.EYellow,
        names.Items.ERed,
        names.Items.ECyan,
        names.Items.EWhite
    },
    names.Groups.BossKeys: {
        names.Items.BKGHZ,
        names.Items.BKCPZ,
        names.Items.BKSSZ,
        names.Items.BKSPH,
        names.Items.BKCTE,
        names.Items.BKSSH,
        names.Items.BKCSC,
        names.Items.BKEUC,
        names.Items.BKPLA
    }
}

filler_weights: dict[str, int] = {
    names.Items.Nothing: 50,
}

def get_item_names_to_id() -> dict[str, int]:
    return {name: ITEM_NAME_TO_INFO[name].id for name in ITEM_NAME_TO_INFO.keys()}

class SonicGensItem(Item):
    game = names.GameName

def create_filler(world: SonicGensWorld, num: int) -> list[Item]:
    choices: dict[str, int] = { ** filler_weights }
    collection_item_count: int = 0

    if not world.options.collection_required and collection_item_count != 90:
        choices[names.Items.CollectionItem] = 50;

    result: list[Item] = []

    for i in range(num):
        choice: str = world.random.choices(list(choices.keys()), list(choices.values()))[0]

        if choice == names.Items.CollectionItem:
            collection_item_count += 1

        result.append(world.create_item(choice))

    return result


def create_item_with_correct_classification(world: SonicGensWorld, name: str) -> SonicGensItem:
    info: ItemInfo = ITEM_NAME_TO_INFO[name]

    classification = info.classification

    if name == names.Items.CollectionItem and world.options.collection_required:
        classification = ItemClassification.progression

    return SonicGensItem(name, classification, info.id, world.player)

def create_all_items(world: SonicGensWorld) -> None:
    itempool: list[Item] = []

    for key, value in ITEM_NAME_TO_INFO.items():
        if value.classification != ItemClassification.filler:
            itempool += [world.create_item(key)]

    num_unfilled: int = len(world.multiworld.get_unfilled_locations(world.player))
    num: int = num_unfilled - len(itempool)

    # final part, uses all remaining slots if there are fewer than it wants
    if world.options.collection_required:
        # if there are fewer locations than we want, we will end up placing them in blb clear when trying to fill all slots, which then becomes impossible to reach
        # so, we need to subtract them from our available slot count
        num -= len(world.get_region(names.Regions.BLB).get_locations())

        # get pct, round up, cap to available slots
        target: int = min(math.ceil(90.0 * (world.options.required_collection_percent / 100.0)), num)

        # this is sent to the client to determine whether player should be able to enter blb
        world.required_collection_count = target

        # then, add the additional items, capping to the maximum 90 or the available slots (whichever is lower)
        target = min(target + world.options.additional_collection_items, min(90, num))

        # finally, create collection items and shove them into the pool
        itempool += [world.create_item(names.Items.CollectionItem) for _ in range(target)]

        # reset this so we can populate with filler
        num = num_unfilled - len(itempool)

    itempool += create_filler(world, num)

    world.multiworld.itempool += itempool
