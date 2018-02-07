# -*- coding: utf-8 -*-
# 选择排序 (Selection sort) 的工作原理大致是将后面的元素中最小的元素一个个取出然后按顺序放置。

# Time complexity: O(n^2)

class Solution(object):
    def selectionSort(self, arr):
        n = len(arr)

        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[key]:
                    min_idx = j
            arr[min_idx], arr[i] = arr[i], arr[min_idx]

        return arr

if __name__ == '__main__':
    lists = [32, 64, 1, 4, 98, 23, 8, 46, 10, 90]

    print(Solution().selectionSort(lists))
