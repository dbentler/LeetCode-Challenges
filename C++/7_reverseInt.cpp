/*
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
*/

#include <iostream>
#include <string>

int reverse(int& x){
    if(x == 0){
        return x;
    }
    if(x > 0){
        // Converts int to a string representation
        std::string strNum = std::to_string(x);
        // Swaps individual chars in a string in place.
        int len = strNum.length();
        int n = len - 1;
        for(int i = 0; i < (len/2); i++){
            std::swap(strNum[i], strNum[n]);
            n--;
        }
        // Sets x to the reversed string, which is converted to an int
        x = stoi(strNum);
        return x;
    }
    if(x < 0){
        // Create a local copy of the absolute value of x
        int absX = std::abs(x);
        // We get the reversed version of absX via recursion. Then we make it negative.
        x = (-1 * reverse(absX));
        return x;
    }
    return 0;
}

int main(){
    // Assumming number is always 32-bit
    int num = -123;
    std::cout << num << std::endl;
    reverse(num);
    std::cout << num << std::endl;
    return 0;
}