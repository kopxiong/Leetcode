// Given an array of integers nums sorted in ascending order,
// find the starting and ending position of a given target value.

// Your algorithm's runtime complexity must be in the order of O(log n).

// If the target is not found in the array, return [-1, -1].

#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> searchRange(std::vector<int>& nums, int target) {
        // // 1. binary search
        // std::vector<int> results = {-1, -1};
        // int low = 0;
        // int high = nums.size() - 1;
        // if (nums.empty() || nums[low] > target || nums[high] < target) {
        //     return results;
        // }
        // int mid, start, end;
        // // find the start element
        // while (low < high) {
        //     mid = (low + high) / 2;
        //     if (nums[mid] < target) low = mid + 1;
        //     else high = mid;
        // }
        // start = low;
        // high = nums.size() - 1;     // reset high to the last element
        // // find the end element
        // while (low < high) {
        //     mid = (low + high + 1) / 2;
        //     if (nums[mid] > target) high = mid - 1;
        //     else low = mid;
        // }
        // end = low;
        // if (nums[low] != target) return results;
        //
        // results = {start, end};
        //
        // return results;

        // 2. STL BinarySearch
        std::vector<int> results = {-1, -1};
        if (nums.empty() || !std::binary_search(nums.begin(), nums.end(), target)) {
            return results;
        }
        // int start = std::lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        // int end = std::upper_bound(nums.begin(), nums.end(), target) - nums.begin() - 1;
        std::pair<std::vector<int>::iterator, std::vector<int>::iterator> bounds;
        bounds = std::equal_range(nums.begin(), nums.end(), target);

        int start = bounds.first - nums.begin();
        int end = bounds.second - nums.begin() - 1;

        results = {start, end};

        return results;
    }
};


int main() {
    Solution Test;
    std::vector<int> nums = {5, 6, 6, 7, 7, 8, 8, 9};
    int target = 7;

    std::vector<int> results = Test.searchRange(nums, target);
    for (int i = 0; i < results.size(); ++i) {
        std::cout << results[i] << std::endl;
    }

    return 0;
}
