def _solve(nums, lower, upper, target):
    # Get middle index-ish
    mid_index = int((upper-lower) / 2)+lower

    if lower == upper:
        return upper

    if nums[mid_index] > target:
        return _solve(nums, lower, mid_index, target)
    elif nums[mid_index] < target:
        return _solve(nums, mid_index + 1, upper, target)
    else:
        return mid_index

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """Binary search time"""
        return _solve(nums, 0, len(nums), target)



class Test:
    import pytest

    @pytest.mark.parametrize("nums, target, expected",
                             [
                                 ([1,3,5,6], 5, 2),
                                 ([1,3,5,6], 2, 1),
                                 ([1,3,5,6], 7, 4),
                             ])
    def test(self, nums, target, expected):
        assert Solution().searchInsert(nums, target) == expected