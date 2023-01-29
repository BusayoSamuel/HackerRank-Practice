"""
Given an array of integers, where all elements but one occur twice, find the unique element.
Example
a = [1,2,3,4,3,2,1]
The unique element is 4 .
"""

def lonelyinteger(a):
    counts = {}
    
    for i in a:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
            
    for i in counts:
        if counts[i] == 1:
            return i

#Alternatives
def lonelyinteger2(a):
    unique_element = []
    
    for i in a:
        if i in unique_element:
            unique_element.remove(i)
        else:
            unique_element.append(i)
            
    return unique_element[0]

