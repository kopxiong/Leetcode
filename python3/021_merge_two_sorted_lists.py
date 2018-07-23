# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
"""
class Solution(object):
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = current = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                current.next, current, l1 = l1, l1, l1.next
            else:
                current.next, current, l2 = l2, l2, l2.next
        # the rest elements will append to the list
        if not l1:
            current.next = l2
        else:
            current.next = l1
        #current.next = l1 or l2

        return dummy.next

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(5)
    l1.next.next = ListNode(7)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    print(Solution().mergeTwoLists(l1, l2))
