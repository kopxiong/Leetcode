# 插入排序 (Insertion Sort) 的工作原理是通过构建有序序列，对于未排序数据，
# 在已排序序列中从后向前扫描，找到相应位置并插入。

class Solution(object):
    def insertionSort(self, arr):
        n = len(arr)

        for i in range(n):
            j = i - 1
            key = arr[i]
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j = j - 1
            arr[j+1] = key

        return arr

if __name__ == '__main__':
    lists = [32, 64, 1, 4, 98, 23, 8, 46, 10, 90]

    print(Solution().insertionSort(lists))
