"""
Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the 
string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no 
solution, return -1. Otherwise, return the index of a character to remove.
Example
s = "bcbc"
Either remove 'b' at index 0 or 'c' at index 3.
"""

def palindromeIndex(s):
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            new_s = s[:i] + s[i+1:]
            if new_s == new_s[::-1]:
                return i
            return -(i+1) + len(s)
    return -1
