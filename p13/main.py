class Solution:

    def __init__(self):
        self.conversion_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }

    def romanToInt(self, s: str) -> int:

        """ Calculate sum in reverse"""
        sum = 0
        biggest_seen= 0

        for c in s[::-1]:

            val = self.conversion_dict[c]

            # Set the new biggest value if it is bigger
            if val > biggest_seen:
                biggest_seen = val

            if val < biggest_seen:
                sum-=val
            else:
                sum+=val

        return sum



class Test:
    import pytest

    @pytest.mark.parametrize("s, expected",
                             [

                                 ('III', 3),
                                 ('LVIII', 58),
                                 ('MCMXCIV', 1994),
                             ])
    def test(self, s, expected):
        assert  Solution().romanToInt(s) == expected