"""
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be 
removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because 
the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:
- Enqueue: add a new element to the end of the queue.
- Dequeue: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using two stacks. Then process q queries, where each query is one of the 
following 3 types:

1. 1 x: Enqueue element x into the end of the queue.
2. 2: Dequeue the element at the front of the queue.
3. 3: Print the element at the front of the queue.
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        if self.head:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
        else:
            self.head = Node(data)
        
    def pop(self):
        if self.head:
            res = self.head.data
            self.head = self.head.next
            return res
        else:
            return None
    
class Queue:
    def __init__(self):
        self.head = None
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def enqueue(self, data):
        if not self.stack1.head:
            self.head = Node(data)
        self.stack1.push(data)
        
    def dequeue(self):
        #print("Here")
        while self.stack1.head:
            self.stack2.push(self.stack1.pop())
        
        res = self.stack2.pop()
        #print(res)
        self.head = self.stack2.head
        
        while self.stack2.head:
            self.stack1.push(self.stack2.pop())
            
        return res
    
queue = Queue()
for _ in range(int(input())):
    q = input()
    if " " in q:
        if q.split()[0] == "1":
            queue.enqueue(q.split()[1])
    else:
        if q == "2":
            queue.dequeue()
        if q == "3":
            if queue.head:
                print(queue.head.data)
            else:
                print(None)
            