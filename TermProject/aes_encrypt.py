# Name : Jun Hee Oh
# ID : junheeo

import copy

#print(f'bin(32) = {bin(32)} has type {type(bin(32))}')

sBoxRow00 = {
    '0':'63', '1':'7c', '2':'77', '3':'7b', '4':'f2', 
    '5':'6b', '6':'6f', '7':'c5', '8':'30', '9':'01',
    'a':'67', 'b':'2b', 'c':'fe', 'd':'d7', 'e':'ab', 'f':'76'
}
sBoxRow10 = {
    '0':'ca', '1':'82', '2':'c9', '3':'7d', '4':'fa', 
    '5':'59', '6':'47', '7':'f0', '8':'ad', '9':'d4',
    'a':'a2', 'b':'af', 'c':'9c', 'd':'a4', 'e':'72', 'f':'c0'
}
sBoxRow20 = {
    '0':'b7', '1':'fd', '2':'93', '3':'26', '4':'36', 
    '5':'3f', '6':'f7', '7':'cc', '8':'34', '9':'a5',
    'a':'e5', 'b':'f1', 'c':'71', 'd':'d8', 'e':'31', 'f':'15'
}
sBoxRow30 = {
    '0':'04', '1':'c7', '2':'23', '3':'c3', '4':'18', 
    '5':'96', '6':'05', '7':'9a', '8':'07', '9':'12',
    'a':'80', 'b':'e2', 'c':'eb', 'd':'27', 'e':'b2', 'f':'75'
}
sBoxRow40 = {
    '0':'09', '1':'83', '2':'2c', '3':'1a', '4':'1b', 
    '5':'6e', '6':'5a', '7':'a0', '8':'52', '9':'3b',
    'a':'d6', 'b':'b3', 'c':'29', 'd':'e3', 'e':'2f', 'f':'84'
}
sBoxRow50 = {
    '0':'53', '1':'d1', '2':'00', '3':'ed', '4':'20', 
    '5':'fc', '6':'b1', '7':'5b', '8':'6a', '9':'cb', 
    'a':'be', 'b':'39', 'c':'4a', 'd':'4c', 'e':'58', 'f':'cf'
}
sBoxRow60 = {
    '0':'d0', '1':'ef', '2':'aa', '3':'fb', '4':'43', 
    '5':'4d', '6':'33', '7':'85', '8':'45', '9':'f9', 
    'a':'02', 'b':'7f', 'c':'50', 'd':'3c', 'e':'9f', 'f':'a8'
}
sBoxRow70 = {
    '0':'51', '1':'a3', '2':'40', '3':'8f', '4':'92', 
    '5':'9d', '6':'38', '7':'f5', '8':'bc', '9':'b6', 
    'a':'da', 'b':'21', 'c':'10', 'd':'ff', 'e':'f3', 'f':'d2'
}
sBoxRow80 = {
    '0':'cd', '1':'0c', '2':'13', '3':'ec', '4':'5f', 
    '5':'97', '6':'44', '7':'17', '8':'c4', '9':'a7', 
    'a':'7e', 'b':'3d', 'c':'64', 'd':'5d', 'e':'19', 'f':'73'
}
sBoxRow90 = {
    '0':'60', '1':'81', '2':'4f', '3':'dc', '4':'22', 
    '5':'2a', '6':'90', '7':'88', '8':'46', '9':'ee', 
    'a':'b8', 'b':'14', 'c':'de', 'd':'5e', 'e':'0b', 'f':'db'
}
sBoxRowA0 = {
    '0':'e0', '1':'32', '2':'3a', '3':'0a', '4':'49', 
    '5':'06', '6':'24', '7':'5c', '8':'c2', '9':'d3', 
    'a':'ac', 'b':'62', 'c':'91', 'd':'95', 'e':'e4', 'f':'79'
}
sBoxRowB0 = {
    '0':'e7', '1':'c8', '2':'37', '3':'6d', '4':'8d', 
    '5':'d5', '6':'4e', '7':'a9', '8':'6c', '9':'56',
    'a':'f4', 'b':'ea', 'c':'65', 'd':'7a', 'e':'ae', 'f':'08'
}
sBoxRowC0 = {
    '0':'ba', '1':'78', '2':'25', '3':'2e', '4':'1c', 
    '5':'a6', '6':'b4', '7':'c6', '8':'e8', '9':'dd',
    'a':'74', 'b':'1f', 'c':'4b', 'd':'bd', 'e':'8b', 'f':'8a'
}
sBoxRowD0 = {
    '0':'70', '1':'3e', '2':'b5', '3':'66', '4':'48', 
    '5':'03', '6':'f6', '7':'0e', '8':'61', '9':'35',
    'a':'57', 'b':'b9', 'c':'86', 'd':'c1', 'e':'1d', 'f':'9e'
}
sBoxRowE0 = {
    '0':'e1', '1':'f8', '2':'98', '3':'11', '4':'69', 
    '5':'d9', '6':'8e', '7':'94', '8':'9b', '9':'1e',
    'a':'87', 'b':'e9', 'c':'ce', 'd':'55', 'e':'28', 'f':'df'
}
sBoxRowF0 = {
                                                                
    '0':'8c', '1':'a1', '2':'89', '3':'0d', '4':'bf', 
    '5':'e6', '6':'42', '7':'68', '8':'41', '9':'99',
    'a':'2d', 'b':'0f', 'c':'b0', 'd':'54', 'e':'bb', 'f':'16'
}
sBox = {
    '0':sBoxRow00, '1':sBoxRow10, '2':sBoxRow20, '3':sBoxRow30, 
    '4':sBoxRow40, '5':sBoxRow50, '6':sBoxRow60, '7':sBoxRow70, 
    '8':sBoxRow80, '9':sBoxRow90, 'a':sBoxRowA0, 'b':sBoxRowB0, 
    'c':sBoxRowC0, 'd':sBoxRowD0, 'e':sBoxRowE0, 'f':sBoxRowF0
}

rcon0 = ['01','00','00','00']
rcon1 = ['02','00','00','00']
rcon2 = ['04','00','00','00']
rcon3 = ['08','00','00','00']
rcon4 = ['10','00','00','00']
rcon5 = ['20','00','00','00']
rcon6 = ['40','00','00','00']
rcon7 = ['80','00','00','00']
rcon8 = ['1b','00','00','00']
rcon9 = ['36','00','00','00']
rCon = [rcon0, rcon1, rcon2, rcon3, rcon4, rcon5, rcon6, rcon7, rcon8, rcon9]

# converts '0' => 0 (type int), '1' => 1 (type int), else => None
def stringBitToInt(val):
    if val == '0':
        return 0
    elif val == '1':
        return 1
    else:
        print(f"InputError: '{val}' is not a string of bit : stringBitToInt()")
        return None

# converts integer into string of binary e.g. 13 => '1101'
# the result is m digits e.g. m = 4, intVal=2 => return 0010
def intToStringBinary(intVal, m):
    max = 2 ** m - 1
    if not isinstance(intVal, int):
        print(f'InputError : intVal={intVal} is not an int'
                                                    +' : intToStringBinary()')
    elif not(0 <= intVal <= max):
        print(f'InputError: intVal = {intVal} out of range 0~2**{m}-1'
                                                    +' : intToStringBinary()')
    else:
        strBinary = bin(intVal)
        strBinary = strBinary[2:]
        return strBinary
    return None
        
# perfom addition of two integers in Galis Field 2^m
# returns binary string of m digits
def additionGF2m(int1, int2, m):

    strBinary1 = intToStringBinary(int1, m)
    strBinary2 = intToStringBinary(int2, m)
    if strBinary1 == None:
        print(f'InputError : int1 = {int1} is not valid input : additionGF2m()')
    if strBinary1 == None:
        print(f'InputError : int2 = {int2} is not valid input : additionGF2m()')

    else:   # there are no problems with input
        binarySum = ''
        strBin1Len = len(strBinary1)
        strBin2Len = len(strBinary2)
        if strBin1Len < m:
            strBinary1 = '0'*(m - strBin1Len) + strBinary1
        if strBin2Len < m:
            strBinary2 = '0'*(m - strBin2Len) + strBinary2
        strBinarySum = ''
        for i in range(m):
            bit1 = int(strBinary1[i])
            bit2 = int(strBinary2[i])
            bitSum = bit1 ^ bit2
            strBinarySum += str(bitSum)
        return strBinarySum
    # if there is error with input return None
    return None


# This is NOT the entire multiplication code for GF(2**m)
# executed only the polynomial multiplication of two strings of Binary of size m
# no modulo operation is executed
def polynomialMult(strBinary1, strBinary2, m):
    polyMultResult = "0"
    trailingZeros = ''
    strBin2Len = len(strBinary2)
    for strB2Inx in range(strBin2Len - 1, -1, -1):
        newDigit = '0'
        if strBinary2[strB2Inx] == '1':
            newDigit = strBinary1 + trailingZeros
        intVerNewDigit = int(newDigit, 2)
        intVerPolyMultResult = int(polyMultResult, 2)
        polyMultResult = additionGF2m(intVerPolyMultResult, intVerNewDigit, m*2)
        trailingZeros += '0'
    return polyMultResult

# Do: binarystring mod binary string
# doing polynomial modulo operation under GF(2^m)
# return the moduloed result binary string
def polynomialModulo(polyMultResult, strBinaryP, m):
    m = m * 2
    polyMultResult = bin(int(polyMultResult, 2))[2:]
    lenPolyMultResult = len(polyMultResult)
    #print(f'm = {m}')
    #print(f'lenPolyMultResult = {lenPolyMultResult}')
    if lenPolyMultResult < m:
        polyMultResult = '0'*(m - lenPolyMultResult) + polyMultResult
    lenPolyMultResult = len(polyMultResult)
    lenStrBinP = len(strBinaryP)
    if lenStrBinP > lenPolyMultResult:
        return polyMultResult
    #print(f'{polyMultResult} mod {strBinaryP}')
    for inx in range(lenPolyMultResult - lenStrBinP + 1):
        #print(f'\tinx = {inx}')
        #print(f'\tpolyMultResult[inx] = {polyMultResult[inx]}')
        if polyMultResult[inx] == '1':
            alter = additionGF2m(int(polyMultResult[:lenStrBinP + inx], 2)
                                                        , int(strBinaryP, 2)
                                                            , lenStrBinP)
            rest = polyMultResult[lenStrBinP + inx:]
            polyMultResult = alter + rest
            lenPolyMultResult = len(polyMultResult)
            if lenPolyMultResult < m:
                polyMultResult = '0'*(m - lenPolyMultResult) + polyMultResult
        #print(f'\t=> polyMultResult = {polyMultResult}')
    polyMultResult = bin(int(polyMultResult, 2))[2:]
    return polyMultResult

# performs multiplication of two integers in Galois Field of 2^m with
# p an integer representing the irreducible polynomial
# returns binary string of m digits
def multiplicationGF2m(int1, int2, p, m):
    noInputError = True
    if not isinstance(p, int):
        print(f'InputError : p = {p} should be an int : multiplicationGF2m()')
        noInputError = False
    strBinaryP = bin(p)[2:]
    if not isinstance(m, int):
        print(f'InputError : m = {m} should be an int : multiplicationGF2m()')
        noInputError = False
    
    strBinary1 = None
    if intToStringBinary(int1, m) != None:
        strBinary1 = bin(int1)[2:]  # does not have leading zeros
    strBinary2 = intToStringBinary(int2, m)
    if strBinary1 == None:
        print(f'InputError : int1 = {int1} is not valid input '
                                                    +': multiplicationGF2m()')
        noInputError = False
    if strBinary2 == None:
        print(f'InputError : int2 = {int2} is not valid input '
                                                    +': multiplicationGF2m()')
        noInputError = False

    if noInputError:       
        polyMultResult = polynomialMult(strBinary1, strBinary2, m)
        polyMultModuloResult = polynomialModulo(polyMultResult, strBinaryP, m)
        return polyMultModuloResult
    else:
        return None

# addition of two hex values in GF(2^m)
# return hex value
# input and output hex vals do NOT include "0x"
def hexAdd(hexVal1, hexVal2, m):
    int1 = int(hexVal1, 16)
    int2 = int(hexVal2, 16)
    return hex(int(additionGF2m(int1, int2, m), 2))[2:]

# multiplication of two hex values in GF(2^m) with mod p (p is INT)
# return hex value
# input and output hex vals do NOT include "0x"
def hexMult(hexVal1, hexVal2, p, m):
    int1 = int(hexVal1, 16)
    int2 = int(hexVal2, 16)
    return hex(int(multiplicationGF2m(int1, int2, p, m), 2))[2:]

# matrix multiplication between matrix and column vector
# return column vector
# all values except p, m are in hex without '0x'
def matXColvecGF2m(mat, vec, p, m):
    matNumRow = len(mat)
    matNumCol = len(mat[0])
    if len(vec) != matNumCol:
        print('InputError : maxtrix and vector dimensions do not match '
                                                        +': matXColvecGF2m()')
    resultColVec = []
    for row in mat:
        rowXCol = '0'
        for inx in range(matNumCol):
            rowXCol = hexAdd(rowXCol, hexMult(row[inx], vec[inx], p, m), 2 * m)
            if len(rowXCol) == 1:
                rowXCol = '0' + rowXCol
            #print(f'rowXCol = {rowXCol}')
        resultColVec.append(rowXCol)
    #print(f'resultColVec = {resultColVec}')
    return resultColVec

# hex = 16 bits (0~F)
# two digit hex = 16 * 16 digits
#
# mixCol Layer implementation
#
# input : list of 4 hex values each with 2 digits
# output : list of 4 hex values each with 2 digits
#
# input and output hex vals do NOT include "0x"
#
#  | 02 03 01 01 |   | B0 |   | C0 |
#  | 01 02 03 03 | * | B5 | = | C1 |
#  | 01 01 02 03 |   | B10|   | C2 |
#  | 03 01 01 01 |   | B15|   | C3 |
def aesMixCol(hexVectorL):
    noInputError = True
    if len(hexVectorL) != 4:
        print(f'InputError : hexVectorL = {hexVectorL} is incorrect vector '
                                                    +'input size : aesMixCol()')
        notInputError = False
    for inputVecVal in hexVectorL:
        if not isinstance(inputVecVal, str):
            print(f'InputError : hexVectorL = {hexVectorL} should represent '
                                            +' hex with string : aesMixCol()')
            notInputError = False
        else:
            if not inputVecVal.isalnum():
                notInputError = False
                print(f'InputError : hexVectorL = {hexVectorL} should '
                                                +'represent hex : aesMixCol()')
            else:
                if inputVecVal[:2] == '0x' or inputVecVal[:2] == '0X':
                    notInputError = False
                    print(f'InputError : hexVectorL = {hexVectorL} should '
                            +'represent hex without 0x infront : aesMixCol()')
                    if len(inputVecVal) > 2:
                        notInputError = False
                        print(f'InputError : hexVectorL = {hexVectorL} should '
                                +'represent 2 digit hex : aesMixCol()')
                        print('2**8 = 2**4 * 2**4 = 16 * 16 = 0xFF')
    if noInputError:
        mat0 = [
        ['02', '03', '01', '01'],
        ['01', '02', '03', '01'],
        ['01', '01', '02', '03'],
        ['03', '01', '01', '02']
        ]
        return matXColvecGF2m(mat0, hexVectorL, 283, 8)

# check if a matrix is a 4x4 2D list with hex strings without 0x prefix
# returns true if satisfy
# returns false otherwise

def checkHexMatrix4x4(matrix, functionName='undefined'):
    noInputError = True
    if not isinstance(matrix, list):
        print(f'InputError : {matrix} is not a 2D List : {functionName}')
        noInputError = False
        return noInputError
    else:
        if isinstance(matrix[0], list):
            if len(matrix) != 4 or len(matrix) != 4:
                print(f'InputError : {matrix} should be 4x4 matrix :'
                                                        +f' {functionName}')
        possibleHexDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                                                'a', 'b', 'c', 'd', 'e', 'f']
        possibleHexStrings = set()                  # set of possible 2Digit hex
        for hexDigit1 in possibleHexDigits:
            for hexDigit2 in possibleHexDigits:
                possibleHexStrings.add(hexDigit1 + hexDigit2)
        for rowInx in range(len(matrix)):           # checking Matrix is 2D
            if not isinstance(matrix[rowInx], list):
                print(f'InputError : {matrix} is not a 2D List : '
                                                            +'{functionName}')
                noInputError = False
                return noInputError
            else:
                for colInx in range(len(matrix)):   # checking vals in Matrix
                    checkingVal = matrix[rowInx][colInx]
                    if not isinstance(checkingVal, str):
                        print(f'InputError : {matrix} should have strings of '
                                                        +'hex : {functionName}')
                        noInputError = False
                    else:
                        if checkingVal[:2] == '0x':
                            print(f'InputError : {matrix} hex strings do not '
                                                +'include 0x : {functionName}')
                            noInputError = False
                        if checkingVal not in possibleHexStrings:
                            print(f'InputError : {matrix} strings to not '
                                +f'represent two digit hex : {functionName}')
                            noInputError = False
    return noInputError


# input : 4x4 2D list of 2 digit hex strings
# output : 4x4 2D list of 2 digit hex strings
# hex strings do not include 0x prefix

# sBox dictinary should be predefined as global variable

# convert values into corresponding s-box values

def aesByteSub(matrix):
    noInputError = checkHexMatrix4x4(matrix, 'aesByteSub()')
    if noInputError:
        resultMat = copy.deepcopy(matrix)
        for rowInx in range(len(resultMat)):
            for colInx in range(len(resultMat)):
                prevVal = resultMat[rowInx][colInx]
                resultMat[rowInx][colInx] = sBox[prevVal[0]][prevVal[1]]
        return resultMat
    else:
        return None

# input a 4x4 matrix with hex strings without 0x prefix
# output a 4x4 matrix with hex strings without 0x prefix

def aesShiftRows(matrix):
    noInputError = checkHexMatrix4x4(matrix, 'aesShiftRows()')
    if noInputError:
        resultMat = copy.deepcopy(matrix)
        for rowInx in range(len(matrix)):
            numOfShifts = rowInx
            for shift in range(numOfShifts):
                shiftVal = resultMat[rowInx].pop(0)
                resultMat[rowInx].append(shiftVal)
        return resultMat
    else:
        return None

# input two 4x4 matrix with hex strings without 0x prefix
# each represent matrix and roundKey
# output a 4x4 matrix with hex strings without 0x prefix

def aesKeyAdd(matrix, roundKey):
    noInputError1 = checkHexMatrix4x4(matrix, 'aesKeyAdd()')
    if noInputError1 == False:
        print('InputError is from matrix : aesKeyAdd()')
    noInputError2 = checkHexMatrix4x4(roundKey, 'aesKeyAdd()')
    if noInputError2 == False:
        print('InputError is from roundKey : aesKeyAdd()')
    if noInputError1 and noInputError2:
        returnMat = copy.deepcopy(matrix)
        for rowInx in range(4):
            for colInx in range(4):
                hexVal1 = matrix[rowInx][colInx]
                hexVal2 = roundKey[rowInx][colInx]
                resultVal = hexAdd(hexVal1, hexVal2, 8)
                if len(resultVal) == 1:
                    resultVal = '0' + resultVal
                returnMat[rowInx][colInx] = resultVal
        return returnMat
    else:
        return None

# turns column of a matrix into a 1D list
# input : 2D list
# output : 1D list
def colTo1DList(matrix, colInx):
    returnL = []
    for row in matrix:
        returnL.append(row[colInx])
    return returnL

# input :
#       lastKey : 4x4 2D list with 2digit hex strings without 0x header
#               represent roundKey right before
#       roundRCon : 4x4 2D list with 2digit hex strings without 0x header
#               represent the current Rcon being used
# output: 4x4 2D list with 2digit hex strings without 0x header
#       represent new (current round's) roundKey
# create 1 round of key extension
def createKey1Round(lastKey, roundRCon):
    newKey = [[],[],[],[]]
    firstCol = colTo1DList(lastKey, 0)
    rotWord = colTo1DList(lastKey, 3)
    rotWord.append(rotWord.pop(0))
    for rotWordInx in range(len(rotWord)):
        origHex = rotWord[rotWordInx]
        rotWord[rotWordInx] = sBox[origHex[0]][origHex[1]]
    for rowInx in range(4):
        hexVal1 = firstCol[rowInx]
        hexVal2 = rotWord[rowInx]
        hexVal3 = roundRCon[rowInx]
        resultVal = hexAdd(hexAdd(hexVal1, hexVal2, 8), hexVal3, 8)
        if len(resultVal) == 1:
            resultVal = '0' + resultVal
        newKey[rowInx].append(resultVal)
    for round in range(1,4):
        col1 = colTo1DList(lastKey, round)
        col2 = colTo1DList(newKey, round - 1)
        for rowInx in range(4):
            hexVal1 = col1[rowInx]
            hexVal2 = col2[rowInx]
            resultVal = hexAdd(hexVal1, hexVal2, 8)
            if len(resultVal) == 1:
                resultVal = '0' + resultVal
            newKey[rowInx].append(resultVal)
    return newKey

# create list of all rounds of keys based on cipher key and store all in a list
# return 3D list : 1D list containing 2D lists of cipherKey and roundKeys
def aesKeyExpansion(cipherKey):
    noInputError = checkHexMatrix4x4(cipherKey, 'aesKeyExpansion()')
    if noInputError == False:
        print('InputError is on cipherKey : aesKeyExpansion()')
        return None
    else:
        keysL = []
        keysL.append(cipherKey)
        for round in range(10):
            keysL.append(createKey1Round(keysL[-1], rCon[round]))
        return keysL

# input : 
#       state : 4x4 2D list with 2digit hex strings without 0x header
#       cipherKey : 4x4 2D list with 2digit hex strings without 0x header
# output : 4x4 2D list with 2digit hex strings without 0x header
#
# encrypts state with cipherKey and returns encrypted result

def aesEncryption(state, cipherKey):
    keys = aesKeyExpansion(cipherKey)
    state = aesKeyAdd(state, keys[0])
    for mainRound in range(1,10):
        state = aesByteSub(state)
        state = aesShiftRows(state)
        newState = [[],[],[],[]]
        for colInx in range(4):
            colVector = colTo1DList(state, colInx)
            mixedColVec = aesMixCol(colVector)
            for rowInx in range(4):
                newState[rowInx].append(mixedColVec[rowInx])
        state = newState
        state = aesKeyAdd(state, keys[mainRound])
    state = aesByteSub(state)
    state = aesShiftRows(state)
    state = aesKeyAdd(state, keys[10])
    return state



def testGF2mArithmetic():
    print(f'\ntesting arithmetic in GF...')
    assert(stringBitToInt('0') == 0)
    assert(stringBitToInt('1')== 1)
    #assert(stringBitToInt('2')==None)
    assert(additionGF2m(0,0,8) == '00000000')
    assert(additionGF2m(3,4,8) == '00000111')
    assert(additionGF2m(3,3,8) == '00000000')

    assert(hex(int(additionGF2m(int('04', 16),int('a0', 16),8),2)) == '0xa4')
    assert(hex(int(additionGF2m(int('66', 16),int('fa', 16),8),2)) == '0x9c')
    assert(hex(int(additionGF2m(int('81', 16),int('fe', 16),8),2)) == '0x7f')
    assert(hex(int(additionGF2m(int('e5', 16),int('17', 16),8),2)) == '0xf2')
    assert(hexAdd('04', 'a0', 8) == 'a4')

    val1 = int(additionGF2m(43,138,8), 2)
    assert(int(additionGF2m(val1,1,8), 2) == 160)
    assert(int('000', 2) == 0)  # int('binary string', 2) => int version of bin
    assert(int('1', 2) == 1)
    assert(int('001', 2) == 1)
    assert(int('111', 2) == 7)
    assert(int(additionGF2m(3,4,8), 2) == 7)
    assert(multiplicationGF2m(7, 5, 11, 3) == '110')

    v00 = multiplicationGF2m(212, 2, 283, 8)
    v00 = int(v00, 2)
    v01 = multiplicationGF2m(191, 3, 283, 8)
    v01 = int(v01, 2)
    v02 = multiplicationGF2m(93, 1, 283, 8)
    v02 = int(v02, 2)
    v03 = multiplicationGF2m(48, 1, 283, 8)
    v03 = int(v03, 2)

    v0 = '0'
    v0 = additionGF2m(int(v0, 2), v00, 8)
    v0 = additionGF2m(int(v0, 2), v01, 8)
    v0 = additionGF2m(int(v0, 2), v02, 8)
    v0 = additionGF2m(int(v0, 2), v03, 8)

    assert(hex(int(v0,2)) == '0x4')
    assert(v0 == '00000100')

    v10 = multiplicationGF2m(212, 1, 283, 8)
    v10 = int(v10, 2)
    v11 = multiplicationGF2m(191, 2, 283, 8)
    v11 = int(v11, 2)
    v12 = multiplicationGF2m(93, 3, 283, 8)
    v12 = int(v12, 2)
    v13 = multiplicationGF2m(48, 1, 283, 8)
    v13 = int(v13, 2)

    v1 = '0'
    v1 = additionGF2m(int(v1, 2), v10, 8)
    v1 = additionGF2m(int(v1, 2), v11, 8)
    v1 = additionGF2m(int(v1, 2), v12, 8)
    v1 = additionGF2m(int(v1, 2), v13, 8)

    assert(hex(int(v1, 2)) == '0x66')

    v20 = multiplicationGF2m(212, 1, 283, 8)
    v20 = int(v20, 2)
    v21 = multiplicationGF2m(191, 1, 283, 8)
    v21 = int(v21, 2)
    v22 = multiplicationGF2m(93, 2, 283, 8)
    v22 = int(v22, 2)
    v23 = multiplicationGF2m(48, 3, 283, 8)
    v23 = int(v23, 2)

    v2 = '0'
    v2 = additionGF2m(int(v2, 2), v20, 8)
    v2 = additionGF2m(int(v2, 2), v21, 8)
    v2 = additionGF2m(int(v2, 2), v22, 8)
    v2 = additionGF2m(int(v2, 2), v23, 8)

    assert(hex(int(v2, 2)) == '0x81')

    v30 = multiplicationGF2m(212, 3, 283, 8)
    v30 = int(v30, 2)
    v31 = multiplicationGF2m(191, 1, 283, 8)
    v31 = int(v31, 2)
    v32 = multiplicationGF2m(93, 1, 283, 8)
    v32 = int(v32, 2)
    v33 = multiplicationGF2m(48, 2, 283, 8)
    v33 = int(v33, 2)

    v3 = '0'
    v3 = additionGF2m(int(v3, 2), v30, 8)
    v3 = additionGF2m(int(v3, 2), v31, 8)
    v3 = additionGF2m(int(v3, 2), v32, 8)
    v3 = additionGF2m(int(v3, 2), v33, 8)

    assert(hex(int(v3, 2)) == '0xe5')

    assert(hexMult('d4', '3', 283, 8) == hex(v30)[2:])
    print('...passed!')


def testAESEncryption():
    print('testing AES encryption...')
    mat0 = [
        ['02', '03', '01', '01'],
        ['01', '02', '03', '01'],
        ['01', '01', '02', '03'],
        ['03', '01', '01', '02']
    ]
    vec0 = ['d4', 'bf', '5d', '30']
    result0 = ['04','66','81','e5']
    assert(matXColvecGF2m(mat0, vec0, 283, 8) == result0)

    mat1 = [
        ['0e', '0b', '0d', '09'],
        ['09', '0e', '0b', '0d'],
        ['0d', '09', '0e', '0b'],
        ['0b', '0d', '09', '0e']
    ]
    assert(matXColvecGF2m(mat1, result0, 283, 8) == vec0)
    # mat1 is the left inverse of mat0
    assert(matXColvecGF2m(mat1, matXColvecGF2m(mat0, vec0, 283, 8)
                                                            , 283, 8) == vec0)
    # mat1 is the right inverse of mat0
    assert(matXColvecGF2m(mat0, matXColvecGF2m(mat1, result0, 283, 8)
                                                        , 283, 8) == result0)
    assert(aesMixCol(vec0) == matXColvecGF2m(mat0, vec0, 283, 8))

    subMat0 = [
        ['19','a0','9a','e9'],
        ['3d','f4','c6','f8'],
        ['e3','e2','8d','48'],
        ['be','2b','2a','08']
    ]
    subMat0Res = [
        ['d4','e0','b8','1e'],
        ['27','bf','b4','41'],
        ['11','98','5d','52'],
        ['ae','f1','e5','30'],
    ]
    #print(f'aesByteSub(subMat0) = {aesByteSub(subMat0)}')
    result = aesByteSub(subMat0)
    for i in range(len(subMat0)):
        for j in range(len(subMat0[0])):
            if result[i][j] != subMat0Res[i][j]:
                print(f'{result[i][j]} != {subMat0Res[i][j]} at {i,j}')
    assert(aesByteSub(subMat0) == subMat0Res)

    subMat1 = [
        ['a4','68','6b','02'],
        ['9c','9f','5b','6a'],
        ['7f','35','ea','50'],
        ['f2','2b','43','49']
    ]
    subMat1Res = [
        ['49','45','7f','77'],
        ['de','db','39','02'],
        ['d2','96','87','53'],
        ['89','f1','1a','3b']
    ]
    assert(aesByteSub(subMat1) == subMat1Res)
    subMat2 = [
        ['aa','61','82','68'],
        ['8f','dd','d2','32'],
        ['5f','e3','4a','46'],
        ['03','ef','d2','9a']
    ]
    subMat2Res = [
        ['ac','ef','13','45'],
        ['73','c1','b5','23'],
        ['cf','11','d6','5a'],
        ['7b','df','b5','b8']
    ]
    assert(aesByteSub(subMat2) == subMat2Res)
    shiftRowsMat0Res = [
        ['d4','e0','b8','1e'],
        ['bf','b4','41','27'],
        ['5d','52','11','98'],
        ['30','ae','f1','e5']
    ]
    assert(aesShiftRows(aesByteSub(subMat0)) == shiftRowsMat0Res)

    addRoundKeyMat0 = [
        ['04','e0','48','28'],
        ['66','cb','f8','06'],
        ['81','19','d3','26'],
        ['e5','9a','7a','4c']
    ]
    addRoundKeyKey0 = [
        ['a0','88','23','2a'],
        ['fa','54','a3','6c'],
        ['fe','2c','39','76'],
        ['17','b1','39','05']
    ]
    addRoundKeyMat0Res = [
        ['a4','68','6b','02'],
        ['9c','9f','5b','6a'],
        ['7f','35','ea','50'],
        ['f2','2b','43','49']
    ]
    assert(aesKeyAdd(addRoundKeyMat0, addRoundKeyKey0) == addRoundKeyMat0Res)

    lastKey0 = [
        ['2b','28','ab','09'],
        ['7e','ae','f7','cf'],
        ['15','d2','15','4f'],
        ['16','a6','88','3c']
    ]
    lastKey0Result = [
        ['a0','88','23','2a'],
        ['fa','54','a3','6c'],
        ['fe','2c','39','76'],
        ['17','b1','39','05']
    ]
    assert(createKey1Round(lastKey0, rCon[0]) == lastKey0Result)

    cipherKey = [
        ['2b','28','ab','09'],
        ['7e','ae','f7','cf'],
        ['15','d2','15','4f'],
        ['16','a6','88','3c']
    ]
    roundKey1 = [
        ['a0','88','23','2a'],
        ['fa','54','a3','6c'],
        ['fe','2c','39','76'],
        ['17','b1','39','05']
    ]
    roundKey2 = [
        ['f2','7a','59','73'],
        ['c2','96','35','59'],
        ['95','b9','80','f6'],
        ['f2','43','7a','7f']
    ]
    roundKey10 = [
        ['d0','c9','e1','b6'],
        ['14','ee','3f','63'],
        ['f9','25','0c','0c'],
        ['a8','89','c8','a6']
    ]
    assert(aesKeyExpansion(cipherKey)[1] == roundKey1)
    assert(aesKeyExpansion(cipherKey)[2] == roundKey2)
    assert(aesKeyExpansion(cipherKey)[10] == roundKey10)

    state = [
        ['32','88','31','e0'],
        ['43','5a','31','37'],
        ['f6','30','98','07'],
        ['a8','8d','a2','34']
    ]
    output = [
        ['39','02','dc','19'],
        ['25','dc','11','6a'],
        ['84','09','85','0b'],
        ['1d','fb','97','32']
    ]
    assert(aesEncryption(state, cipherKey) == output)

    print('...passed!\n')

# source : https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
# prints list into 2D from on terminal
# only for demonstration
def repr2dList(L):
    if (L == []): return '[]'
    output = [ ]
    rows = len(L)
    cols = max([len(L[row]) for row in range(rows)])
    M = [['']*cols for row in range(rows)]
    for row in range(rows):
        for col in range(len(L[row])):
            M[row][col] = repr(L[row][col])
    colWidths = [0] * cols
    for col in range(cols):
        colWidths[col] = max([len(M[row][col]) for row in range(rows)])
    output.append('[\n')
    for row in range(rows):
        output.append(' [ ')
        for col in range(cols):
            if (col > 0):
                output.append(', ' if col < len(L[row]) else '  ')
            output.append(M[row][col].rjust(colWidths[col]))
        output.append((' ],' if row < rows-1 else ' ]') + '\n')
    output.append(']')
    return ''.join(output)

def aesEncryptionDemo():
    cipherKey = [
        ['2b','28','ab','09'],
        ['7e','ae','f7','cf'],
        ['15','d2','15','4f'],
        ['16','a6','88','3c']
    ]
    state = [
        ['32','88','31','e0'],
        ['43','5a','31','37'],
        ['f6','30','98','07'],
        ['a8','8d','a2','34']
    ]
    output = [
        ['39','02','dc','19'],
        ['25','dc','11','6a'],
        ['84','09','85','0b'],
        ['1d','fb','97','32']
    ]
    input()
    print('state :')
    print(repr2dList(state))
    input()
    print('cipher key :')
    print(repr2dList(cipherKey))
    input()
    runEncrypt = input('encrypt with aesEncryption(state, cipherKey)?   ')
    if runEncrypt == 'y':
        print('encrypting...')
        result = aesEncryption(state, cipherKey)
        print('...encryption done!')
        input()
        print('result :')
        print(repr2dList(result))
        input()
        print('expected :')
        print(repr2dList(output))
    else:
        print('aes encryptor shutting down...')
    

#testGF2mArithmetic()
#testAESEncryption()
aesEncryptionDemo()

# Sources:
# AES Rijndael Cipher explained as a Flash animation
# AppliedGo
# https://www.youtube.com/watch?v=gP4PqVGudtg
# 
# Lecture 7: Introduction to Galois Fields for the AES by Christof Paar
# Introduction to Cryptography by Christof Paar
# https://www.youtube.com/watch?v=x1v2tX4_dkQ
#
# Lecture 8: Advanced Encryption Standard (AES) by Christof Paar
# Introduction to Cryptography by Christof Paar
# https://www.youtube.com/watch?v=NHuibtoL_qk
#
# AES Proposal: Rijndael
# Joan Daemen, Vincent Rijmen
# https://csrc.nist.gov/csrc/media/projects/cryptographic-standards-and-guidelines/documents/aes-development/rijndael-ammended.pdf
#
# AES Specifications:
#
# Low Level:
#   Arithmetic is conducted under GF(2^8)
#   Usually thought of with polynomial representation
#   a_{m-1} x^{m-1} + ··· + a_1 x^1 + a_0 = A(x) ∊ GF(2^m)
#
#       Addition = Subtraction:
#           C(x) = A(x) + B(x) = Σ^{m-1}_{i=0} c_i x^i
#               c_i = a_i + b_i (mod 2)
#
#       Multiplication:
#           C(x) = A(x) · B(x) mod P(x)
#               P(x) = x^8 + x^4 + x^3 + x + 1
#                    = 100011011 (b)
#                    = 11b (0x)
#                    = 283 (10)
#               P(x) should be an Irreducible Polynomial to have an inverse
#
#       Multiplicative Inverse:
#           A(x) · A^{-1}(x) ≅ 1 mod P(x)
#           Do not need to compute this because we work on a table
#           (Byte Substitution)
#
#
# AES Encryption Transformations:
# 1) byteSubstitution
# 2) shiftRow
# 3) mixCol
# 4) keyAdd
#
#
# AES Encryption Process:
#
# input
# ↓
# 1) initial round (1 round)
#       keyAdd
#
# 2) main rounds (9 rounds)
#       byteSub
#       shiftRow
#       mixCol
#       keyAdd
#
# 3) final round (1 round)
#       byteSub
#       shiftRow
#       keyAdd
# ↓
# output
#
#
# AES Key Schedule:
#   Expansion of the given Cipher key into 11 partial keys
#
#
#
#
#
#               https://www.youtube.com/watch?v=gP4PqVGudtg
#                               S-box
#
#     	00	01	02	03	04	05	06	07	08	09	0a	0b	0c	0d	0e	0f
#   00	63	7c	77	7b	f2	6b	6f	c5	30	01	67	2b	fe	d7	ab	76
#   10	ca	82	c9	7d	fa	59	47	f0	ad	d4	a2	af	9c	a4	72	c0
#   20	b7	fd	93	26	36	3f	f7	cc	34	a5	e5	f1	71	d8	31	15
#   30	04	c7	23	c3	18	96	05	9a	07	12	80	e2	eb	27	b2	75
#   40	09	83	2c	1a	1b	6e	5a	a0	52	3b	d6	b3	29	e3	2f	84
#   50	53	d1	00	ed	20	fc	b1	5b	6a	cb	be	39	4a	4c	58	cf
#   60	d0	ef	aa	fb	43	4d	33	85	45	f9	02	7f	50	3c	9f	a8
#   70	51	a3	40	8f	92	9d	38	f5	bc	b6	da	21	10	ff	f3	d2
#   80	cd	0c	13	ec	5f	97	44	17	c4	a7	7e	3d	64	5d	19	73
#   90	60	81	4f	dc	22	2a	90	88	46	ee	b8	14	de	5e	0b	db
#   a0	e0	32	3a	0a	49	06	24	5c	c2	d3	ac	62	91	95	e4	79
#   b0	e7	c8	37	6d	8d	d5	4e	a9	6c	56	f4	ea	65	7a	ae	08
#   c0	ba	78	25	2e	1c	a6	b4	c6	e8	dd	74	1f	4b	bd	8b	8a
#   d0	70	3e	b5	66	48	03	f6	0e	61	35	57	b9	86	c1	1d	9e
#   e0	e1	f8	98	11	69	d9	8e	94	9b	1e	87	e9	ce	55	28	df
#   f0	8c	a1	89	0d	bf	e6	42	68	41	99	2d	0f	b0	54	bb	16
#
#
# https://www.youtube.com/watch?v=gP4PqVGudtg
#               Rcon
#
#   01 02 04 08 10 20 40 80 1B 36
#   00 00 00 00 00 00 00 00 00 00
#   00 00 00 00 00 00 00 00 00 00
#   00 00 00 00 00 00 00 00 00 00
#
#
# https://www.youtube.com/watch?v=gP4PqVGudtg
#               mixCol matrix
#
#               02 03 01 01
#               01 02 03 01
#               01 01 02 03
#               03 01 01 02
