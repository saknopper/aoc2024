
def is_safe(report : list) -> bool:
    if report != sorted(report, reverse=False) and report != sorted(report, reverse=True):
        return False

    if all(abs(report[i] - report[i + 1]) >= 1 and abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1)):
        return True

    return False

def is_safe_dampened(report : list) -> bool:
    return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))

reports = []

with open('input.txt', 'r') as file:
    for line in file:
        reports.append([int(level) for level in line.split()])

safeA = 0
safeB = 0

for r in reports:
    if is_safe(r):
        safeA += 1
        safeB += 1
    elif is_safe_dampened(r):
        safeB += 1

print('Part A: {}'.format(safeA))
print('Part B: {}'.format(safeB))
