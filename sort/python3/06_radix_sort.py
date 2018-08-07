#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 基数排序 (Radix sort) 是一种非比较型整数排序算法，属于"分配式排序"(distribution sort)，又称"桶子法"(bucket sort)或 bin sort，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。
# 它是这样实现的：将所有待比较数值（正整数）统一为同样的数位长度，数位较短的数前面补零。然后，从最低位开始，依次进行一次排序。这样从最低位排序一直到最高位排序完成以后，数列就变成一个有序序列。
# 基数排序的方式可以采用 LSD(Least significant digital)或 MSD(Most significant digital)，LSD的排序方式由键值的最右边开始，而 MSD则相反，由键值的最左边开始。

# 1. 时间复杂度：O(d * n), n是排序元素个数，d是数字位数
# 2. 空间复杂度：O(k + n), n是排序元素个数，k是单位数字最大值
# 3. 基数排序算法还可以用于字符串排序

import random
import math


class Solution:
    # LSD
    def radixSortLSD(self, lists, radix=10):
        """
        lists为整数列表， radix为基数
        """
        K = int(math.ceil(math.log(max(lists)+1, radix))) # 用K位数可表示任意整数
        print("bit number: ", K)

        for i in range(1, K+1):     # K次循环
            bucket = [[] for i in range(radix)]     # 不能用[[]]*radix, 否则相当于开了radix个完全相同的list对象
            for val in lists:
                bucket[int(val%(radix**i) // (radix**(i-1)))].append(val)  # 析取整数第K位数字(从低到高, LSD)
                #print("bucket: ", bucket)
            del lists[:]
            for each in bucket:
                lists.extend(each)      # 桶合并

        return lists

    # MSD
    def radixSortMSD(self, lists, d=None):
        # base case
        if len(lists) == 1 or d <= 0:
            return lists
        elif d is None:
            m = max(lists)
            d = len(str(m))

        idxs = [x * 0 for x in range(10)]   #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        temp = []
        for val in lists:
            radix = (val // 10 ** (d - 1)) % 10             # get the digit in the highest location
            #radix = (val // 10 ** (d - 1))                 # this does not work, because recursively d-1
            idxs[radix] += 1
            temp.insert(sum(idxs[:radix + 1]) - 1, val)     # to find the right index for inserting

        result = []
        for i in range(len(idxs)):
            if idxs[i] != 0:
                sub = temp[sum(idxs[:i]): sum(idxs[:i + 1])]
                print("sub: ", sub)
                result.extend(self.radixSortMSD(sub, d - 1))    # recursively

        return result

if __name__ == "__main__":
    lists = [random.randint(100, 1000) for i in range(10)]

    print("Before sorting: ", lists)
    print("After sorting(LSD): ", Solution().radixSortLSD(lists, radix=10))
    print("After sorting(MSD): ", Solution().radixSortMSD(lists, d=3))
