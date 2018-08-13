# -*- coding: utf-8 -*-
# 快速排序 (Quick sort)，又称划分交换排序（partition-exchange sort），快速排序使用分治法（Divide and conquer）策略把一个序列（list）分为两个子序列（sub-lists）。
# 基本思想： 冒泡 + 二分 + 递归分治

# 1. 从数列中挑出一个元素，称为"基准"（pivot）
# 2. 重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
# 3. 递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。

# Optimal time complexity: O(n log n), worst case: O(n^2)


"""
# in-place sorting
class Solution:
    def quickSort(self, lists, low, high):
        if low < high:
            p = self.partition(lists, low, high)      # find the pivot
            self.quickSort(lists, low, p)
            self.quickSort(lists, p+1, high)

        return

    def partition(self, lists, low, high):
        pivot = lists[high-1]     # take the last element as pivot
        i = low - 1
        for j in range(low, high):
            if lists[j] < pivot:
                i += 1
                lists[i], lists[j] = lists[j], lists[i]

        # exchange the higher part to the end
        if lists[high-1] < lists[i+1]:
            lists[i+1], lists[high-1] = lists[high-1], lists[i+1]

        return i+1
"""

# this solution needs more extra space
class Solution1:
    def quickSort(self, lists):
        low = []
        pivotList = []
        high = []

        if len(lists) <= 1:
            return lists
        else:
            pivot = lists[0]
            for i in lists:
                if i < pivot:
                    low.append(i)
                elif i > pivot:
                    high.append(i)
                else:
                    pivotList.append(i)
            low = self.quickSort(low)
            high = self.quickSort(high)
            return low + pivotList + high

if __name__ == '__main__':
    lists = [32, 64, 1, 4, 98, 23, 8, 46, 10, 45]

    print(Solution1().quickSort(lists))
