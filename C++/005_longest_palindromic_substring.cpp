// Given a string s, find the longest palindromic substring in s.

#include <iostream>
#include <string>

// class Solution {
// public:
//     std::string longestPalindrome(std::string s) {
//         int max_length = 0;
//         std::string result, temp;
//         for (int i = 0; i < s.length(); ++i) {
//             for (int j = i; j < s.length(); ++j) {
//                 temp = s.substr(i, j);
//                 if (isPalindrome(s.substr(i, j)) && temp.length() > max_length) {
//                     result = temp;
//                     max_length = result.length();
//                 }
//             }
//         }
//
//         return result;
//     }
//     bool isPalindrome(std::string s) {
//         if (s.empty() || s.length() < 1) {
//             return false;
//         }
//         char *front, *back;
//         front = s;
//         back = s + s.length() - 1;
//         while (front < back) {
//             if (*front != *back) {
//                 return false;
//             }
//             ++front;
//             --back;
//         }
//         return true;
//     }
// };

class Solution {
public:
    std::string longestPalindrome(std::string s) {
        // base case
        if (s.length() == 0) {
            return "";
        }
        if (s.length() == 1) {
            return s;
        }

        std::string result = "";
        for (int i = 0; i < s.length(); ++i) {
            std::string temp = helper(s, i, i);
            if (temp.length() > result.length()) {
                std::cout << "odd!" << std::endl;
                result = temp;
            }

            temp = helper(s, i, i+1);
            if (temp.length() > result.length()) {
                result = temp;
                std::cout << "Even!" << std::endl;
            }
        }

        return result;
    }

    std::string helper(std::string s, int left, int right) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            left--;
            right++;
        }

        return s.substr(left+1, right-(left+1));
    }
};

int main()
{
    Solution Test;
    std::string s = "ababd";
    std::string result = Test.longestPalindrome(s);

    std::cout << "longestPalindrome: " << result << std::endl;

    return 0;
}
