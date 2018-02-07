# -*- coding: utf-8 -*-
# 希尔排序 (Shell sort)，也称递减增量排序算法，非稳定排序算法, 是插入排序的一种更高效的改进版本。

# 希尔排序是基于插入排序的以下两点性质而提出改进方法的：
# 1. 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
# 2. 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位。

# Time complexity: O(n log n)

class Solution(object):
    def shellSort(self, arr):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                key = arr[i]
                j = i

                # the same with insertion sort method
                while j >= gap and arr[j - gap] > key:
                    arr[j] = arr[j - gap]
                    j = j - gap
                arr[j] = key
            gap = gap // 2

        return arr

if __name__ == '__main__':
    lists = [32, 64, 1, 4, 98, 23, 8, 46, 10, 90]

    print(Solution().shellSort(lists))
