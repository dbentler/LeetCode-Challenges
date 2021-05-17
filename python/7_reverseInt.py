"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Ex 1:
Input: x = 123
Output: 321

Ex 2:
Input: x = -123
Output: -321

Ex 3:
Input: x = 120
Output: 21

Ex 4:
Input: x = 0
Output: 0

Constraints:
-2^31 <= x <= 2^31 - 1
"""


def reverse(x):
    solution = 0
    if x == 0:
        return solution
    elif x < 0:
        x = abs(x)
        solution = (-1 * int(str(x)[::-1]))
        if solution < (-2**31):
            return 0
        else:
            return solution
    else:
        solution = int(str(x)[::-1])
        if solution > (2**31):
            return 0
        else:
            return solution

if __name__ == "__main__":
    number = -123
    print(reverse(number))