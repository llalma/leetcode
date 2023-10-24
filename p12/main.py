class Solution:
    def __init__(self):
        self.ones = ['I', 'X', 'C','M']
        self.fives = ['V', 'L','D']
    def intToRoman(self, num: int) -> str:

        """Create the string in reverse order"""
        output_str = ''

        current_depth = 0
        while num > 0:

            v = num%10

            if v in (1,2,3):
                output_str = (self.ones[current_depth] * v) + output_str
            elif v == 4:
                output_str = (self.ones[current_depth]+self.fives[current_depth]) + output_str
            elif v in (5,6,7,8):
                output_str = (self.fives[current_depth] + self.ones[current_depth]*(v - 5)) + output_str
            elif v == 9:
                output_str = self.ones[current_depth] + self.ones[current_depth+1] + output_str

            current_depth += 1
            num //= 10

        return output_str






class Test:
    import pytest

    @pytest.mark.parametrize("num, expected",
                             [

                                 # (4, 'IV'),
                                 # (3, 'III'),
                                 # (58, 'LVIII'),
                                 (1994, 'MCMXCIV'),
                             ])
    def test(self, num, expected):
        assert  Solution().intToRoman(num) == expected