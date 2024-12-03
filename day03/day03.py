import re

lines = []
with open('input.txt', 'r') as file:
    lines = [line for line in file]

regexA = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
regexB = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")

sumOfMulsA = 0
sumOfMulsB = 0
mulEnabled = True
for line in lines:
    sumOfMulsA += sum([int(match.groups()[0]) * int(match.groups()[1]) for match in regexA.finditer(line)])

    for match in regexB.finditer(line):
        if match.group() == "don't()":
            mulEnabled = False
        elif match.group() == "do()":
            mulEnabled = True
        elif mulEnabled:
            sumOfMulsB += int(match.groups()[0]) * int(match.groups()[1])

print('Part A: {}'.format(sumOfMulsA))
print('Part B: {}'.format(sumOfMulsB))
