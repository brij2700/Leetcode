# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        answer=ListNode()
        head=answer
        while(l1 or l2 or carry):
            answer.next=ListNode()
            answer=answer.next
            l1_val=l1.val if l1 else 0
            l2_val=l2.val if l2 else 0
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            sum_val=l1_val+l2_val+carry
            carry=sum_val//10
            sum_val=sum_val%10
            answer.val=sum_val
        return head.next

            