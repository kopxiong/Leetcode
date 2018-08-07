// Time complexity: O(nlogn)

#include <iostream>
#include <utility>      // swap

class HeapSort {
public:
    // O(logn)
    void heapify(int arr[], int start, int end) {
        int root = start;
        while (true) {
            int child = 2 * root + 1;
            if (child > end) break;
            if ((child + 1 <= end) && (arr[child] < arr[child + 1])) {
                child += 1;
            }
            if (arr[child] > arr[root]) {
                std::swap(arr[child], arr[root]);
                root = child;
            }
            else break;
        }
    }

    int* heapSort(int arr[], int n) {
        // start from the last non-leaf node:
        for (int start = (n-2)/2; start >= 0; --start) {
            heapify(arr, start, n-1);
        }

        // swap the root with the last node, then heapify recursively: O(n)
        for (int end = n-1; end >= 0; --end) {
            std::swap(arr[0], arr[end]);
            heapify(arr, 0, end-1);
        }

        return arr;
    }
};

int main() {
    HeapSort Test;
    int arr[10] = {9, 2, 1, 7, 6, 8, 5, 3, 4, 10};
    int* result = Test.heapSort(arr, 10);

    // print out the sorted array
    for (int i = 0; i < 10; ++i) {
        std::cout << *(result + i) << std::endl;
    }

    return 0;
}
