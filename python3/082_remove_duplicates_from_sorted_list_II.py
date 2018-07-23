# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

# create a dummy node to store the last previous node
# class Solution:
#     def deleteDuplicates(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head is None:
#             return
#         dummy = ListNode(0)
#         dummy.next = head
#         pre, temp = dummy, head
#         flag = False
#
#         while(temp and temp.next):
#             if temp.next.val == temp.val:
#                 temp.next = temp.next.next
#                 flag = True
#             else:
#                 if not flag:
#                     temp = temp.next
#                     pre  = pre.next
#                 else:
#                     pre.next = temp.next
#                     flag = False
#
#         return dummy.next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return

        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur = self.helper(cur.next)    # to remove the same val's node
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next

    def helper(self, cur):
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur = cur.next
            else:
                return cur.next
        return cur.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(4)

    print("before duplicates deletion: ", head)
    print("after duplicates deletion: ", Solution().deleteDuplicates(head))
