"""
Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target 
value.

Example
k = 1
arr = [1,2,3,4]

There are three values that differ by k = 1: 2 - 1 = 1 , 3 - 2 = 1, and 4 - 3 = 1. Return 3.
"""
def pairs(k, arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i]-arr[j]) == k:
                count += 1
    
    return count

#A more efficient approach
def pairs(k, arr):
    arr.sort()
    i = 0
    j = 1
    count = 0
    
    while j < len(arr):
        diff = arr[j] - arr[i]
        
        if diff == k:
            count += 1
            j += 1
        elif diff > k:
            i += 1
        else:
            j += 1
            
    return count