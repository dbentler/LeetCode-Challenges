/*
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
*/

#include <iostream>

double myPow(double& x, int& n){
    if (n == 0){
        return 1.0;
    }
    if (n > 0){
        double result = 1.0;
        for(int i = 0; i < n; i++){
            result *= x;
        }
        return result;
    }
    if (n < 0){
        // Gets the absolute value of n
        int absN = abs(n);
        // We then use recursion to get the correct answer.
        return (1 / myPow(x, absN));
    }
    return 0.0;
}

int main(){
    double num = 2;
    int pow = -2;
    std::cout << myPow(num, pow);
    return 0;
}