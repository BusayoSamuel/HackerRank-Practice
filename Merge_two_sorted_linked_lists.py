"""
Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null
meaning that the corresponding list is empty.

Example
headA refers to 1 -> 3 -> 7 -> NULL
headB refers to 1 -> 2 -> NULL

The new list is 1 -> 1 -> 2 -> 3 -> 7 -> NULL 
"""

def mergeLists(head1, head2):
    head1_list = []
    head2_list = []
    
    while head1 != None:
        head1_list.append(head1.data)
        head1 = head1.next
        
    while head2 != None:
        head2_list.append(head2.data)
        head2 = head2.next
        
    merge = head1_list + head2_list
    merge.sort()
    
    head = SinglyLinkedListNode(merge[0])
    pointer = head
    
    for node in merge[1:]:
        pointer.next = SinglyLinkedListNode(node)
        pointer = pointer.next
        
    pointer.next = None
    return head

#or

def mergeLists2(head1, head2):
    sys.setrecursionlimit(2000)
    if not head1:
        return head2
    
    if not head2:
        return head1
        
    if head1.data < head2.data:
        merge = head1
        merge.next = mergeLists(head2, head1.next)
    else:
        merge = head2
        merge.next = mergeLists(head1, head2.next)
        
    return merge