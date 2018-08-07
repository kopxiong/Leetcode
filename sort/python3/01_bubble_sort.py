# -*- coding: utf-8 -*-
# 冒泡排序 (Bubble Sort) 是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，
# 如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
# 这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

# Time complexity: O(n^2)

class Solution(object):
    def bubbleSort(self, lists):
        n = len(lists)

        # after each iteration, the last element is the maximum
        for i in range(n-1):
            flag = True
            for j in range(n-1-i):
                if lists[j] > lists[j+1]:
                    # swap, doesn't use temp because Python passes by reference (pointer in C++)
                    # shallow copy vs copy.deepcopy in Python
                    lists[j], lists[j+1] = lists[j+1], lists[j]
                    flag = False
            print("current lists: ", lists)

            # if no exchange, return arr or lists
            if flag:
                return lists

        return lists

if __name__ == '__main__':
    lists = [32, 64, 1, 4, 98, 23, 8, 46, 10, 90]
    #lists = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(Solution().bubbleSort(lists))
