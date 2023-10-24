class Solution:
    def myAtoi(self, s: str) -> int:

        # remove whitespace
        s = s.strip()

        if len(s) == 0:
            return 0

        output_int = 0

        multiplier = 1
        if s[0] == '-':
            multiplier = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]


        for char in s:
            if char.isnumeric():
                output_int = int(char) + (output_int*10)
            else:
                break

        output_int = output_int*multiplier

        if output_int > 2**31-1:
            return 2**31-1
        elif output_int < -2**31:
            return -2**31
        return output_int






class Test:
    import pytest

    @pytest.mark.parametrize("x, expected",
                             [
                                 ("+1", 1),
                                 ("42", 42),
                                 ("-42", -42),
                                 ("4193 with words", 4193)
                             ])
    def test(self, x, expected):
        assert  Solution().myAtoi(x) == expected