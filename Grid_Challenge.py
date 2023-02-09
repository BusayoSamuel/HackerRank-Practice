"""
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. 
Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
Example
grid = ['abc', 'adc', 'efg']
The grid is illustrated below.

a b c
a d e
e f g

The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer 
would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.
"""

def gridChallenge(grid):
    n = len(grid)
    m = len(grid[0])
    
    for i in range(n):
        grid[i] = sorted(grid[i])
        
    for j in range(m):
        for i in range(1,n):
            if ord(grid[i-1][j]) <= ord(grid[i][j]):
                continue
            return "NO"
    return "YES"