from dataclasses import dataclass
import itertools

@dataclass
class Calibration:
    test_value: int
    numbers: list[int]

calibrations = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        (test_value, numbers) = line.strip().split(':')
        calibrations.append(Calibration(int(test_value), [int(i) for i in numbers.strip().split()]))

def all_combinations_for_operators_rec(numbers : list[int], current_value : int, operator : str, operators : list[str]) -> list[int]:
    if not len(numbers):
        return [current_value]

    new_value = -1
    match operator:
        case '*':
            new_value = current_value * numbers[0]
        case '+':
            new_value = current_value + numbers[0]
        case '||':
            new_value = int(str(current_value) + str(numbers[0]))

    return list(itertools.chain.from_iterable(all_combinations_for_operators_rec(numbers[1:], new_value, op, operators) for op in operators))

def all_combinations_for_operators(numbers : list[int], operators : list[str]) -> list[int]:
    return list(itertools.chain.from_iterable(all_combinations_for_operators_rec(numbers[1:], numbers[0], op, operators) for op in operators))

sum_a = 0
sum_b = 0
for c in calibrations:
    if c.test_value in all_combinations_for_operators(c.numbers, ['+', '*']):
        sum_a += c.test_value
        sum_b += c.test_value
    elif c.test_value in all_combinations_for_operators(c.numbers, ['+', '*', '||']):
        sum_b += c.test_value

print('Part A: {}'.format(sum_a))
print('Part B: {}'.format(sum_b))
