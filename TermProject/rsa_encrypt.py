# name : Jun Hee Oh
# id : junheeo

# RSA algoritm : https://www.youtube.com/watch?v=QSlWzKNbKrU

import random
import pickle

# Algorithm : CMU 21-127 Concepts of Mathematics Prof.Ervin Fall 2021 Lec 2 Lecture Note 11/29+12/1+12/3.pdf
# https://canvas.cmu.edu/courses/24963/files/folder/LECTURE%20NOTES?preview=7335260
# extended Eucledian Algorithm
# input int, int return int, int, int, int
# input : two positive integers a, b
# output : gcd = a * m + b * n
def extEA(a, b):
    if a <= 0 or b <= 0:
        print(f'InputError : inputs of should be positive : extEA()')
        return None
    if a == b:
        return a, a, 1, b, 0
    originalA = a
    originalB = b

    if a < b:
        temp = a
        a = b
        b = temp
    # p is greater than q

    aPrime, bPrime, q, r = a, b, 1, 1
    aEqualsbTimesqPlusr = list()
    while r > 0:
        q = aPrime // bPrime
        r = aPrime % bPrime
        if r == 0:
            break
        aEqualsbTimesqPlusr.insert(0,(aPrime, bPrime, q, r))
        aPrime = bPrime
        bPrime = r
    
    gcd = aEqualsbTimesqPlusr[0][3]

    a, b, q, r = aEqualsbTimesqPlusr[0]
    m, n, o, p = a, 1, b, -q
    m, n, j, k, s, t = m, n, 0, 0, 0, p
    for abqr in aEqualsbTimesqPlusr[1:]:
        a, b, q, r = abqr   # we know that r = a - b * q
        m, n, j, k, s, t = m, n, a, b, q, p # gcd = m * n + (a - b * q) * t
        m, n, o, p = j, t, m, n - s * t # gcd = j * t + m * (n - s * t)
    

    if originalA == o:
        temp = n
        n = p
        p = temp
    
    return gcd, originalA, n, originalB, p


primeList = list()


def readStringPrimeList():
    with open('/Users/junheeoh/Code/TermProject/primeList.txt', 'rb') as f:
        primeList = pickle.load(f)
    return primeList

def convertStringPrimeListToIntPrimeList(primeList):
    for i in range(len(primeList)):
        primeList[i] = int(primeList[i])
    print(primeList)
    return primeList

def print1000PrimeList():
    convertStringPrimeListToIntPrimeList(readStringPrimeList())

primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]


def primeTestRound(a, n, r, d):
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for i in range(r):
        #print(f'i = {i}')
        x = pow(a ,(2 ** i) * d, n)     # using ** causes memory error for large numbers
        if x == n - 1:
            return True
    return False

# inputs :
#       n : odd integer to test prime
#       k : rounds of test
# outputs :
#       True : probably is a prime
#       False : probably is not a prime
# pseudocode : https://en.wikipedia.org/wiki/Miller–Rabin_primality_test
# math : https://www.youtube.com/watch?v=zmhUlVck3J0
def millerRabinTest(n, k):

    r = 0
    d = 1
    tempN = n - 1
    while True:
        if tempN % 2 == 0:
            r += 1
            tempN = tempN // 2
        else:
            d = tempN
            break

    for round in range(k):
        a = random.randint(2, n - 2)
        #print(f'a = {a}')
        if primeTestRound(a, n, r, d) == False:
            return False
    return True

def findLargePrimes():
    while True:
        a = random.randint(2**(256), 2**(300))
        b = random.randint(2**(256), 2**(300))
        if a == b:
            continue
        elif abs(a - b) < 100:
            continue
        else:
            areBothPrimes = True
            for prime in primeList:
                if a % prime == 0 or b % prime == 0:
                    areBothPrimes = False
            if areBothPrimes == True:
                if millerRabinTest(a, 10) == False or millerRabinTest(b, 10) == False:
                    continue
            else:
                continue
        return a, b

def rsaCreateKeys():
    gcd = 0
    while gcd != 1:
        p, q = findLargePrimes()
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randint(1, phi - 1)
        Kpub = e
        # Kpr = d  s.t. d * e = 1 mod phi
        # <=> e * d + phi * y = gcd(a, phi) = 1
        gcd, e, d, phi, y = extEA(e, phi)
        Kpr = d
    assert(gcd == e*d + phi*y)
    return Kpub, Kpr, n

# input : int
# output : int
def rsaEncrypt(x, e, n):
    if not 1 <= x <= n - 1:
        print('InputError : x out of range : rsaEncrypt()')
        return None
    y = pow(x, e, n)
    return y
def rsaDecrypt(y, d, n):
    x = pow(y, d, n)
    return x



####### TEST FUNCTIONS

def testRSA():
    e, d, n = rsaCreateKeys()
    print(f'd = {d}')
    print(f'rsaEncrypt(1, e, n) = {rsaEncrypt(8, e, n)}')
    print(chr(rsaDecrypt(rsaEncrypt(int(ord('a')), e, n), d, n)))
    print(rsaDecrypt(rsaEncrypt(1, e, n), d, n) == 1)
    print(rsaDecrypt(rsaEncrypt(3, e, n), d, n) == 3)
    print(rsaDecrypt(rsaEncrypt(50, e, n), d, n) == 50)
    print(rsaDecrypt(rsaEncrypt(462, e, n), d, n) == 462)
    print(rsaDecrypt(rsaEncrypt(2503, e, n), d, n) == 2503)
    print(rsaDecrypt(rsaEncrypt(31235132123812311532, e, n), d, n) == 31235132123812311532)
#testRSA()

# nonPrimeCount = 0
# for prime in primeList[5000:5100]:
#     if millerRabinTest(n, 300) == False:
#         print(f'{n} is a prime!')
#         nonPrimeCount += 1
# print(f'prob = {nonPrimeCount/999}')

def testMillerRabinTest():
    n = 5669
    k = 8
    print(f'millerRabinTest({n}, {k}) = {millerRabinTest(n, k)}')
    assert(millerRabinTest(n, k) == True)
    n = 5667
    k = 8
    print(f'millerRabinTest({n}, {k}) = {millerRabinTest(n, k)}')
    assert(millerRabinTest(n, k) == False)
    n = 5666
    k = 8
    print(f'millerRabinTest({n}, {k}) = {millerRabinTest(n, k)}')
    assert(millerRabinTest(n, k) == False)
    n = 5665
    k = 8
    print(f'millerRabinTest({n}, {k}) = {millerRabinTest(n, k)}')
    assert(millerRabinTest(n, k) == False)
    n = 5664
    k = 8
    print(f'millerRabinTest({n}, {k}) = {millerRabinTest(n, k)}')
    assert(millerRabinTest(n, k) == False)
    n = 5663
    k = 8
    print(f'millerRabinTest({n}, {k}) = {millerRabinTest(n, k)}')
    assert(millerRabinTest(n, k) == False)


    primes = {7541, 7547, 7549, 7559, 7561, 7573, 7577, 7583, 7589, 7591, 7603, 7607, 7621, 7639, 7643, 7649}
    max = 7649
    min = 7541
    print(max + 1 - min)
    falseCount = 0
    for val in range(min, max + 1):
        print(val)
        isPrime = millerRabinTest(val, 8)
        if (val in primes) and isPrime == False:
            print(f'{val} is a prime!!')
            falseCount += 1
        elif (val not in primes) and isPrime == True:
            print(f'{val} is not a prime!!')
            falseCount += 1
    print(f'propFalse = {falseCount / (max - min)}')

#testMillerRabinTest()


def testfindLargePrimes():
    def existsDividingPrime(a,b):
        for prime in primeList:
            if a % prime == 0 or b % prime == 0:
                return False
        return True

    p, q = findLargePrimes()
    print(existsDividingPrime(p,q))
    print(millerRabinTest(p, 10))
    print(millerRabinTest(q, 10))
    print(findLargePrimes())

#testfindLargePrimes()


# extEA(111, 64)
# extEA(3587, 1819)
# extEA(1819, 3587)