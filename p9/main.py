class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x > 0 and x%10 == 0):
            return False

        reverse_val = 0
        # Calculate reverse int
        while x > reverse_val:
            reverse_val = (reverse_val*10)+x%10
            x //= 10

        return x == reverse_val or x == reverse_val//10


class Test:
    import pytest

    @pytest.mark.parametrize("x, expected",
                             [
                                 (121, True),
                                 (-121, False),
                                 (10, False),
                             ])
    def test(self, x, expected):
        assert  Solution().isPalindrome(x) == expected