from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeInt(node) :
    digit = 1
    num = 0
    currentNode = node
    while(True) :
        print(f'current Node ={currentNode.val}')
        num += currentNode.val * digit
        if currentNode.next==None:
            break
        currentNode = currentNode.next
        digit*=10
    return num

def makeListNode( alist) :
    preNode = None
    for v in alist :
        preNode = ListNode(v,preNode)
    return preNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return makeListNode(list(str(makeInt(l1) + makeInt(l2))))

# node1 = makeListNode([2,4,3])
# print(makeInt(node1))

# node2 = makeListNode([5,6,4])
# currentNode = node1
# while(True) :
#     print(f'current Node ={currentNode.val}')
#     if currentNode.next==None:
#         break
#     currentNode = currentNode.next

# currentNode = node2
# while(True) :
#     print(f'current Node ={currentNode.val}')
#     if currentNode.next==None:
#         break
#     currentNode = currentNode.next

