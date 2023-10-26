class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        len_nums = len(nums)
        if len_nums == 0:
            return 0

        p1 = 0

        count_valid = lambda x: sum(v!=val for v in x)

        while p1<len_nums:

            if nums[p1] == val:

                # Find first p2 value above p1 that is not val
                p2 = p1
                while nums[p2] == val:
                    p2+=1
                    if p2 >= len_nums:
                        return count_valid(nums)

                # Swap p2 into p1
                nums[p1] = nums[p2]
                nums[p2] = val

            p1 += 1

        return count_valid(nums)


class Test:
    import pytest

    @pytest.mark.parametrize("nums, val, expected1, expected2",
                             [
                                 ([3,2,2,3], 3, 2, [2,2]),
                             ])
    def test(self, nums, val, expected1, expected2):
        res = Solution().removeElement(nums, val)
        assert res == expected1
        nums.sort()
        for i, v in enumerate(expected2):
            assert v == nums[i]