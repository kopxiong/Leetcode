# Bubble sorting algorithms

class Solution(object):
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(n-1-i):
                if arr[j] > arr[j+1]:
                    temp     = arr[j]
                    arr[j]   = arr[j+1]
                    arr[j+1] = temp

        return arr

if __name__ == '__main__':
    lists = [32, 64, 1, 4, 98, 23, 8, 46, 10, 90]

    print(Solution().bubbleSort(lists))
