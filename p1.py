from random import random
import time


def randList(n):
    r = 2147483647
    return [int(r*random()) for i in range(n)]


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap


def insert(array, i):
    if len(array) > 1:
        pivot = len(array)//2
        if i < array[pivot]:
            left = insert(array[:pivot], i)
            array = left + array[pivot:]
        else:
            right = insert(array[pivot:], i)
            array = array[:pivot] + right
    else:
        if i <= array[0]:
            array = [i] + array
        else:
            array = array + [i]
    return array


def main():
    n, m, k = input().split()
    n, m, k = (int(n), int(m), int(k))
    ring = input().split()
    for i in range(n):
        ring[i] = int(ring[i])
    ring = ring + ring[:m]
    sortedSub = sorted(ring)
    sortedSub = sortedSub[:k]
    smallestK = 2147483647
    for i in range(n):
        toDrop = ring[i]
        toAdd = ring[i+m]
        if toDrop < ring[-1]:
            if toDrop in sortedSub:
                sortedSub.remove(toDrop)
        if toAdd < ring[-1]:
            sortedSub = insert(sortedSub, toAdd)
        sortedSub = sortedSub[:k]

    print(sortedSub[-1])


@timing
def test(n, m, k):
    ring = randList(n)
    ring = ring + ring[:m+1]
    smallestK = 2147483647
    sortedSub = sorted(ring[:m+1])

    for i in range(n):
        subK = sortedSub[k-1]
        if subK < smallestK:
            smallestK = subK

        toDrop = ring[i]
        toAdd = ring[i+m+1]
        iDrop = sortedSub.index(toDrop)
        tempSub = sortedSub[:iDrop] + sortedSub[iDrop+1:]
        if toAdd < smallestK:
            sortedSub.insert(toAdd)

    print(smallestK)

if __name__ == 'main':
    main()
