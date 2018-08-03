// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


// class Solution {
// public:
//     std::string longestCommonPrefix(std::vector<std::string>& strs) {
//         if (strs.empty()) {
//             return "";
//         }
//         std::string prefix = strs[0];
//         for (int i = 0; i < strs.size(); ++i) {
//             for (int j = 0; j < prefix.size(); ++j) {
//                 if (strs[i][j] != prefix[j]) {
//                     prefix.resize(j);
//                     break;
//                 }
//             }
//         }
//         return prefix;
//     }
// };


// Divide and conquer
class Solution {
public:
    std::string longestCommonPrefix(std::vector<std::string>& strs) {
        if (strs.empty()) {
            return "";
        }

        return divideAndConquer(strs, 0, strs.size()-1);
    }

    std::string divideAndConquer(std::vector<std::string>& strs, int l, int r) {
        if (l == r) {
            return strs[l];
        }
        else {
            int mid = (l + r) / 2;
            std::string left = divideAndConquer(strs, l, mid);
            std::string right = divideAndConquer(strs, mid+1, r);

            return commonPrefix(left, right);
        }
    }

    // combine
    std::string commonPrefix(std::string left, std::string right) {
        int min_len = std::min(left.size(), right.size());
        for (int i = 0; i < min_len; ++i) {
            if (left[i] != right[i]) {
                return left.substr(0, i);
            }
        }
        return left.substr(0, min_len);
    }
};

int main()
{
    Solution Test;
    std::vector<std::string> strs = {"leetcode", "leet", "leexiao"};

    std::cout << "The longest common prefix is: " << Test.longestCommonPrefix(strs) << std::endl;

    return 0;
}
