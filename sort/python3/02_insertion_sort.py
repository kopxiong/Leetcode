# -*- coding: utf-8 -*-
# 插入排序 (Insertion Sort) 的工作原理是通过构建有序序列，对于未排序数据，
# 在已排序序列中从后向前扫描，找到相应位置并插入。类似于打扑克牌分牌的时候，拿到一张新牌，然后找到合适的位置插入。

# Time complexity: O(n^2)

class Solution(object):
    def insertionSort(self, lists):
        n = len(lists)

        for i in range(n):
            j = i - 1
            key = lists[i]
            while j >= 0 and lists[j] > key:
                lists[j+1] = lists[j]
                j = j - 1
            lists[j+1] = key
            print("current lists: ", lists)

        return lists

if __name__ == '__main__':
    lists = [32, 64, 1, 4, 98, 23, 8, 46, 10, 90]

    print(Solution().insertionSort(lists))
