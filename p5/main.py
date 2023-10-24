class Solution:

    def check_1(self, s, i):
        p1,p2 = i, i
        while s[p1:p1 + 1] == s[p2:p2 + 1] and s[p1:p1 + 1] != [] and p1 >= 0 and p2 <= len(s):
            p1 -= 1
            p2 += 1
        return s[p1+1:p2]

    def check_2(self, s, i):
        p1,p2 = i-1,i
        while s[p1:p1 + 1] == s[p2:p2 + 1] and s[p1:p1 + 1] != [] and p1 >= 0 and p2 <= len(s):
            p1 -= 1
            p2 += 1
        return s[p1+1:p2]

    def longestPalindrome(self, s: str) -> str:

        longest_found = ''

        for i in range(0, len(s)):

            res = self.check_1(s,i)
            if len(res) > len(longest_found):
                longest_found = res

            res = self.check_2(s,i)
            if len(res) > len(longest_found):
                longest_found = res

        return longest_found





class Test:
    import pytest

    @pytest.mark.parametrize("s, expected",
                             [
                                 ('a', 'a'),
                                 ('abad', 'aba'),
                                 ('aacabdkacaa', 'aca'),
                                 ('bcdabadd', 'dabad'),
                                 ('babad', 'bab'),
                                 ('cbbd', 'bb'),
                             ])
    def test(self, s, expected):
        assert  Solution().longestPalindrome(s) == expected