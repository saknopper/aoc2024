#!/usr/bin/python3

left = list()
right = list()

with open('input.txt', 'r') as file:
    for line in file:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

distance = 0
similarity = 0
for i in range(len(left)):
    distance += abs(left[i] - right[i])
    similarity += left[i] * right.count(left[i])

print('Part A: {}'.format(distance))
print('Part B: {}'.format(similarity))