def convertToList(num):
    res = [int(x) for x in str(num)]
    return res


def checkLengthIsSix(list):
    if len(list) == 6:
        return True
    else:
        return False


def checkContainsValidRepeatingUnits(list):
    i = 0
    containsValidUnits = False

    while i <= len(list) - 2:

        if list[i] == list[i + 1]:

            if checkOnlyDouble(list, i, i+1):
                containsValidUnits = True

        i += 1
    return containsValidUnits

def checkOnlyDouble(list,pos1,pos2):
    if pos1 == 0:
        if list[pos1] == list[pos2 + 1]:
            return False
        else:
            return True
    if pos2 == len(list)-1:
        if list[pos1-1] == list[pos1]:
            return False
        else:
            return True
    else:
        if list[pos1-1] != list[pos1] and list[pos1] != list[pos2 + 1]:
            return False


def checkDecreases(list):
    containsDecrease = False
    i = 0
    while i < len(list) - 1:
        if list[i] > list[i + 1]:
            containsDecrease = True

        i += 1
    return containsDecrease


def testAllRules(number):
    list = convertToList(number)
    lengthSix = checkLengthIsSix(list)
    repeatingUnits = checkContainsValidRepeatingUnits(list)

    decreases = checkDecreases(list)

    if lengthSix and repeatingUnits and decreases == False:
        return True
    else:
        return False


def checkRange(start, end):
    possiblePWs = 0
    i = start
    while i <= end:

        if testAllRules(i) == True:
            possiblePWs += 1
        print(testAllRules(i), i)
        i += 1

    return possiblePWs


print(testAllRules(111122))
print(testAllRules(112255))
print(testAllRules(111233))
print(testAllRules(112222))
print(testAllRules(111122))

# print(checkRange(372037,905157))
