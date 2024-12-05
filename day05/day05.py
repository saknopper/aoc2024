from functools import cmp_to_key

with open('input.txt', 'r') as file:
    (rules, updates) = file.read().split('\n\n')

cmp = cmp_to_key(lambda x, y: -(x + '|' + y in rules))

middlePageSums = [0, 0]
for update in updates.split():
    updatePages = update.split(',')
    sortedUpdatePages = sorted(updatePages, key=cmp)
    if updatePages == sortedUpdatePages:
        middlePageSums[0] += int(sortedUpdatePages[len(sortedUpdatePages) // 2])
    else:
        middlePageSums[1] += int(sortedUpdatePages[len(sortedUpdatePages) // 2])

print('Part A: {}'.format(middlePageSums[0]))
print('Part B: {}'.format(middlePageSums[1]))
