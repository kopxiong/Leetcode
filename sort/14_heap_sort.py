# -*- coding: utf-8 -*-
# 堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
# 堆积是一个近似完全二叉树 (Complete Binary Tree) 的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

# 堆可以分为大根堆和小根堆，这里用最大堆的情况来定义操作:
# 1. 最大堆调整(MAX_Heapify):将堆的末端子节点作调整，使得子节点永远小于父节点。这是核心步骤，在建堆和堆排序都会用到。比较i的根节点和与其所对应i的孩子节点的值。当i根节点的值比左孩子节点的值要小的时候，就把i根节点和左孩子节点所对应的值交换，当i根节点的值比右孩子的节点所对应的值要小的时候，就把i根节点和右孩子节点所对应的值交换。然后再调用堆调整这个过程，可见这是一个递归的过程。
# 2. 建立最大堆(Build_Max_Heap):将堆所有数据重新排序。建堆的过程其实就是不断做最大堆调整的过程，从len/2出开始调整，一直比到第一个节点。
# 3. 堆排序(HeapSort):移除位在第一个数据的根节点，并做最大堆调整的递归运算。堆排序是利用建堆和堆调整来进行的。首先先建堆，然后将堆的根节点选出与最后一个节点进行交换，然后将前面len-1个节点继续做堆调整的过程。直到将所有的节点取出，对于n个数我们只需要做n-1次操作。


# heap is stored in array or list
class Solution:
    def heap_sort(self, lists):
        # 创建最大堆
        for start in range((len(lists) - 2) // 2, -1, -1): # start from the last non-child node
            self.sift_down(lists, start, len(lists) - 1)

        # 堆排序
        for end in range(len(lists) - 1, 0, -1):
            lists[0], lists[end] = lists[end], lists[0]
            self.sift_down(lists, 0, end - 1)

        return lists

    # 最大堆调整
    def sift_down(self, lists, start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lists[child] < lists[child + 1]:
                child += 1
            if lists[root] < lists[child]:
                lists[root], lists[child] = lists[child], lists[root]
                root = child
            else:
                break


if __name__ == "__main__":
    lists = [9, 2, 1, 7, 6, 8, 5, 3, 4, 10]

    print(Solution().heap_sort(lists))
