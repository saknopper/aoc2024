def is_out_of_bounds(x : int, y : int) -> bool:
    return x < 0 or y < 0 or y >= len(_map) or x >= len(_map[0])

def get_next_position_and_direction(current_pos : tuple, current_direction : tuple) -> tuple:
    next_pos = (current_pos[0] + current_direction[0], current_pos[1] + current_direction[1])
    if is_out_of_bounds(next_pos[0], next_pos[1]):
        raise RuntimeWarning('Out of bounds')

    while _map[next_pos[1]][next_pos[0]] == '#':
        current_direction = (-current_direction[1], current_direction[0])
        next_pos = (current_pos[0] + current_direction[0], current_pos[1] + current_direction[1])

    return (next_pos, current_direction)

with open('input.txt', 'r') as file:
    _map = [list(line.strip()) for line in file.readlines()]

current_pos = [(x, y) for y, row in enumerate(_map) for x, column in enumerate(row) if column == '^'][0]
current_direction = (0, -1)

visited = [ current_pos ]
directions = [ current_direction ]

while True:
    try:
        (next_pos, current_direction) = get_next_position_and_direction(current_pos, current_direction)
    except:
        break

    current_pos = next_pos
    if current_pos not in visited:
        visited.append(current_pos)
        directions.append(current_direction)

potential_obstacle_locations = []
for i, obstacle in enumerate(visited[1:]):
    _map[obstacle[1]][obstacle[0]] = '#'

    current_pos = visited[i-1]
    current_direction = directions[i-1]

    visitedWithDirection = []
    while True:
        visitedWithDirection.append((current_pos[0], current_pos[1], current_direction[0], current_direction[1]))

        try:
            (next_pos, current_direction) = get_next_position_and_direction(current_pos, current_direction)
        except:
            break

        if (next_pos[0], next_pos[1], current_direction[0], current_direction[1]) in visitedWithDirection:
            potential_obstacle_locations.append(obstacle)
            break

        current_pos = next_pos

    _map[obstacle[1]][obstacle[0]] = '.'

print('Part A: {}'.format(len(visited)))
print('Part B: {}'.format(len(potential_obstacle_locations)))
