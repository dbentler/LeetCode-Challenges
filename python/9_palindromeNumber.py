"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Ex 1:
Input: x = 121
Output: true

Ex 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Ex 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Ex 4:
Input: x = -101
Output: false

Constraints:
-2^31 <= x <= 2^31 - 1
"""
def isPalindrome(x: int) -> bool:
    if (x >= 2**31) or (x <= -2**31):
        return False
    else:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

if __name__ == "__main__":
    num = 10
    print(isPalindrome(num))
