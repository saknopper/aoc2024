from collections import deque
from dataclasses import dataclass
from enum import Enum
import more_itertools
import itertools

class ItemType(Enum):
    FILE = 1
    FREE = 2

@dataclass
class Item:
    type : ItemType
    length : int
    id : int

items_a = deque()
items_b = deque()
with open('input.txt', 'r') as file:
    for line in file.readlines():
        for i, it in enumerate(line.strip()):
            items_a.append(Item(ItemType.FILE, int(it), i // 2) if i % 2 == 0 else Item(ItemType.FREE, int(it), -1))
            items_b.append(Item(ItemType.FILE, int(it), i // 2) if i % 2 == 0 else Item(ItemType.FREE, int(it), -1))

def has_non_ending_free_block(items, min_size = 0) -> bool:
    for w in more_itertools.windowed(items, n=2, step=1):
        if w[0].type == ItemType.FREE and w[1].type == ItemType.FILE and w[0].length >= min_size:
            return True

    return False

def get_first_non_ending_free_block_index(items, min_size = 0) -> int:
    for i in range(len(items)):
        if items[i].type == ItemType.FREE and items[i].length >= min_size:
            return i;

def compact_files(items):
    while has_non_ending_free_block(items, 0):
        free_block_idx = get_first_non_ending_free_block_index(items, 0);
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

def get_last_unchecked_item(items, item_id):
    for i in reversed(range(len(items))):
        if items[i].id == item_id:
            return (i, items[i])

    return False

def defragment_files(items):
    file_ids_to_check = [item.id for item in items if item.type == ItemType.FILE]

    while has_non_ending_free_block(items) and file_ids_to_check:
        file_id = file_ids_to_check.pop()
        (cur_item_idx, cur_item) = get_last_unchecked_item(items, file_id)
        if has_non_ending_free_block(items, cur_item.length):
            free_block_idx = get_first_non_ending_free_block_index(items, cur_item.length)
            free_block = items[free_block_idx]
            if free_block.length > cur_item.length:
                items[cur_item_idx] = Item(ItemType.FREE, cur_item.length, -1)
                items.insert(free_block_idx, cur_item)
                free_block.length -= cur_item.length
            elif free_block.length == cur_item.length:
                items[cur_item_idx] = Item(ItemType.FREE, cur_item.length, -1)
                items[free_block_idx] = cur_item

            # TODO combine adjacent free items into 1 item


compact_files(items_a)
defragment_files(items_b)

print(' ')
print(*items_b, sep='\n')
print(' ')

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
