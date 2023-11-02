def reverse(arr):
    bPoint, n = -1, len(arr)
    for i in range(n - 2, -1, -1):
        if arr[i] >= arr[i + 1]: continue  # Skip the non-increasing sequence
        bPoint = i  # Got our breakpoint
        for j in range(n - 1, i, -1):  # again traverse from end
            if arr[j] > arr[bPoint]:  # Search an element greater the element present at the breakPoint.
                arr[j], arr[bPoint] = arr[bPoint], arr[j]  # Swap it
                break  # We just need to swap once
        break  # Break this loop too
    arr[bPoint + 1:] = reversed(arr[bPoint + 1:])

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Find next largets number
        """

        if len(nums) < 2:
            return 0

        # Find first non increasing digit from right
        i = len(nums)-2
        while nums[i+1] <= nums[i] and i >= 0:
            i-=1

        # Only flip a digit in the middle of the nums array if, the array is non-increasing
        breakpoint_index = i
        breakpoint_val = nums[i]
        if breakpoint_index>=0:
            # Iterate from RHS in section right of breakpoint, Find the first instance of number bigger than breakpoint
            i = len(nums)-1
            while i > breakpoint_index:
                if nums[i] > breakpoint_val:
                      break
                i-=1
            nums[i], nums[breakpoint_index] = nums[breakpoint_index], nums[i]

        # Reverse the part right of breakpoint_index
        left = breakpoint_index + 1
        right = len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

        return nums

class Test:
    import pytest

    @pytest.mark.parametrize("nums, expected",
                             [
                                 ([1,1], [1,1]),
                                 ([5,1,1], [1,1,5]),
                                 ([1,2], [2,1]),
                                 ([1,2,4,3], [1,3,2,4]),
                                 ([1,2,3], [1,3,2]),
                                 ([3,2,1], [1,2,3]),
                                 ([1,1,5], [1,5,1]),
                                 ([1,3,2], [2,1,3]),
                             ])
    def test(self, nums, expected):
        assert Solution().nextPermutation(nums) == expected