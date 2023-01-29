"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number 
of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a 
rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

Example
s = There's-a-starman-waiting-in-the-sky
k = 3
The alphabet is rotated by 3, matching the mapping above. The encrypted string is Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb.
Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
"""

def caesarCipher(s, k):
    s = list(s)
    k = k % 26
    upper = False
    
    for i in range(len(s)):
        if ord(s[i]) in range(97, 123):
            upper = False
        elif ord(s[i]) in range(65, 91):
            upper = True
        else:
            continue
        
        cipher = ord(s[i]) + k
        
        if upper and cipher >= 91:
            cipher -= 26
        elif not upper and cipher >= 123:
            cipher -= 26
            
        s[i] = chr(cipher)
    
    return "".join(s)