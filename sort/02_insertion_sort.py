# Insertion sorting algorithm

class Solution(object):
    def insertionSort(self, arr):
        n = len(arr)

        for i in range(n-1):
            j = i - 1
            key = arr[i]
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j = j -1
            arr[j+1] = key

        return arr

if __name__ == '__main__':
    lists = [32, 64, 1, 4, 98, 23, 8, 46, 10, 90]

    print(Solution().insertionSort(lists))
