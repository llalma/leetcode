class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        seen_dict = {}
        output = []

        # Add all single values to the seen dict for lookup
        for i, num in enumerate(nums):
            if num not in seen_dict:
                seen_dict[num] = [i]

        # Add all comvination of values into the dict
        for i, num1 in enumerate(nums[0:-1]):
            for j, num2 in enumerate(nums[i+1:], i+1):
                complement = -1 * (num1 + num2)
                if complement in seen_dict:
                    complement_index = seen_dict[complement].copy()

                    # Filter out any indicies which already being used
                    if i in complement_index:
                        complement_index.remove(i)
                    if j in complement_index:
                        complement_index.remove(j)

                    if len(complement_index) > 0:
                        for ci in complement_index:
                            output.append([nums[i],nums[j],nums[ci]])

        # Remove any duplicates
        de_duplicated = set(tuple(sorted(t)) for t in output)

        # Convert indicies to values
        return [list(v) for v in de_duplicated]

class Test:
    import pytest

    @pytest.mark.parametrize("nums, expected",
                             [
                                 ([-7,-4,-6,6,4,-6,-9,-10,-7,5,3,-1,-5,8,-1,-2,-8,-1,5,-3,-5,4,2,-5,-4,4,7],[[-10,2,8],[-10,3,7],[-10,4,6],[-10,5,5],[-9,2,7],[-9,3,6],[-9,4,5],[-8,2,6],[-8,3,5],[-8,4,4],[-7,-1,8],[-7,2,5],[-7,3,4],[-6,-2,8],[-6,-1,7],[-6,2,4],[-5,-3,8],[-5,-2,7],[-5,-1,6],[-5,2,3],[-4,-4,8],[-4,-3,7],[-4,-2,6],[-4,-1,5],[-3,-2,5],[-3,-1,4],[-2,-1,3],[-1,-1,2]]),
                                 ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
                                 ([0,1,1], []),
                                 ([0,0,0], [[0,0,0]]),
                             ])
    def test(self, nums, expected):
        assert  sorted(Solution().threeSum(nums)) == expected