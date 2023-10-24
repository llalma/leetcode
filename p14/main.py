class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        pointer = 0
        current_prefix = ''
        while 1:
            for i, s in enumerate(strs):
                current_char = s[pointer] if s[pointer:pointer+1] else None

                if current_char is None:
                    if len(current_prefix) == pointer:
                        return current_prefix
                    return current_prefix[0:-1]

                # If first word of new pointer just add the char
                if i == 0:
                    current_prefix += current_char

                else:
                    if current_char != current_prefix[-1]:
                        return current_prefix[0:-1]

            # Move to next postion
            pointer += 1



class Test:
    import pytest

    @pytest.mark.parametrize("strs, expected",
                             [
                                 (["a"], "a"),
                                 (["ab", "a"], "a"),
                                 (["flower","flow","flight"], "fl"),
                                 (["dog","racecar","car"], ""),
                             ])
    def test(self, strs, expected):
        assert  Solution().longestCommonPrefix(strs) == expected