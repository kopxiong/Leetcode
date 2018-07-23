# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        temp = head

        while(temp and temp.next):
            if temp.next.val == temp.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(3)

    print("before duplicates deletion: ", head)
    print("after duplicates deletion: ", Solution().deleteDuplicates(head))
