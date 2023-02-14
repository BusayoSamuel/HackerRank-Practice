"""
Jesse loves cookies and wants the sweetness of some cookies to be greater than value k. To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined 
cookie with:
sweetness = (1 x Least sweet cookie + 2 x 2nd least sweet cookie).
This occurs until all the cookies have a sweetness >= k.
Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return -1.
Example
k = 9
A = [2, 7, 3, 6, 4, 6]
The smallest values are 2,3.
Remove them then return 2 + 2 x 3 = 8 to the array. Now A = [8, 7, 6, 4, 6].
Remove 4, 6 and return 4 + 6 x 2 = 16 to the array. Now A = [16, 8, 7, 6].
Remove 6, 7, return 6 + 2 x 7 = 20 and A = [20, 16, 8, 7].
Finally, remove 8, 7 and return 7 + 2 x 8 = 23 to A. Now A = [28, 20, 16].
All values are >= k = 9 so the process stops after 4 iterations. Return 4.
"""

def cookies(k, A):
    count = 0
    while min(A) < k and len(A) > 1:
        least = min(A)
        A.remove(min(A))
        sec_least = min(A)
        A.remove(min(A))
        sweetness = (1 * least) + (2 * sec_least)
        A.append(sweetness)
        count += 1
        
    if min(A) < k:
        return -1
    else:
        return count
