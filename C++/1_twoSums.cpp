/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Ex 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Ex 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Ex 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
*/

#include <iostream>
#include <vector>

std::vector<int> twoSum(std::vector<int>& nums, int& target){
    std::vector<int> answer;
    for (int i = 0; i < nums.size(); i++){
        for (int j = 0; j < nums.size(); j++){
            if((nums[i] + nums[j] == target) && (nums[i] != nums[j])){
                answer = {i, j};
                return answer;
            }
        }
    }
    std::cout << "No solution, returning null vector" << std::endl;
    return answer; // Returns a null vector if no solution was found.
}

int main(){
    std::vector<int> foo = {2, 7, 11, 15};
    int target = 9;
    
    std::vector<int> solution = twoSum(foo, target);
    for(auto val : solution){
        std::cout << val << " ";
    }

    return 0;
}