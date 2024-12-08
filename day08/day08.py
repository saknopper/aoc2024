import itertools

with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

antennas = dict()
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col == '.':
            continue

        antennas_per_type = antennas.get(col, list())
        antennas_per_type.append((x, y))
        antennas[col] = antennas_per_type

def generate_antinode(starting_point, direction):
    (x, y) = (starting_point[0] + direction[0], starting_point[1] + direction[1])
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return (-1, -1)

    return (x, y)

def generate_antinodes(infinitely=False):
    antinodes = set()

    for antenna_type, positions in antennas.items():
        if infinitely:
            antinodes.update(positions)

        for combination in itertools.combinations(positions, 2):
            direction_vectors = ((combination[0][0] - combination[1][0], combination[0][1] - combination[1][1]),
                                 (combination[1][0] - combination[0][0], combination[1][1] - combination[0][1]))

            for i, c in enumerate(combination):
                starting_point = c
                for _ in range(999 if infinitely else 1):
                    (x, y) = generate_antinode(starting_point, direction_vectors[i])
                    if x == -1 and y == -1:
                        break
                    antinodes.add((x, y))
                    starting_point = (x, y)

    return len(antinodes)

print('Part A: {}'.format(generate_antinodes()))
print('Part B: {}'.format(generate_antinodes(True)))
