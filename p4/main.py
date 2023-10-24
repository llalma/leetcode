class Solution:

    def construct_array(self, nums1, nums2):
        res = []
        p1, p2 = 0,0

        while 1:
            v1 = nums1[p1:p1+1]
            v2 = nums2[p2:p2+1]

            if v1 and v2:
                v1, v2 = v1[0], v2[0]

                if v1<v2:
                    res.append(v1)
                    p1+=1
                else:
                    res.append(v2)
                    p2+=1
            elif v1:
                res.append(v1[0])
                p1+=1
            elif v2:
                res.append(v2[0])
                p2+=1
            else:
                return res


    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        sorted_vals = self.construct_array(nums1, nums2)

        mid_point = len(sorted_vals)/2
        if not mid_point.is_integer():
            return sorted_vals[int(mid_point)]

        return (sorted_vals[int(mid_point)-1] + sorted_vals[int(mid_point)])/2

class Test:
    import pytest

    @pytest.mark.parametrize("nums1, nums2, expected",
                             [
                                 ([], [2,3,4], 3),
                                 ([1,3], [2], 2.00000),
                                 ([1,2], [3,4], 2.50000),
                             ])
    def test(self, nums1, nums2, expected):
        assert expected == Solution().findMedianSortedArrays(nums1, nums2)