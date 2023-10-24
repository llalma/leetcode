class Solution:
    def find_volume(self, heights, i1, i2):
        distance = abs(i2 - i1)
        return min(heights[i1], heights[i2]) * distance

    def maxArea(self, height: list[int]) -> int:
        if len(height) == 0:
            return 0

        p1, p2 = 0, len(height)-1
        found_max = 0

        while p1 < p2:

            found_max = max(found_max, self.find_volume(height, p1, p2))
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1


        return found_max







class Test:
    import pytest

    @pytest.mark.parametrize("height, expected",
                             [

                                 ([2,3,10,5,7,8,9], 36),
                                 ([1,8,6,2,5,4,8,3,7], 49),
                                 ([1,1], 1)
                             ])
    def test(self, height, expected):
        assert  Solution().maxArea(height) == expected