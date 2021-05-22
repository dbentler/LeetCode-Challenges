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