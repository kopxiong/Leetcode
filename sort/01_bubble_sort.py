# 冒泡排序 (Bubble Sort) 是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，
# 如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
# 这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

class Solution(object):
    def bubbleSort(self, arr):
        n = len(arr)

        # after each iteration, the last element is the maximum
        for i in range(n-1):
            flat = True
            for j in range(1, n-1-i):
                if arr[j] > arr[j+1]:
                    # swap, doesn't use temp because Python passes by reference (pointer in C++)
                    # shallow copy vs copy.deepcopy in Python
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    flag = False

            # if no exchange, return arr or lists
            if flag:
                return arr

        return arr

if __name__ == '__main__':
    lists = [32, 64, 1, 4, 98, 23, 8, 46, 10, 90]

    print(Solution().bubbleSort(lists))
