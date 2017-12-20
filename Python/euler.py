# -*- coding: utf-8 -*-
import math
import numpy
from primes import primes

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def euler1():
    maxVal = 1000
    fizzBuzz = [ elem for elem in range(maxVal) if elem%3 == 0 or elem%5 == 0]
    return sum(fizzBuzz)

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def euler2():
    maxVal = 4000000
    prev = 0
    curr = 1
    s = 0
    while ( curr < maxVal ):
        temp = prev + curr
        prev = curr
        curr = temp
        if curr%2 == 0:
            s += curr
    return s

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
def euler3():
    maxVal = 600851475143
    p = primes()
    pList = p.primesLessThan(math.sqrt(maxVal))
    primeFactors = [elem for elem in pList if maxVal%elem == 0]
    return primeFactors[-1]

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers.
def euler4():
    maxPalindrome = 0
    threeDigitNums = range(100,1000,1)

    for i in threeDigitNums:
        for j in [ elem for elem in threeDigitNums if elem >= i ]:
            if isPalindrome(i*j) and i*j > maxPalindrome:
                maxPalindrome = i*j

    return maxPalindrome

def isPalindrome(s):
    s = str(s)
    return s == s[::-1]

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# FASTER METHOD, GENERATE PRIME FACTORS AND MULTIPLY THEM
def euler5():
    maxVal = 20
    curr = maxVal
    nums = range(1,maxVal+1,1)
    while not all( [curr%elem == 0 for elem in nums] ):
        curr = curr + maxVal
    return curr

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def euler6():
    maxVal = 100
    array = range(1,maxVal + 1)
    sumOfSquares = sum([ elem**2 for elem in array ])
    squareOfSums = sum(array)**2
    return squareOfSums - sumOfSquares

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
def euler7():
    index = 10001
    p = primes()
    return p.primeAt(index)

# The four adjacent digits in the 1000-digit number that have the greatest product are 9*9*8*9=5832
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
def euler8():
    length = 13
    i = 0
    maxVal = 0
    with open('euler8.d', 'r') as f:
        data = f.read()
    while( i + length < len(data) ):
        val = 1
        for j in range(length):
            val = val * int(data[i+j])
        if val > maxVal:
            maxVal = val
        i = i + 1
    return maxVal

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
def euler9():
    tripSum = 1000
    checkVal = tripSum / 2
    for a in range(1,checkVal+1):
        for b in range(1,checkVal+1):
            c = math.sqrt( a**2 + b**2 )
            if c.is_integer():
                c = int(c)
                s = a + b + c
                if s == tripSum:
                    return a * b * c
    return None

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
def euler10():
    maxVal = 2000000
    p = primes()
    return sum(p.primesLessThan(maxVal))

# In the 20x20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 x 63 x 78 x 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?
def euler11():
    maxProd = 0
    numbers = 4
    with open('euler11.d', 'r') as f:
        i = 0
        array = []
        for line in f:
            array.append([int(elem) for elem in line.split()])
    npArray = numpy.array(array)

    for r in range(npArray.shape[0]):
        for c in range(npArray.shape[1]):
            # check row
            if r <= npArray.shape[0] - numbers:
                p = numpy.prod(npArray[r:r+numbers,c])
                if p > maxProd:
                    maxProd = p
            # check column
            if c <= npArray.shape[1] - numbers:
                p = numpy.prod(npArray[r,c:c+numbers])
                if p > maxProd:
                    maxProd = p
            # check right diagonal
            if (r <= npArray.shape[0] - numbers and c <= npArray.shape[1] - numbers):
                p = 1
                for i in range(numbers):
                    p = p * npArray[r+i,c+i]
                if p > maxProd:
                    maxProd = p
            # check left diagonal 
            if (r >= numbers - 1 and c <= npArray.shape[1] - numbers):
                p = 1
                for i in range(numbers):
                    p = p * npArray[r-i,c+i]
                if p > maxProd:
                    maxProd = p
    
    return maxProd

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?
def euler12():
    nextNatural = 9337
    triangleNumber = 43585116
    desiredDivisors = 500
    # generate traingle number
    while True:
        triangleNumber = triangleNumber + nextNatural
        nextNatural = nextNatural + 1
        divisors = findNumberOfDivisors(triangleNumber)
        print str(triangleNumber) + ':' + str(nextNatural) + ':' + str(divisors)
        if divisors > desiredDivisors:
            return triangleNumber

def findNumberOfDivisors( number ):
    numberOfDivisors = 0
    for i in range(1,number+1):
        if number%i == 0:
            numberOfDivisors = numberOfDivisors + 1
    return numberOfDivisors

def getNumberOfDivisors( num ):
    pass

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
def euler13():
    array = []
    with open('euler13.d', 'r') as f:
        for line in f:
            array.append(int(line.rstrip()))
    return str(sum(array))[0:10]

# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
def euler14():
    s = collatz()
    maxLength = 0
    maxI = 0
    numsToCheck = range(1,1000000)
    while len(numsToCheck) > 0:
        num = numsToCheck.pop()
        collatzSeq = s.getCollatz(num)
        length = len(collatzSeq)
        if length > maxLength:
            maxLength = length
            maxI = num
        numsToCheck = [ elem for elem in numsToCheck if elem not in collatzSeq ]
    return maxI

class collatz:
    dCollatz = {}
    dLength = {}

    def __init__(self):
        return

    def getCollatz(self, num):
        if num in self.dCollatz.keys():
            return self.dCollatz[num]
        if num:
            array = [num] + self.getCollatz(self.nextCollatzNum(num))
            self.dCollatz[num] = array
            return array
        else:
            return []

    def getCollatzLength(self, num):
        if num in self.dLength.keys():
            # print str(num) + ' in dictionary'
            return self.dLength[num]
        if num:
            length = 1 + self.getCollatzLength(self.nextCollatzNum(num))
            self.dLength[num] = length
            return length
        else:
            return 0

    def nextCollatzNum(self, num):
        if num == 1:
            return None
        elif num%2 == 0:
            return num/2
        else:
            return 3*num+1

if __name__ == "__main__":
    print "Euler14: " + str(euler14())
