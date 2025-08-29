// https://leetcode.com/problems/running-sum-of-1d-array/

#include <vector>

using namespace std;

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> sums(nums.size());
        sums[0] = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            sums[i] = sums[i - 1] + nums[i];
        }
        return sums;
    }

    vector<int> runningSum2(vector<int>& nums) {
        vector<int> sums;
        for (int i = 0; i < nums.size(); ++i) {
            if (i == 0) {
                sums.push_back(nums[i]);
            } else {
                sums.push_back(sums[i - 1] + nums[i]);
            }
        }

        return sums;
    }
};