#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 桶排序 (Bucket sort)或箱排序 (Bin sort)，桶排序算是计数排序的一种改进和推广，原理是将数组分到有限数量的桶里。每个桶再个别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）。桶排序是鸽巢排序 (Pigeonhole sort) 的一种归纳结果。当要被排序的数组内的数值是均匀分配的时候，桶排序使用线性时间 O(n)。但桶排序并不是比较排序，他不受到 O(n\log n)下限的影响。

# 1. 设置一个定量的数组当作空桶子
# 2. 寻访序列，并且把项目一个一个放到对应的桶子去
# 3. 对每个不是空的桶子进行排序
# 4. 从不是空的桶子里把项目再放回原来的序列中

# Stable
# Time: O(n + k), linear complexity !!!!!!， worst case: O(n^2)
# Auxiliary Space: O(n + k)

import random

"""
# 范围是1~M的桶排序
class Solution:
    def bucketSort(self, lists):
        _max = max(lists)
        _min = min(lists)
        # 建立 max-min+1 个桶，将 min~max 区间的数都置为0
        # 每个桶代表的值分别为min,min+1,min+2,...,max
        count = [0 for i in range(_min, _max + 1)]      #count = [0] * (max_num - min_num + 1)
        # 遍历数组，对于元素i，其对应的桶s[i-_min]加1
        for i in lists:
            count[i - _min] += 1
        current = _min
        # n为新list的计数变量
        n = 0
        for index in count:
            while index > 0:
                lists[n] = current
                index   -= 1
                n       += 1
            current += 1
        return lists
"""

# 基于插入排序的区间为[0,1)均匀分布的桶排序
class Solution1:
    def insertSort(self, lists):
        n = len(lists)
        if n <= 1:
            pass
        for i in range(1, n):
            key = lists[i]
            j   = i - 1
            while key < lists[j] and j >= 0:
                lists[j+1] = lists[j]
                j         -= 1
            lists[j+1] = key

    def sort(self, lists):
        n = len(lists)
        s = [[] for i in range(n)]     # 将[0,1)划分成n个相同大小的子区间（桶）
        for i in lists:                # 将n个输入数分布到各个桶中
            s[int(i*n)].append(i)
        new_list = []
        for lst in s:
            self.insertSort(lst)
            new_list.extend(lst)    # vs append

        return new_list

    def bucketSort(self, lists):
        return self.sort(lists)

if __name__ == "__main__":
    #lists = [random.randint(0, 20) for i in range(20)]
    lists = [random.random() for i in range(10)]

    print("Before sorting: ", lists)
    print("After sorting: ",Solution1().bucketSort(lists))
