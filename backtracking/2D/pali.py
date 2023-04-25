class Palindrome:

    def first(self, word: str) -> str:
        return word[0]

    def last(self, word: str) -> str:
        return word[-1]

    def middle(self, word: str) -> str:
        return word[1:-1]

    def is_pal(self, _str: str) -> bool:
        # base case -> check for a small unit of the input i.e. empty string or a single character
        if len(_str) <= 1:
            return True

        # additional base case -> if the last and first don't match(True)
        # NOTE: checking if they match then returning True is incorrect
        # there could be unmatching inner characters e.g bulb
        if self.first(_str) != self.last(_str):
            return False

        return self.is_pal(self.middle(_str))

    def main(self) -> None:
        conditions: dict[str, bool] = {
            'redivider': True,
            'mama': False,
            'amma': True,
            'madam': True,
            'kenya': False
        }

        for input, output in conditions.items():
            assert self.is_pal(input) == output


palidrome = Palindrome()
palidrome.main()
