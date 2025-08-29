// 13. Roman to Integer - https://leetcode.com/problems/roman-to-integer/

#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<string, int> mapping = {
            {"I", 1}, {"IV", 4}, {"V", 5}, {"IX", 9},
            {"X", 10}, {"XL", 40}, {"L", 50}, {"XC", 90},
            {"C", 100}, {"CD", 400}, {"D", 500}, {"CM", 900},
            {"M", 1000}
        };

        int res = 0, i = 0;

        while (i < s.size()) {
            if (i + 1 < s.size()) {
                string two = s.substr(i, 2);
                // if (mapping.contains(two)) {
                if (mapping.find(two) != mapping.end()) {
                    res += mapping[two];
                    i += 2;
                    continue;
                }
            }
            string one = s.substr(i, 1);
            res += mapping[one];
            i += 1;
        }

        return res;
    }

    int romanToIntV2(string s) {
        unordered_map<char, int> mapping = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int res = 0, prev = 0;
        int i = s.size() - 1;

        while (i >= 0) {
            int curr = mapping[s[i]];
            if (curr < prev) {
                res -= curr;
            } else {
                res += curr;
            }

            prev = curr;
            i -= 1;
        }

        return res;
    }

    int romanToIntV1(string s) {
        unordered_map<char, int> mapping = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int res = 0, i = 0;
        
        while (i < s.size()) {
            int curr = mapping[s[i]];

            if (i + 1 < s.size()) {
                int nxt = mapping[s[i + 1]];

                if (curr < nxt) {
                    res += nxt - curr;
                    i += 2;
                    continue;
                }
            }

            res += curr;
            i += 1;
        }

        return res;
    }
};