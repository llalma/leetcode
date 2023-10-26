class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        if len(nums) == 0:
            return 0

        p1, p2 = 0,1
        len_nums = len(nums)
        prev_value = nums[0]
        unique_count = 1

        while p1 < len_nums:

            if nums[p1] > prev_value:
                prev_value = nums[p1]
                nums[p2] = nums[p1]
                p2+=1
                unique_count+=1

            p1+=1

        return unique_count


class Test:
    import pytest

    @pytest.mark.parametrize("nums, expected1, expected2,",
                             [
                                 # ([1,1,2], 2, [1,2]),
                                 ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4]),
                             ])
    def test(self, nums, expected1, expected2):

        res1, res2 = Solution().removeDuplicates(nums)

        assert res1==expected1
        for i in range(expected1):
            assert res2[i] == expected2[i]