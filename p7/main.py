class Solution:
    def reverse(self, x: int) -> int:

        negative = False
        if x < 0:
            x *= -1
            negative = True

        # Calculate output value
        sum = 0
        while x:
            sum = (sum*10) + (x%10)
            x = x//10

        sum = int(sum) * (-1 if negative else 1)

        if sum > 2**31 or sum < -2**31:
            return 0

        return sum


class Test:
    import pytest

    @pytest.mark.parametrize("x, expected",
                             [
                                 (123, 321),
                                 (-123, -321),
                                 (120, 21)
                             ])
    def test(self, x, expected):
        assert  Solution().reverse(x) == expected