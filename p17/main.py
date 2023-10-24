class Solution:

    def solve(self, digits, index):
        output = []

        if len(digits) <= index:
            return []

        temp = self.solve(digits, index+1)

        for char in self.mapping[digits[index]]:
            if len(temp) > 0:
                # Apply each char to the mappings
                output += list(map(lambda v: char + v, temp))
            else:
                output.append(char)

        return output

    def letterCombinations(self, digits: str) -> list[str]:
        self.mapping = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','i','h'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }

        return self.solve(digits, 0)


class Test:
    import pytest

    @pytest.mark.parametrize("digits, expected",
                             [
                                 ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
                                 ("", []),
                                 ("2", ["a","b","c"])
                             ])
    def test(self, digits, expected):
        assert  Solution().letterCombinations(digits) == expected