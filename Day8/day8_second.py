import re
import numpy as np
import scipy.misc as smp
from PIL import Image
from matplotlib import pyplot as plt


input = open("input.txt").read()

sifInput = str(input)


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


chunkedInput = list(chunkstring(sifInput, 150))


def addAllLayers(chunkedInput):
    chunkLength = len(chunkedInput[0])

    chunkedInput.reverse()
    result = list("2" * chunkLength)

    i = 0
    while i < len(chunkedInput):
        print(i)

        result = addLayer(result, list(chunkedInput[i]))

        i += 1
    return result


def addLayer(oldChunk, newChunk):
    result = []
    for oldNumber, newNumber in zip(oldChunk, newChunk):
        result.append(numberRules(oldNumber,newNumber))

    return result


def numberRules(oldNumber, newNumber):
    if int(newNumber) == 2:
        return oldNumber
    else:
        return newNumber


allLayers = addAllLayers(chunkedInput)
print(allLayers)
newAllLayers = []
for item in allLayers:
    if item == '1':
        newAllLayers.append(1)
    if item == '0':
        newAllLayers.append(0)
#


displayData = list(chunkstring(newAllLayers,25))
print(list(displayData))

z = np.array([np.array(xi) for xi in displayData])
print(z)
print(type(z[0][0]))

img = Image.fromarray(z,"1")
img.show()