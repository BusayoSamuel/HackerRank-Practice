"""
Implement a simple text editor. The editor initially contains an empty string, . Perform  operations of the following  types:
1.append(W) - Append string W to the end of S.
2.delete(k) - Delete the last k characters of S.
3.print(k) - Print the kth character of S.
4.undo() - Undo the last (not previously undone) operation of type 1 or 2, reverting S to the state it was in prior to that operation.

Example
S = 'abcde'
ops = ['1 fg', '3 6', '2 5', '4', '3 7', '4', '3 4']

operation
index   S       ops[index]  explanation
-----   ------  ----------  -----------
0       abcde   1 fg        append fg
1       abcdefg 3 6         print the 6th letter - f
2       abcdefg 2 5         delete the last 5 letters
3       ab      4           undo the last operation, index 2
4       abcdefg 3 7         print the 7th characgter - g
5       abcdefg 4           undo the last operation, index 0
6       abcde   3 4         print the 4th character - d

The results should be printed as:

f
g
d
"""

class SimpleTextEditor:
    def __init__(self):
        self.S = ""
        self.stack = []
    
    def append(self, W):
        self.stack.append(self.S)
        self.S += W
    
    def delete(self, k):
        self.stack.append(self.S)
        self.S = self.S[:-k]
        
    def printk(self,k):
        print(self.S[k-1])
        
    def undo(self):
        self.S = self.stack.pop()
        
ste = SimpleTextEditor()
for _ in range(int(input())):
    q = input()
    
    if " " in q:
        q = q.split()
        if q[0] == "1":
            ste.append(q[1])
        elif q[0] == "2":
            ste.delete(int(q[1]))
        else:
            ste.printk(int(q[1]))
    else:
        ste.undo()