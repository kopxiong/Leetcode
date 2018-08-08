// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
// (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

// You are given a target value to search.
// If found in the array return true, otherwise return false.

#include <iostream>
#include <vector>

class Solution {
public:
    bool search(std::vector<int>& nums, int target) {
        if (nums.empty())
            return false;
        int low = 0;
        int high = nums.size() - 1;

        while (low <= high) {
            int mid = (low + high) / 2;
            // std::cout << "mid: " << mid << std::endl;
            if (nums[mid] == target)
                return true;

            // remove all duplicates from the right direction
            else if (nums[low] == nums[high])
                high--;
            // rotation in the right part
            else if (nums[mid] > nums[high]) {
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
        return false;
    }
};


int main() {
    Solution Test;
    std::vector<int> nums = {1, 3, 1, 1, 1, 1, 1};
    int target = 3;

    bool flag = Test.search(nums, target);
    if (flag)
        std::cout << "the target is found!" << std::endl;
    else
        std::cout << "the target is not found!" << std::endl;

    return 0;
}
