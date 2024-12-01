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

distances = list()
similarities = list()
for i in range(len(left)):
    distances.append(abs(left[i] - right[i]))
    similarities.append(left[i] * right.count(left[i]))

print('Part A: {}'.format(sum(distances)))

print('Part B: {}'.format(sum(similarities)))