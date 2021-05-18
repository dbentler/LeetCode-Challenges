"""
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Ex 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Ex 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Ex 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
"""

# I'm assuming they don't want you to use the power operator.

def myPow(x: float, n: int) -> float:
    result = 1
    if n == 0:
        return result
    elif n >= 0:
        for i in range(1, n+1):
            result *= x
        return result
    elif n <= 0:
        return 1 / myPow(x, abs(n))

if __name__ == "__main__":
    num = 2.0
    pow_num = -2
    print(myPow(num, pow_num))