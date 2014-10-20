def main():
    n = int(input())
    array = [int(a) for a in input().split()]
    nops = int(input())
    ops = []
    for line in range(nops):
        ops.append(int(input()))

    for op in ops:
        temp = []
        for i in range(n):
            temp.append(array[i]+array[(i+n-op) % n])
        array = temp[:]

    Sum = sum(array)
    Sum %= pow(10, 9)+7
    print(Sum)

main()
