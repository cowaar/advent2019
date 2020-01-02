from intcode import Intcode
import itertools

array = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

listOfPhaseSettings = (list(itertools.permutations(range(5,10), 5)))
print(listOfPhaseSettings)

def runAmplifierSeries(phaseSettings):
    i = 0
    userInput = 0
    while i < 5:
        print(userInput)
        userInput = Intcode(array, userInput, phaseSettings[i])

        i += 1
    return userInput


result = [(runAmplifierSeries(settings), settings) for settings in listOfPhaseSettings]

print(max(result))
