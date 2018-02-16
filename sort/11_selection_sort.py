# -*- coding: utf-8 -*-
# 选择排序 (Selection sort) 的工作原理大致是将后面的元素中最小的元素一个个取出然后按顺序放置。可以看成是冒泡排序的优化，减少了交换的次数

# Time complexity: O(n^2)

class Solution(object):
    def selectionSort(self, lists):
        n = len(lists)

        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if lists[j] < lists[min_idx]:
                    min_idx = j
            if min_idx != i:
                lists[min_idx], lists[i] = lists[i], lists[min_idx]
            print("current lists: ", lists)
        return lists

if __name__ == '__main__':
    lists = [32, 64, 1, 4, 98, 23, 8, 46, 10, 90]

    print(Solution().selectionSort(lists))
