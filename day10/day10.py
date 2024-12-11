
with open('input.txt', 'r') as file:
    grid = [[-99 if col == '.' else int(col) for col in list(line.strip())]
            for line in file.readlines()]

start_positions = list()
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col == 0:
            start_positions.append((x, y))

def find_next_steps(cur_pos : tuple) -> list:
    steps = list()

    for diff in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        try:
            x = cur_pos[0] + diff[0]
            y = cur_pos[1] + diff[1]
            if x < 0 or y < 0:
                continue

            new_pos_height = grid[y][x]
            if new_pos_height - grid[cur_pos[1]][cur_pos[0]] == 1:
                steps.append((x, y))
        except:
            continue

    return steps

def find_paths_to_top(start_pos : tuple, cur_pos : tuple) -> int:
    if grid[cur_pos[1]][cur_pos[0]] == 9:
        summits_per_starting_point[start_pos].add(cur_pos)
        return 1

    number_of_paths = 0
    next_steps = find_next_steps(cur_pos)
    for new_pos in next_steps:
        number_of_paths += find_paths_to_top(start_pos, new_pos)

    return number_of_paths

summits_per_starting_point = {}
sum_of_possible_trails = 0
for pos in start_positions:
    summits_per_starting_point[pos] = set()
    sum_of_possible_trails += find_paths_to_top(pos, pos)

score_a = 0
for summits in summits_per_starting_point.values():
    score_a += len(summits)

print('Part A: {}'.format(score_a))
print('Part B: {}'.format(sum_of_possible_trails))
