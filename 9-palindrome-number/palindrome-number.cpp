class Solution {
public:
    bool isPalindrome(long int x) {
        if (x < 0) {
            return false;
        }

        long int original = x;
        long int reverse = 0;

        while (x > 0) {
            long int digit = x % 10;
            reverse = reverse * 10 + digit;
            x = x / 10;
        }

        return original == reverse;
    }
};