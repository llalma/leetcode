class Solution:
    def isValid(self, s: str) -> bool:
        values = {
            '(':')',
            '[':']',
            '{':'}'
        }

        open_order = ''
        for c in s:
            if c in values.keys():
                open_order+=c
            else:
                if len(open_order) == 0:
                    return False
                if values[open_order[-1]] == c:
                    open_order = open_order[0:-1]
                else:
                    return False

        return open_order == ''


class Test:
    import pytest

    @pytest.mark.parametrize("nums, expected",
                             [
                                 (']', False),
                                 ('()', True),
                                 ('()[]{}', True),
                                 ('(]', False)
                             ])
    def test(self, nums, expected):
        assert  Solution().isValid(nums) == expected