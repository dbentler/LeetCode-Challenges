/*
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
*/

#include <iostream>
#include <string>

bool isPalindrome(const int& x){
    if(x < 0){ // Any negative number is not a palindrome
        return false;
    }
    int y;
    // Reversing the number.
    std::string strNum = std::to_string(x);
        // Swaps individual chars in a string in place.
        int len = strNum.length();
        int n = len - 1;
        for(int i = 0; i < (len/2); i++){
            std::swap(strNum[i], strNum[n]);
            n--;
        }
        // Sets y to the reversed string, which is converted to an int
        y = stoi(strNum);
    if (x == y){
        return true;
    } else {
        return false;
    }
}

int main(){
    int num = 121;
    std::cout << isPalindrome(num);
    return 0;
}