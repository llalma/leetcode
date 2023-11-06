class Solution:
    def mySqrt(self, x: int) -> int:
        current_num = 1

        while 1:
            if current_num * current_num > x:
                return current_num - 1

            current_num += 1


class TestHi:
    import pytest

    @pytest.mark.parametrize("x, expected",
                             [
                                 (4, 2),
                                 (8, 2),
                                 (9, 3),
                             ])
    def test_hi(self, x, expected):
        assert Solution().mySqrt(x) == expected
