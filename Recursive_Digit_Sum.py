"""
We define super digit of an integer x using the following rules:
Given an integer, we need to find the super digit of the integer.
- If x has only 1 digit, then its super digit is x.
- Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.

For example, the super digit of 9875 will be calculated as:
	super_digit(9875)   9+8+7+5 = 29 
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2 
    
Example
n = "9875"
k = 4

The number p is created by concatenating the string n k times so the initial p = 9875987598759875.
    superDigit(p) = superDigit(9875987598759875)
                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    superDigit(p) = superDigit(116)
                  1+1+6 = 8
    superDigit(p) = superDigit(8)

All of the digits of p sum to 116. The digits of 116 sum to 8. 8  is only one digit, so it is the super digit.
"""

def superDigit1(n, k):  #Inefficient with memory
    p = k * n
    
    p = list([int(i) for i in p])
        
    while sum(p) >= 10:
        p = list([int(i) for i in str(sum(p))])
        
    return sum(p)

def superDigit2(n, k): 
    if k == len(n) == 1:
        return n
    
    res = 0
    for i in n:
        res += int(i)
    res = res * k
    
    return superDigit(str(res), 1)

#or

def superDigit3(n, k):
    
    p = str(sum(map(int, [*n]))*k)
        
    while len(p) > 1:
        p =  str(sum(map(int, [*p])))
        
    return int(p)