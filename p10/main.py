class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp_dict = {}

        def dp(i,j):

            # If it does not exist in dict create it
            if (i,j) not in dp_dict:

                # If end of pattern
                if j == len(p):
                    # Determine if also at the end of the string
                    res = len(s) == i

                else:
                    # If pattern is a match for the text or a wildcard match and not at the end of the string
                    # Basically match the first instace of the pattern before checking for *
                    first_match = i < len(s) and p[j] in {s[i], '.'}

                    #Check if next pattern is a *
                    next_pattern = p[j+1] if p[j+1:j+2] else None
                    if next_pattern and next_pattern == '*':
                        # Check using either the next pattern after the * or use the pattern just matched again
                        res = dp(i, j+2) or first_match and dp(i+1, j)

                    # Is a single pattern with no repetition using *
                    else:
                        res = first_match and dp(i+1, j+1)

                # Add to the dictionary
                dp_dict[i,j] = res

            # Return it from the dict
            return dp_dict[i,j]

        return dp(0,0)

class Test:
    import pytest

    @pytest.mark.parametrize("s, p, expected",
                             [

                                 # ("aaa", "aaaa", True),
                                 # ("aaa", "a*a", True),
                                 # ("aaba", "ab*a*c*a", False),
                                 # ("aaa", "ab*a*c*a", True),

                                 ("ab", ".*c", False),
                                 ("xiv", "xv*", False),
                                 ("mississippi", "mis*is*p*.", False),
                                 ("aab", "c*a*b", True),
                                 ("aa", "a", False),
                                 ("aa", "a*", True),
                                 ("ab", ".*", True),
                             ])
    def test(self, s, p, expected):
        assert  Solution().isMatch(s, p) == expected