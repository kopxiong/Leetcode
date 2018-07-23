# Sort a linked list using insertion sort.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

'''
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current = head

        while current.next:
            if current.next.val < current.val:
                pre = dummy

                # find the insertion position (from the beginning direction)
                while pre.next.val < current.next.val:
                    pre = pre.next
                temp         = current.next
                current.next = temp.next
                temp.next    = pre.next
                pre.next     = temp
            else:
                current = current.next

        return dummy.next
'''

# faster
class Solution1(object):
    def insertionSortList(self, head):
        current = dummy = ListNode(0)
        while head:

            # reset pointer only when new number is smaller than pointer value
            if current and current.val > head.val:
                current = dummy

            # classic insertion sort to find position
            while current.next and current.next.val < head.val:
                current = current.next
            current.next, current.next.next, head = head, current.next, head.next # insert
        return dummy.next


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(2)
    head.next.next.next.next.next = ListNode(6)

    print(Solution1().insertionSortList(head))
