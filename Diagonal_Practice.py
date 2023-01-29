"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix arr is shown below:
1 2 3
4 5 6
9 8 9

The left-to-right diagonal = 1+5+9 = 15. The right to left diagonal = 3 + 5 + 9 = 17 . Their absolute difference is |15-17| = 2.
"""

def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    
    for i in range(len(arr)):
        left_to_right += arr[i][i]
        right_to_left += arr[i][-1-i]
        
    return(abs(right_to_left - left_to_right))

#Alternative
def diagonalDifference2(arr):
    n = len(arr)

    left_to_right = sum(arr[i][i] for i in range(n))
    right_to_left = sum(arr[i][-1-i] for i in range(n))

    return(abs(right_to_left - left_to_right))