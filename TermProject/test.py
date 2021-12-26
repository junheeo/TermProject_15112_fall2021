import random
primeL = [5,7,11,13,17,19,23,27,29,31,37,41]

primeChoiceInx1, primeChoiceInx2 = 0, 0
while (primeChoiceInx1 == primeChoiceInx2):
    primeChoiceInx1 = random.randint(0, len(primeL) - 1)
    primeChoiceInx2 = random.randint(0, len(primeL) - 1)

prime1 = primeL[primeChoiceInx1]
prime2 = primeL[primeChoiceInx2]









'''
# Here is an example that saves and loads data from a file.
# It works well with builtin data types. It's a bit more complicated
# to do this with custom classes.  For those, you have to be sure
# that your __repr__ method returns a string such that
# (eval(v.__repr__()) == v) is True.

import ast
import os

# def findPathToTermProjectFolder(path = '', filename = ''):
#     if (not os.path.isfile(path)) and filename == 'TermProject' :
#         isFoundThisCode = False
#         for file in os.listdir(path):
#             if file == 'test.py':
#                 ifFoundThisCode = True
#         if isFoundThisCode == True:
#             return path
#     else:
#         for filename in os.listdir(path):
#             checkPath = path + '/' + filename
#             if not os.path.isfile(checkPath):
#                 print(f"searching... {checkPath}")
#                 returnPath = findPathToTermProjectFolder(checkPath, filename)
#                 if returnPath != None:
#                     return returnPath
#     return None
#
# for filename in os.listdir('/'):
#     checkPath = '/'+filename
#     findPathToTermProjectFolder(checkPath, filename)

# source : https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(fileName):
    with open(fileName, "rt") as f:
        return f.read()

# source : https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def writeFile(fileName, contents):
    with open(fileName, "wt") as f:
        f.write(contents)

# Place all your data in a dictionary, like so:
# myData = {
#     'names': ['fred', 'wilma', 'betty'],
#     'highScores': [32, 41, 18, 17, 64],
#     'stateCapitals': { 'pa':'harrisburg', 'oh':'columbus' },
#     'setOfPrimes': { 2, 3, 5, 7, 11 },
# }
myData = 'abcdefgABCDEFG12345 \t\n!@#$%'

# Then, you can save your data to a file like so:
#writeFile('myData.txt', repr(myData))
writeFile('myData.txt', myData)

readVal = readFile('myData.txt')

#print(f'readVal = {repr(readVal)}')

print(f'readFile(README.txt) = {repr(readFile("README.txt"))}')

# # Later on, you can restore your data from the file like so:
# myData1 = ast.literal_eval(readFile('myData.txt'))

# # Finally, let's confirm that these two dictionaries are equal:
# print(myData1 == myData) # True!
'''