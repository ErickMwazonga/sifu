// https://leetcode.com/problems/find-the-middle-index-in-array/description/

#include <vector>

using namespace std;

class Solution {
public:
    int findMiddleIndex(vector<int>& nums) {
        int n = nums.size();
        vector<int> lefts(n + 1, 0);
        vector<int> rights(n + 1, 0);

        int i = 0, j = n - 1;

        while (i < n) {
            lefts[i + 1] = lefts[i] + nums[i];
            rights[j] = rights[j + 1] + nums[j];
            ++i;
            --j;
        }

        // check middle index
        for (int k = 0; k < n; ++k) {
            if (lefts[k] == rights[k + 1]) {
                return k;
            }
        }

        return -1;
    }

    int findMiddleIndex2(vector<int>& nums) {
        int n = nums.size();
        vector<int> lefts = {0};
        vector<int> rights = {0};  // we'll reverse later)

        int i = 0, j = n - 1;

        while (i < n) {
            lefts.push_back(lefts.back() + nums[i]);
            rights.push_back(rights.back() + nums[j]);

            ++i;
            --j;
        }

        reverse(rights.begin(), rights.end()); // aligns rights[i + 1] with lefts[i]

        for (int i = 0; i < n; ++i) {
            if (lefts[i] == rights[i + 1]) {
                return i;
            }
        }

        return -1;
    }

    int findMiddleIndex3(vector<int>& nums) {
        int n = nums.size();
        vector<int> lefts(n + 1, 0);
        vector<int> rights(n + 1, 0);

        for (int i = 0; i < n; ++i) {
            lefts[i + 1] = lefts[i] + nums[i];
            rights[n - 1 - i] = rights[n - i] + nums[n - 1 - i];
        }

        for (int i = 0; i < n; ++i) {
            if (lefts[i] == rights[i + 1]) {
                return i;
            }
        }

        return -1;
    }
};