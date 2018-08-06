// Determine whether an integer is a palindrome.
// An integer is a palindrome when it reads the same backward as forward.

#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    bool isPalindrome(int x) {
        // base case, -1, 0, 10, etc.
        if (x < 0 || (x != 0 && x % 10 == 0)) return false;

        std::vector<int> digits;
        for (; x; x/=10) {
            digits.push_back(x % 10);
        }
        std::vector<int> copy_digits;
        copy_digits = digits;

        std::reverse(digits.begin(), digits.end());

        return copy_digits == digits;
    }

    //     // odd case
    //     if (digits.size() % 2 != 0) {
    //         int mid = digits.size() / 2;
    //         return helper(digits, mid, mid);
    //     }
    //     if (digits.size() % 2 == 0) {
    //         int mid = digits.size() / 2;
    //         return helper(digits, mid-1, mid);
    //     }
    //     return false;
    // }
    //
    // bool helper(const std::vector<int> &digits, int left, int right) {
    //     while (left >= 0 && right < digits.size()) {
    //         if (digits[left] != digits[right]) {
    //             return false;
    //         }
    //         left--;
    //         right++;
    //     }
    //     return true;
    // }
};

int main() {
    int x = 0;
    Solution Test;
    if (Test.isPalindrome(x)) {
        std::cout << x << " is a Palindrome number!" << std::endl;
    }
    else {
        std::cout << x << " is not a Palindrome number!" << std::endl;
    }

    return 0;
}
