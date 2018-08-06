// Merge two sorted linked lists and return it as a new list.
// The new list should be made by splicing together the nodes of the first two lists.

#include <iostream>

// Definition for single-linked list
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;

        ListNode* current = new ListNode(0);
        ListNode* dummy = current;

        while (l1 && l2) {
            if (l1->val <= l2->val) {
                current->next = l1;
                current       = l1;
                l1            = l1->next;
            }
            else {
                current->next = l2;
                current       = l2;
                l2            = l2->next;
            }
        }
        if (!l1) {
            current->next = l2;
        }
        if (!l2) {
            current->next = l1;
        }

        return dummy->next;
    }
};


int main() {
    Solution Test;
    ListNode *l1 = new ListNode(1);
    l1->next = new ListNode(2);
    l1->next->next = new ListNode(5);
    ListNode *l2 = new ListNode(1);
    l2->next = new ListNode(3);
    l2->next->next = new ListNode(4);

    ListNode *result = Test.mergeTwoLists(l1, l2);

    while (result) {
        std::cout << result->val << std::endl;
        result = result->next;
    }

    // std::cout << "the merged sorted list is: " << Test.mergeTwoLists(l1, l2) << std::endl;

    return 0;
}
