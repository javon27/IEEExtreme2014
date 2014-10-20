heroes = []
affinities = []
qualities = []
candidates = []
affinityPool = ['Intelligence', 'Strength', 'Agility']


def main():
    global heroes, affinities, qualities
    rosterSize, pickSize = input().split()
    rosterSize, pickSize = int(rosterSize), int(pickSize)

    for popularity in range(rosterSize):
        hero, affinity, ratio = input().split(',')
        heroes.append(hero)
        affinities.append(affinity)
        a, b = ratio.split(':')
        a, b = int(a), int(b)
        quality = int((a/(a+b))*100)*(popularity+1)
        qualities.append(quality)

    for pick in range(pickSize):
        add = qualities.index(max(qualities))
        candidates.append(add)
        qualities[add] = 0

    for i in candidates:
        print(heroes[i])

    print()
    print('This set of heroes:')
    for affinity in affinityPool:
        count = 0
        for x in candidates:
            if affinities[x] == affinity:
                count += 1
        percent = (count / len(candidates)) * 100
        print('Contains {0:.2f} percentage of {1}'.format(round(percent, 2), affinity))

main()
