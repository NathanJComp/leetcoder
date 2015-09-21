# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        output = ListNode(0)
        carry=0
        while l1 or l2:
            if l1:
                value1=l1.val if l1 else 0
                value2=l2.val if l2 else 0
                l1=l1.next if l1 else l1
                l2=l2.next if l2 else l2
                output.next = ListNode((value1+value2+carry)%10)
                carry = (value1+value2+carry)//10
                output = output.next
            if carry:
                output.next = ListNode(carry)
            return output