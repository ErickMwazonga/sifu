// https://leetcode.com/problems/find-the-highest-altitude/

#include <vector>

using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> altitudes(gain.size() + 1);
        altitudes[0] = 0;
        int highest = 0;

        for (int i = 0; i < gain.size(); ++i) {
            altitudes[i + 1] = altitudes[i] + gain[i];
            if (altitudes[i + 1] > highest) {
                highest = altitudes[i + 1];
            }
        }

        return highest;
    }
};
