class Solution:
    def max_discount_tags(self, tags: list[int],) -> int:
        sum_pos_nums = sum(filter(lambda x: x > 0, tags))
        if not sum_pos_nums % 2:
            return sum_pos_nums

        smallest_pos_odd_num = min(filter(lambda x: x > 0 and x % 2, tags))
        return sum_pos_nums - smallest_pos_odd_num

class SolutionV2:

    def max_discount_tags(self, tags: list[int],) -> int:
        return self.dp(tags, idx=0, memo={})

    def is_even(self, num: int) -> bool:
        return not num % 2

    def dp(self, tags: list[int], idx: int, memo: dict) -> int:
        if idx >= len(tags):
            return 0

        if idx in memo:
            return memo[idx]

        # take
        take = self.dp(tags, idx + 1, memo) + tags[idx]

        # leave
        leave = self.dp(tags, idx + 1, memo)

        ans = 0
        if self.is_even(take) and self.is_even(leave):
            ans = max(take, leave, tags[idx])
        elif self.is_even(take):
            ans = max(take, tags[idx])
        elif self.is_even(leave):
            ans = max(leave, tags[idx])

        memo[idx] = ans
        return ans

class SolutionV3:

    def max_discount_tags(self, tags: list[int]) -> int | float:
        return self.dp(tags, idx=0, even_sum=0, memo={})

    def dp(self, tags: list[int], idx: int, even_sum: int, memo: dict) -> int | float:
        if idx >= len(tags):
            return even_sum if even_sum % 2 == 0 else float('-inf')

        if (idx, even_sum) in memo:
            return memo[(idx, even_sum)]

        # take
        take = self.dp(tags, idx + 1, even_sum + tags[idx], memo)

        # leave
        leave = self.dp(tags, idx + 1, even_sum, memo)

        memo[(idx, even_sum)] = max(take, leave)
        return memo[(idx, even_sum)]


soln = Solution()
soln2 = SolutionV2()
soln3 = SolutionV3()

print(soln.max_discount_tags([2, 3, 6, -5, 10, 1, 1]))
print(soln2.max_discount_tags([2, 3, 6, -5, 10, 1, 1]))
print(soln3.max_discount_tags([2, 3, 6, -5, 10, 1, 1]))
