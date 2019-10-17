# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        low2high=0
        re= ListNode(0)
        r= re
        while (l1 or l2): 
            a  = l1.val if l1 else 0
            b  = l2.val if l2 else 0
            r.next=ListNode((a+b+low2high)%10)
            r=r.next
            print(r.val)
            low2high=int((a+b+low2high)/10)
            if l1==None and l2==None:
                break
            if(l1!=None):l1 = l1.next
            if(l2!=None):l2 = l2.next
        if low2high>0:
            r.next = ListNode(1)
        return re.next
