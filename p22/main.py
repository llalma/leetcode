class Solution:

    def _solve(self, input:[str], opening_count:int, close_count:int):

        temp1=[]
        temp2=[]

        if len(input[0]) == 2*self.target:
            return input

        if opening_count < self.target:
            temp1 = self._solve([v+'(' for v in input], opening_count+1, close_count)
        if close_count < opening_count:
            temp2 = self._solve([v + ')' for v in input], opening_count, close_count+1)

        return temp1+temp2


    def generateParenthesis(self, n: int) -> list[str]:
        """ Idea is to use recursion for each possibility"""
        self.target = n
        x = self._solve(['('], 1, 0)
        return x





class Test:
    import pytest

    @pytest.mark.parametrize("n, expected",
                             [
                                 ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
                                 (2, ["()()", "(())"]),
                                 (3,  ["((()))","(()())","(())()","()(())","()()()"]),
                             ])
    def test(self, n, expected):
        assert sorted(Solution().generateParenthesis(n)) == sorted(expected)
