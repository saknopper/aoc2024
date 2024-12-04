
lines = []
with open('input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file]

def find_word_in_direction(start_x : int, start_y : int, direction : tuple, word : str) -> bool:
    found_word = str()
    for c in range(4):
        cur_x = start_x + (c * direction[0])
        cur_y = start_y + (c * direction[1])

        if cur_x < 0 or cur_y < 0 or cur_x >= len(lines[0]) or cur_y >= len(lines):
            break

        found_word += lines[cur_y][cur_x]

    return found_word == word

def find_words_in_shape(start_x : int, start_y : int, words : list) -> bool:
    found_word = str()
    for neighbour in ((0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        cur_x = start_x + neighbour[0]
        cur_y = start_y + neighbour[1]
        if cur_x < 0 or cur_y < 0 or cur_x >= len(lines[0]) or cur_y >= len(lines):
            break

        found_word += lines[cur_y][cur_x]

    return found_word in words

foundWordsA = 0
foundWordsB = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        for direction in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            if find_word_in_direction(x, y, direction, 'XMAS'):
                foundWordsA += 1

        if find_words_in_shape(x, y, ['ASMSM', 'AMSMS', 'ASSMM', 'AMMSS']):
            foundWordsB += 1

print('Part A: {}'.format(foundWordsA))
print('Part B: {}'.format(foundWordsB))
