def convertToList(num):
    res = [int(x) for x in str(num)]
    return res




def checkLengthIsSix(list):
    if len(list) == 6:
        return True
    else:
        return False


def checkRepeatingUnits(list):
    containsDouble = False
    i = 0
    while i < len(list)-1:
        if list[i] == list[i+1]:
            containsDouble = True

        i += 1
    return containsDouble

def checkDecreases(list):
    containsDecrease = False
    i = 0
    while i < len(list)-1:
        if list[i] > list[i+1]:
            containsDecrease = True

        i += 1
    return containsDecrease

def testAllRules(number):
    list = convertToList(number)
    lengthSix = checkLengthIsSix(list)
    repeatingUnits = checkRepeatingUnits(list)
    decreases = checkDecreases(list)

    if lengthSix and repeatingUnits and decreases == False:
        return True
    else:
        return False

def checkRange(start,end):
    possiblePWs = 0
    i = start
    while i <= end:
        print(i)
        if testAllRules(i) ==True:
            possiblePWs += 1
        i += 1

    return possiblePWs

print(checkRange(372037,905157))
