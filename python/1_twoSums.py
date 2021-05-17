"""
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
"""

def twoSums(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i] + nums[j] == target) and (i is not j):
                return [i, j]

if __name__ == "__main__":
    nums = [3, 3]
    target = 6
    print(twoSums(nums, target)) 
