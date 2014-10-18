"""
pdf-source: coffee-empire-English.pdf
"""
layout = []
w = h = None
capacity = ['-', 'L', 'M', 'H']


def top(incomes, x, y):
    if y != 0:
        if incomes[y-1][x] >= 5 and layout[y-1][x] == 'H':
            return 1
    return 0


def bottom(incomes, x, y):
    if y != h-1:
        if incomes[y+1][x] >= 5 and layout[y+1][x] == 'H':
            return 1
    return 0


def left(incomes, x, y):
    if x != 0:
        if incomes[y][x-1] >= 5 and layout[y][x-1] == 'H':
            return 1
    return 0


def right(incomes, x, y):
    if x != w-1:
        if incomes[y][x+1] >= 5 and layout[y][x+1] == 'H':
            return 1
    return 0


def cornerValue(incomes, x, y):
    baseValue = incomes[y][x]
    baseValue += top(incomes, x, y)
    baseValue += bottom(incomes, x, y)
    baseValue += left(incomes, x, y)
    baseValue += right(incomes, x, y)
    return baseValue


def main():
    global w, h, layout
    w, h = input().split()
    w = int(w)
    h = int(h)

    for line in range(h):
        layout.append(input().split('*'))
    potentialCorners = []
    for y in range(h):
        for x in range(w):
            if layout[y][x] != 'H':
                potentialCorners.append((x, y))

    dailyIncomes = []
    for day in range(7):
        input()  # discard day text
        dailyIncomes.append([])
        for y in range(h):
            row = input().split('*')
            for i, each in enumerate(row):
                row[i] = int(each)
            dailyIncomes[day].append(row)

    best = (-1, -1)
    highestIncome = 0

    for px, py in potentialCorners:
        weekIncome = 0
        for day in range(7):
            cornerIncome = cornerValue(dailyIncomes[day], px, py)

            cap = capacity.index(layout[py][px])
            if cap == 0:
                cap = 1
            cornerIncome /= cap
            if cornerIncome >= 20:
                weekIncome += cornerIncome
        if weekIncome > highestIncome:
            highestIncome = weekIncome
            best = (px+1, py+1)

    bx, by = best
    print(str(bx)+' '+str(by))

main()
