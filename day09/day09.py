from dataclasses import dataclass
from enum import Enum

class ItemType(Enum):
    FILE = 1
    FREE = 2

@dataclass
class Item:
    type : ItemType
    length : int
    id : int

items_a = list()
items_b = list()
with open('input.txt', 'r') as file:
    for line in file.readlines():
        for i, it in enumerate(line.strip()):
            items_a.append(Item(ItemType.FILE, int(it), i // 2) if i % 2 == 0 else Item(ItemType.FREE, int(it), -1))
            items_b.append(Item(ItemType.FILE, int(it), i // 2) if i % 2 == 0 else Item(ItemType.FREE, int(it), -1))

def get_first_non_ending_free_block_index(items, min_size = 0) -> int:
    for i, item in enumerate(items):
        if item.type == ItemType.FREE and item.length >= min_size:
            for it in items[i+1:]:
                if it.type == ItemType.FILE:
                    return i

    return -1

def compact_files(items):
    free_block_idx = get_first_non_ending_free_block_index(items, 0)
    while free_block_idx != -1:
        free_block = items_a[free_block_idx]
        cur_item = items_a.pop()
        while cur_item.type != ItemType.FILE:
            cur_item = items_a.pop()

        if free_block.length > cur_item.length:
            items_a.insert(free_block_idx, cur_item)
            free_block.length -= cur_item.length
        elif free_block.length == cur_item.length:
            items_a[free_block_idx] = cur_item
        else:
            items_a[free_block_idx] = Item(ItemType.FILE, free_block.length, cur_item.id)
            cur_item.length -= free_block.length
            items_a.append(cur_item)

        free_block_idx = get_first_non_ending_free_block_index(items, 0)

def get_item_by_file_id(items, file_id):
    for i in range(len(items)):
        if items[i].id == file_id:
            return (i, items[i])

    return False

def defragment_files(items):
    for file_id in reversed([item.id for item in items if item.type == ItemType.FILE]):
        (cur_item_idx, cur_item) = get_item_by_file_id(items, file_id)

        free_block_idx = get_first_non_ending_free_block_index(items, cur_item.length)
        if free_block_idx != -1 and free_block_idx < cur_item_idx:
            free_block = items[free_block_idx]
            if free_block.length > cur_item.length:
                items[cur_item_idx] = Item(ItemType.FREE, cur_item.length, -1)
                items.insert(free_block_idx, cur_item)
                free_block.length -= cur_item.length
            elif free_block.length == cur_item.length:
                items[cur_item_idx] = Item(ItemType.FREE, cur_item.length, -1)
                items[free_block_idx] = cur_item


compact_files(items_a)
defragment_files(items_b)

sum_a = 0
block_pos = 0
for item in items_a:
    for i in range(item.length):
        sum_a += item.id * block_pos
        block_pos += 1

sum_b = 0
block_pos = 0
for item in items_b:
    for i in range(item.length):
        if item.type == ItemType.FILE:
            sum_b += item.id * block_pos
        block_pos += 1

print('Part A: {}'.format(sum_a))
print('Part B: {}'.format(sum_b))
