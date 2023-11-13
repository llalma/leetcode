    

class Solution:
     
    def _solve(self, nums: [int], low_p: int, high_p) -> int:
        
        mid_p = (low_p + high_p)//2
        shifted_p = (mid_p + self.shift)%self.length

        # Base case and is 
        if nums[shifted_p] == self.target:
            return shifted_p

        if low_p >= high_p:
            return -1

        # If target is less than current val
        if self.target < nums[shifted_p]:
            return self._solve(nums, low_p, mid_p-1)

        # If target is greater than current val
        if self.target > nums[shifted_p]:
            return self._solve(nums, mid_p+1, high_p)
    
    def find_lowest_value(self, nums: [int]) -> int:
        """
        Find the index of the lowest value in the nums array. Using binart search
        """
        p1, p2 = 0, self.length-1

        while p1 < p2:
            mid_p = (p1+p1)//2
            if nums[mid_p] > nums[p2]:
                p1 = mid_p+1
            else:
                p2 = mid_p

        return p1
        


    def search(self, nums: list[int], target: int) -> int:
        self.length = len(nums)
        self.target = target
       
        self.shift = self.find_lowest_value(nums)

        return self._solve(nums, 0, self.length-1)


class Test:
    import pytest

    @pytest.mark.parametrize("nums, target, expected",
                             [
                                 ([1, 3, 5], 5, 2),
                                 ([1], 2, -1),
                                 ([4,5,6,7,0,1,2], 0, 4), 
                                ([4,5,6,7,0,1,2], 3, -1), 
                                ([1], 0, -1),
                                ([3,1], 3, 0),
                                ([1,3], 4, -1)
                            ])
    def test(self, nums, target, expected):
        assert Solution().search(nums, target) == expected 
