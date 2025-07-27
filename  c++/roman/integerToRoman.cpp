// 12. Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        vector<pair<int, string>> mapping = {
            {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
            {100, "C"},  {90, "XC"},  {50, "L"},  {40, "XL"},
            {10, "X"},   {9, "IX"},   {5, "V"},   {4, "IV"}, {1, "I"}
        };

        string res;
        for (const auto& [value, symbol] : mapping) {
            int tokens = num / value;
            while (tokens > 0) {
                res += symbol;
                --tokens;
            }
            num %= value;
        }
        return res;
    };

    string intToRoman2(int num) {
        vector<pair<int, string>> mapping = {
            {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
            {100, "C"},  {90, "XC"},  {50, "L"},  {40, "XL"},
            {10, "X"},   {9, "IX"},   {5, "V"},   {4, "IV"}, {1, "I"}
        };

        string res;
        for (const auto& [value, symbol] : mapping) {
            while (num >= value) {
                res += symbol;
                num -= value;
            }
        }

        return res;
    }
};