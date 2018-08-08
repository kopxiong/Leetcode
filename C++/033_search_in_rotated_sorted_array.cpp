// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
// (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
// You are given a target value to search. If found in the array return its index, otherwise return -1.

// You may assume no duplicate exists in the array.
// Your algorithm's runtime complexity must be in the order of O(log n).

#include <iostream>
#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        if (nums.empty())
            return -1;
        int low = 0;
        int high = nums.size() - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            // std::cout << "mid: " << mid << std::endl;
            if (nums[mid] == target)
                return mid;

            // rotation in the right part
            if (nums[mid] > nums[high]) {
                if (nums[mid] > target && nums[high] < target)
                    high = mid - 1;
                else
                    low = mid + 1;
            }

            // rotation in the left part
            else if (nums[mid] < nums[low]) {
                if (nums[mid] < target && nums[low] > target)
                    low = mid + 1;
                else
                    high = mid - 1;
            }

            // no rotation case, just normal binary search
            else {
                if (nums[mid] > target)
                    high = mid - 1;
                else
                    low = mid + 1;
            }
        }
        return -1;
    }
};


int main() {
    Solution Test;
    std::vector<int> nums = {4, 5, 6, 7, 8, 9, 0, 1, 2};
    int target = 3;

    std::cout << "the index is: " << Test.search(nums, target) << std::endl;

    return 0;
}
