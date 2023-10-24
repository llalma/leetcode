class Solution:
    def threeSumClosest(self, nums:list[int], target: int) -> int:

        """Just try eveything"""
        nums.sort()

        closest = float('inf')
        for i in range(len(nums)-2):
            l,r = i+1, len(nums)-1

            while l<r:
                current_sum = nums[l]+nums[r]+nums[i]

                if current_sum < target:
                    l+=1
                else:
                    r-=1

                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

        return closest




class Test:
    import pytest

    @pytest.mark.parametrize("nums, target, expected",
                             [
                                 ([4,0,5,-5,3,3,0,-4,-5], -2, -2),
                                 ([-1,2,1,-4], 1, 2),
                                 ([0,0,0], 1, 0),
                             ])
    def     test(self, nums, target, expected):
        assert  Solution().threeSumClosest(nums, target) == expected