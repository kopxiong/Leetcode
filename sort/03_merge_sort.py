# -*- coding: utf-8 -*-
# 归并操作（merge），也叫归并算法，指的是将两个已经排序的序列合并成一个序列的操作。

# 迭代法（Top-down）
# 1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
# 2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置
# 3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
# 4. 重复步骤3直到某一指针到达序列尾
# 5. 将另一序列剩下的所有元素直接复制到合并序列尾

# 递归法（Bottom-up）
# 原理如下（假设序列共有n个元素）：
# 1. 将序列每相邻两个数字进行归并操作，形成ceil(n/2)个序列，排序后每个序列包含两/一个元素
# 2. 若此时序列数不是1个则将上述序列再次归并，形成ceil(n/4)个序列，每个序列包含四/三个元素
# 3. 重复步骤2，直到所有元素排序完毕，即序列数为1

# Time complexity: O(n log n), 需要 O(n) 额外空间


import random

# Bottom-up method
class Solution:
    def mergeSort(self, lists):
        if len(lists) <= 1:
            return lists

        middle = len(lists) // 2
        left   = self.mergeSort(lists[:middle])
        right  = self.mergeSort(lists[middle:])

        return self.merge(left, right)

    def merge(self, left, right):
        l, r   = 0, 0

        # top-down method, assign a storage space for the result list
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        # append the rest of left or right parts to the end
        result += left[l:]
        result += right[r:]

        return result


if __name__ == '__main__':
    lists = random.sample(range(100), 50)

    print(Solution().mergeSort(lists))
