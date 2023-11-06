class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return 1


class TestHi:
    import pytest

    @pytest.mark.parametrize("s, expected", [("(()", 2), (")()())", 4), ("", 0)])
    def test_hi(self, s, expected):
        assert Solution().longestValidParentheses(s) == expected
