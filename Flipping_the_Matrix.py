"""
Sean invented a game involving a 2n x 2n matrix where each cell of the matrix contains an integer. He can reverse any of its rows 
or columns any number of times. The goal of the game is to maximize the sum of the elements in the n x n submatrix located in the 
upper-left quadrant of the matrix.

Given the initial configurations for q matrices, help Sean reverse the rows and columns of each matrix in the best possible way 
so that the sum of the elements in the matrix's upper-left quadrant is maximal.
Example
matrix = [[1,2],[3,4]]
1 2
3 4

It is 2 x 2 and we want to maximize the top left quadrant, a 1 x 1 matrix. Reverse row 1:

1 2
4 3

And now reverse column 0 :

4 2
1 3

The maximal sum is 4.
"""

def flippingMatrix(matrix):
    n = len(matrix)
    s = 0
    for i in range(n//2):
        for j in range(n//2):
            s += max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][n-j-1], matrix[n-i-1][j])
    return s