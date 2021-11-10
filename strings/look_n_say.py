'''
38. Count and Say
https://leetcode.com/problems/count-and-say/
https://en.wikipedia.org/wiki/Look-and-say_sequence

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so
that each group is a contiguous section all of the same character.
Then for each group, say the number of characters, then say the character.
To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:
Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

Another Explanation
1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ... 

To generate a member of the sequence from the previous member, read off the digits of the previous member,
counting the number of digits in groups of the same digit. For example:

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 is read off as "one 1, one 2, then two 1s" or 111221.
111221 is read off as "three 1s, two 2s, then one 1" or 312211.
'''


class Solution:

    def nextNumber(self, s):
        res = []
        s = str(s)
        i, n = 0, len(s)

        while i < n:
            count = 1

            while i + 1 < n and s[i] == s[i+1]:
                count += 1
                i += 1

            res.append(str(count) + s[i])
            i += 1

        return ''.join(res)

    def countAndSay(self, n):
        s = '1'

        if n == 1:
            return s

        for i in range(n-1):
            s = self.nextNumber(s)

        return s


soln = Solution()
soln.nextNumber(1) == "1"
soln.nextNumber(4) == "1211"
