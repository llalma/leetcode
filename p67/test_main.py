class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1, p2 = len(a)-1, len(b)-1
        carry = 0
        output = []

        while p1 >= 0 or p2 >= 0 or carry > 0:
            
            v1 = int(a[p1] if p1 >= 0 else '0')
            v2 = int(b[p2] if p2 >= 0 else '0')
            
            temp_sum = v1 + v2 + carry

            output.append(str(temp_sum % 2))

            carry = temp_sum // 2
            p1 -= 1
            p2 -= 1

        return ''.join(output[::-1])


class TestHi:
    import pytest

    @pytest.mark.parametrize("a, b, expected",
                             [
                                 ('11', '1', '100'),
                                 ('1010', '1011', '10101'),
                             ])
    def test_1(self, a, b, expected):
        assert Solution().addBinary(a, b) == expected
