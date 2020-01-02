def posOrImm(immSignal, inputArray, position):
    if immSignal == "1":
        return position
    if immSignal == "0":
        return inputArray[position]


def getPositionsFromMode(inputArray, p, immSignal):
    pos1 = posOrImm(immSignal[2], inputArray, p + 1)
    pos2 = posOrImm(immSignal[1], inputArray, p + 2)
    pos3 = posOrImm(immSignal[0], inputArray, p + 3)
    return (pos1, pos2, pos3)


def opcode1(inputArray, p, immSignal):
    pos1, pos2, pos3 = getPositionsFromMode(inputArray, p, immSignal)

    inputArray[pos3] = inputArray[pos1] + inputArray[pos2]
    return inputArray


def opcode2(inputArray, p, immSignal):
    pos1, pos2, pos3 = getPositionsFromMode(inputArray, p, immSignal)

    inputArray[pos3] = inputArray[pos1] * inputArray[pos2]
    return inputArray


def opcode3(inputArray, p, immSignal, userInput):
    pos1 = posOrImm(immSignal[2], inputArray, p + 1)

    inputArray[pos1] = int(userInput)
    return inputArray


def opcode4(inputArray, p, immSignal):
    pos1 = posOrImm(immSignal[2], inputArray, p + 1)

    output = inputArray[pos1]
    return inputArray, output


def opcode5(inputArray, p, immSignal):
    pos1, pos2, pos3 = getPositionsFromMode(inputArray, p, immSignal)

    if inputArray[pos1] != 0:
        p = inputArray[pos2]
    else:
        p = p + 3
    return inputArray, p


def opcode6(inputArray, p, immSignal):
    pos1, pos2, pos3 = getPositionsFromMode(inputArray, p, immSignal)
    if inputArray[pos1] == 0:
        p = inputArray[pos2]
    else:
        p = p + 3
    return inputArray, p


def opcode7(inputArray, p, immSignal):
    pos1, pos2, pos3 = getPositionsFromMode(inputArray, p, immSignal)
    if inputArray[pos1] < inputArray[pos2]:
        inputArray[pos3] = 1
    else:
        inputArray[pos3] = 0
    return inputArray


def opcode8(inputArray, p, immSignal):
    pos1, pos2, pos3 = getPositionsFromMode(inputArray, p, immSignal)
    if inputArray[pos1] == inputArray[pos2]:
        inputArray[pos3] = 1
    else:
        inputArray[pos3] = 0
    return inputArray


def Intcode(Array, userInput, phaseSetting):
    i = 0
    opcode3count = 0
    while i < len(Array):

        opcode = str(format(Array[i], "05"))[3:]

        immSignal = format(Array[i], "05")[:3]
        if opcode == "01":
            Array = opcode1(Array, i, immSignal)
            i += 4
        if opcode == "02":
            Array = opcode2(Array, i, immSignal)
            i += 4
        if opcode == "03":
            if opcode3count == 0:
                Array = opcode3(Array, i, immSignal, phaseSetting)
            if opcode3count == 1:
                Array = opcode3(Array, i, immSignal, userInput)
            opcode3count += 1
            i += 2
        if opcode == "04":
            Array,output = opcode4(Array, i, immSignal)
            i += 2
        if opcode == "05":
            Array, i = opcode5(Array, i, immSignal)
        if opcode == "06":
            Array, i = opcode6(Array, i, immSignal)
        if opcode == "07":
            Array = opcode7(Array, i, immSignal)
            i += 4
        if opcode == "08":
            Array = opcode8(Array, i, immSignal)
            i += 4
        if opcode == "99":
            break
    return output



