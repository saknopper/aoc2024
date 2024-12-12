
with open('input.txt', 'r') as file:
    stones = [[int(col) for col in line.split()]
              for line in file.readlines()][0]

def get_numbers_for_blinks(times: int) -> int:
    counter_per_stone_type = {}
    for stone in stones:
        cnt = counter_per_stone_type.get(stone, 0)
        counter_per_stone_type[stone] = cnt + 1

    for _ in range(times):
        new_counter_per_stone_type = {}

        for item in counter_per_stone_type.items():
            stone = item[0]
            stone_str = str(stone)
            stone_str_len = len(stone_str)
            if stone == 0:
                cnt = new_counter_per_stone_type.get(1, 0)
                new_counter_per_stone_type[1] = cnt + item[1]
            elif stone_str_len % 2 == 0:
                lh = int(stone_str[: stone_str_len // 2])
                cnt = new_counter_per_stone_type.get(lh, 0)
                new_counter_per_stone_type[lh] = cnt + item[1]

                rh = int(stone_str[stone_str_len // 2:])
                cnt = new_counter_per_stone_type.get(rh, 0)
                new_counter_per_stone_type[rh] = cnt + item[1]
            else:
                cnt = new_counter_per_stone_type.get(stone * 2024, 0)
                new_counter_per_stone_type[stone * 2024] = cnt + item[1]

        counter_per_stone_type = new_counter_per_stone_type

    return sum(counter_per_stone_type.values())


print('Part A: {}'.format(get_numbers_for_blinks(25)))
print('Part B: {}'.format(get_numbers_for_blinks(75)))
