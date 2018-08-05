// Given an array of size n, find the majority element.
// The majority element is the element that appears more than ⌊ n/2 ⌋ times.
// You may assume that the array is non-empty and the majority element always exist in the array.

// TODO Consider if the array is empty, it there is no majority element, or there are two majority elements.

#include <iostream>
#include <vector>
#include <unordered_map>


class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }

        std::unordered_map<int, int> counts;
        int majorityCount = nums.size() / 2;
        std::cout << "majorityCount: " << majorityCount << std::endl;

        for (int i = 0; i < nums.size(); ++i) {
            if (++counts[nums[i]] > majorityCount) {
                return nums[i];
            }

            // iterators
            for (auto i = counts.begin(); i != counts.end(); ++i) {
                std::cout << i->first << "    " << i->second << std::endl;
            }
            // Range-based for loop
            // for (auto it : counts) {
            //     std::cout << it.first << "    " << it.second << std::endl;
            // }
        }

        return 0;

    }
};

int main() {
    std::vector<int> nums = {2, 2, 1, 1, 1, 2, 2};
    Solution Test;
    std::cout << "The majority element of vector: " << Test.majorityElement(nums) << std::endl;
}
