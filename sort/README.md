# Sorting algorithms:

Implementation of all kinds of sorting algorithms using Python3

Talking about the computational complexity and stability

https://zhuanlan.zhihu.com/p/21839027


Stable algorithms:

01. Bubble sort (冒泡排序): O(n^2)

02. Insertion sort (插入排序): O(n^2)

03. Merge sort (归并排序): O(n log n), 需要 O(n) 额外空间

04. Counting sort (计数排序): O(n+k), 需要O(n+k)额外空间

05. Binary tree sort (二叉树排序): O(n log n), worst case: O(n^2); 需要O(n)额外空间

06. 桶排序(bucket sort): O(n); 需要O(k)额外空间

07. 原地归并排序: O(n log^2 n)

08. 基数排序(radix sort): O(n·k); 需要O(n)额外空间

09. 块排序(block sort): O(n log n)


Unstable algorithms:

11. Selection sort (选择排序): O(n^2)

12. Shell sort (希尔排序): O(n log^2 n)

13. Quick sort (快速排序): partition-exchange sort (划分交换排序); 最优: O(n log n); 最坏: O(n^2)

14. Heap sort (堆排序): O(n log n)

15. Clover排序算法(Clover sort): O(n)期望时间, O(n^2)最坏情况

16. 梳排序: O(n log n)

17. 平滑排序(smooth sort): O(n log n)

18. 内省排序(introsort): O(n log n)

19. 耐心排序(patience sort): O(n log n + k)最坏情况时间, 需要额外的O(n + k)空间,也需要找到最长的递增子序列
（longest increasing subsequence）


Divide and Conquer (分治法):

1. Quick sort

2. Merge sort
