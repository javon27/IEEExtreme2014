"""
pdf-source: assembly-simulator-English.pdf
"""
size = 0
memory = []
temp = None
pc = 0  # program counter
labels = {}
program = []
keywords = ['PRINT', 'MOVE', 'ADD', 'SUB', 'AND', 'OR', 'XOR', 'COMP',
            'BEQ', 'BNE', 'BGT', 'BLT', 'BGE', 'BLE', 'END']


def END():
    pass


def hPrint(n, end='\n'):
    s = hex(n)[2:].upper()
    if len(s) == 1:
        s = '0'+s
    print(s, end=end)


def cleanArgs(args):
    n = None
    p1 = False
    a1 = None
    p2 = False
    a2 = None
    args = args.split(',')
    for i, each in enumerate(args):
        args[i] = each.strip()

    if len(args) == 0:
        a1 = args[0]
    else:
        if '#' in args[0]:
            n = int(args[0].strip('#'), 16)
            if '(' in args[1]:
                p1 = True
                a1 = int(args[1][1:-1], 16)
            else:
                a1 = int(args[1], 16)
        elif '(' in args[0]:
            p1 = True
            a1 = int(args[0][1:-1], 16)
            if '(' in args[1]:
                p2 = True
                a2 = int(args[1][1:-1], 16)
            else:
                a2 = int(args[1], 16)
        else:
            a1 = int(args[0], 16)
            if '(' in args[1]:
                p2 = True
                a2 = int(args[1][1:-1], 16)
            else:
                a2 = int(args[1], 16)
    return (n, p1, a1, p2, a2)


def PRINT(args):
    args = args.split(',')
    if (len(args) > 2 or len(args) == 0):
        raise TypeError
    elif len(args) == 1:
        a1 = int(args[0], 16)
        hPrint(memory[a1])
    else:
        a1, a2 = args
        a1 = int(a1, 16)
        a2 = int(a2, 16)
        for i in range(a1, a2):
            hPrint(memory[i], end=' ')
        hPrint(memory[a2])


def MOVE(args):
    n, p1, a1, p2, a2 = cleanArgs(args)
    if n is not None:
        if p1:
            MOVE2(n, a1)
        else:
            MOVE1(n, a1)
    elif p1 and (not p2):
        MOVE3(a1, a2)
    elif p1 and p2:
        MOVE4(a1, a2)
    elif (not p1) and p2:
        MOVE5(a1, a2)
    else:
        MOVE6(a1, a2)


def MOVE1(n, a1):  # MOVE #N,A1
    global memory
    memory[a1] = n


def MOVE2(n, a1):  # MOVE #N, (A1)
    global memory
    memory[memory[a1]] = n


def MOVE3(a1, a2):  # MOVE (A1),A2
    global memory
    memory[a2]


def MOVE4(a1, a2):  # MOVE (A1), (A2)
    global memory
    memory[memory[a2]] = memory[memory[a1]]


def MOVE5(a1, a2):  # MOVE A1, (A2)
    global memory
    memory[memory[a2]] = memory[a1]


def MOVE6(a1, a2):  # MOVE A1,A2
    global memory
    memory[a2] = memory[a1]


def ADD(args):
    n, p1, a1, p2, a2 = cleanArgs(args)
    if n is not None:
        ADD1(n, a1)
    else:
        ADD2(a1, a2)


def ADD1(n, a1):  # ADD #N, A1
    global memory
    s = n + memory[a1]
    if s > 255:
        s -= 256
    memory[a1] = s


def ADD2(a1, a2):  # ADD A1,A2
    global memory
    s = memory[a1] + memory[a2]
    if s > 255:
        s -= 256
    memory[a2] = s


def SUB(args):
    n, p1, a1, p2, a2 = cleanArgs(args)
    if n is not None:
        SUB1(n, a1)
    else:
        SUB2(a1, a2)


def SUB1(n, a1):
    global memory
    d = memory[a1] - n
    if d < 0:
        d = 0
    memory[a1] = d


def SUB2(a1, a2):
    global memory
    d = memory[a2] - memory[a1]
    if d < 0:
        d = 0
    memory[a2] = d


def AND(args):
    n, p1, a1, p2, a2 = cleanArgs(args)
    if n is not None:
        AND1(n, a1)
    else:
        AND2(a1, a2)


def AND1(n, a1):
    global memory
    memory[a1] = n and memory[a1]


def AND2(a1, a2):
    global memory
    memory[a2] = memory[a1] and memory[a2]


def OR(args):
    n, p1, a1, p2, a2 = cleanArgs(args)
    if n is not None:
        OR1(n, a1)
    else:
        OR2(a1, a2)


def OR1(n, a1):
    global memory
    memory[a1] = n or memory[a1]


def OR2(a1, a2):
    global memory
    memory[a2] = memory[a1] or memory[a2]


def XOR(args):
    n, p1, a1, p2, a2 = cleanArgs(args)
    if n is not None:
        XOR1(n, a1)
    else:
        XOR2(a1, a2)


def XOR1(n, a1):
    global memory
    notN = 0
    notA1 = 0
    if (n == 0):
        notN = 1
    if a1 == 0:
        notA1 = 1

    memory[a1] = ((n and notA1) or (notN and a1))


def XOR2(a1, a2):
    global memory
    notA1 = 0
    notA2 = 0
    if (a1 == 0):
        notA1 = 1
    if a2 == 0:
        notA2 = 1

    memory[a2] = ((a1 and notA2) or (notA1 and a2))


def COMP(args):
    n, p1, a1, p2, a2 = cleanArgs(args)
    if n is not None:
        COMP1(n, a1)
    else:
        COMP2(a1, a2)


def COMP1(n, a1):
    global temp
    a1 = memory[a1]
    if n < a1:
        temp = -1
    if n > a1:
        temp = 1


def COMP2(a1, a2):
    global temp
    a1 = memory[a1]
    a2 = memory[a2]
    if a1 < a2:
        temp = -1
    if a1 > a2:
        temp = 1


def BEQ(label):
    global pc, temp
    if temp == 0:
        pc = labels[label]


def BNE(label):
    global pc
    if temp != 0:
        pc = labels[label]


def BGT(label):
    global pc
    if temp > 0:
        pc = labels[label]


def BLT(label):
    global pc
    if temp < 0:
        pc = labels[label]


def BGE(label):
    global pc
    if temp >= 0:
        pc = labels[label]


def BLE(label):
    global pc
    if temp <= 0:
        pc = labels[label]

commandLookUp = {}
commandLookUp['PRINT'] = PRINT
commandLookUp['MOVE'] = MOVE
commandLookUp['ADD'] = ADD
commandLookUp['SUB'] = SUB
commandLookUp['AND'] = AND
commandLookUp['OR'] = OR
commandLookUp['XOR'] = XOR
commandLookUp['COMP'] = COMP
commandLookUp['BEQ'] = BEQ
commandLookUp['BNE'] = BNE
commandLookUp['BGT'] = BGT
commandLookUp['BLT'] = BLT
commandLookUp['BGE'] = BGE
commandLookUp['BLE'] = BLE
commandLookUp['END'] = END


def main():
    global size, memory, temp, pc, labels, program
    size = int('0x'+input(), 16)
    memory = [0 for i in range(size+1)]
    line = ''
    while line != 'END 0':
        try:
            line = input()
        except:
            line = 'END 0'
        if line == '':
            line = 'END 0'
        program.append(line)

    for i, line in enumerate(program):
        ll = line.split(' ', 1)
        if ll[0] not in keywords:
            labels[ll[0]] = i-1
            ll = ll[1].split(' ', 1)
        program[i] = [ll[0], ll[1].strip()]

    #print(program)

    command, args = program[pc]
    while command != 'END':
        run = commandLookUp[command]
        run(args)
        pc += 1
        command, args = program[pc]

if __name__ == '__main__':
    main()
