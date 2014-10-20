def main():
    N = int(input())
    square = []
    rowSums = [0 for i in range(N)]
    colSums = [0 for i in range(N)]
    mainSum = 0
    antiSum = 0
    Sum = 0

    for i in range(N):
        row = []
        temp = input().split()
        for j in temp:
            row.append(int(j))
        square.append(row)

    magic = True
    for x in range(N):
        for y in range(N):
            a = square[x][y]
            rowSums[x] += a
            colSums[y] += a
            if x == y:
                mainSum += a
            elif (x + y) == (N - 1):
                antiSum += a
            if x > 0:
                if colSums[y] > Sum or rowSums[x] > Sum or mainSum > Sum or antiSum > Sum:
                    magic = False
        if x == 0:
            Sum = rowSums[0]

    # print('DEBUG:')
    # print(rowSums)
    # print(colSums)
    # print(mainSum)
    # print(antiSum)
    # print('END')

    if magic:
        print(0)
    else:
        bads = []
        for x in range(N):
            if rowSums[x] != mainSum:
                bads.append(x+1)
        for y in range(N):
            if colSums[y] != mainSum:
                bads.append(-(y+1))
        if antiSum != mainSum:
            bads.append(0)
        print(len(bads))
        for each in sorted(bads):
            print(each)

main()
