"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6  places after the decimal.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
though answers with absolute error of up to 10^-4 are acceptable.
Example
arr = [1, 1, 0, -1, -1]
There are n = 5 elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000
Results are printed as:
0.400000
0.400000
0.200000
"""

def plusMinus(arr):
    array_size = len(arr)
    pos_elements = 0
    neg_elements = 0
    zero_elements = 0
    
    for i in arr:
        if i > 0:
            pos_elements += 1
        elif i < 0:
            neg_elements += 1
        else:
            zero_elements += 1
    
    pos_ratio = pos_elements/array_size
    neg_ratio = neg_elements/array_size
    zero_ratio = zero_elements/array_size
    
    print(f"{pos_ratio: 6f}")
    print(f"{neg_ratio: 6f}")
    print(f"{zero_ratio: 6f}")

    """
    print('%.6f' % (pos_elements/array_size))
    print('%.6f' % (neg_elements/array_size))
    print('%.6f' % (zero_elements/array_size))
    """
    