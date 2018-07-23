# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

'''
# Algorithm: Brute Force
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: list[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)

        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for k in sorted(self.nodes):
            point.next = ListNode(k)
            point = point.next

        return head.next
'''

# Algorithm1: Divide and Conquer
class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: list[ListNode]
        :rtype: ListNode
        """
        nums = len(lists)
        delta = 1
        while delta < nums:
            for i in range(0, nums - delta, delta * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + delta])
            delta *= 2

        return lists[0] if nums > 0 else lists

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next, current, l1 = l1, l1, l1.next
            else:
                current.next, current, l2 = l2, l2, l2.next

        # the rest elements will append to the list
        if l1 != None:
            current.next = l1
        elif l2 != None:
            current.next = l2

        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(3)
    l1.next = ListNode(5)
    l2 = ListNode(4)
    l2.next = ListNode(7)
    l2.next.next = ListNode(8)
    l3 = ListNode(1)
    l3.next = ListNode(9)
    l3.next.next = ListNode(11)
    l4 = ListNode(2)
    l4.next = ListNode(12)
    l4.next.next = ListNode(14)
    l5 = ListNode(2)
    l5.next = ListNode(6)
    lists = [l1, l2, l3, l4, l5]

    print(Solution1().mergeKLists(lists))
