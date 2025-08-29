#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numToIdx;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (numToIdx.find(complement) != numToIdx.end()) {
                return {numToIdx[complement], i};
            }
            numToIdx[nums[i]] = i;
        }
        return {};
    }
};