class Solution:
    def longestValidParentheses(self, s:str) -> int:
        # Logic is to store the last opening bracket 
        # in the stack. Then can use that to keep track of what is 
        # open and closed and just calculate longests value per run

        longest_found = 0
        stack = [-1]

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)

            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    longest_found = max(longest_found,
                                        i-stack[-1])
        return longest_found

class Test:
    import pytest

    @pytest.mark.parametrize("s,expected",
                             [
                                 ("(()", 2),
                                 (")()())", 4),
                                 ("", 0),
                                ("(()(", 2)
                            ])
    def test(self, s, expected):
        assert Solution().longestValidParentheses(s) == expected 
