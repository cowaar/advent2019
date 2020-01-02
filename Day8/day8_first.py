import re

input = open("input.txt").read()

sifInput = str(input)


def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))



chunkedInput = list(chunkstring(sifInput, 150))

count = len(re.findall("0", chunkedInput[0]))


def countNumber(string,search):
    return len(re.findall(str(search), string))


zerosCount = [countNumber(string,0) for string in chunkedInput]

index = zerosCount.index(min(zerosCount))

ones = countNumber(chunkedInput[index],1)
twos = countNumber(chunkedInput[index],2)

print(ones*twos)