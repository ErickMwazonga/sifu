// 9. Palindrome Number - https://leetcode.com/problems/palindrome-number/description/

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int original = x;
        long reversedNum = 0;
        while (x > 0) {
            int rem = x % 10;
            reversedNum = reversedNum * 10 + rem;
            x /= 10; 
        }

        return original == reversedNum;
    }
};