class Solution:

    def calc_row(self, start_index, s, offset_1, offset_2):


        offset_1_version = True
        i = start_index

        output_str = ''
        while 1:

            res = s[i:i+1]
            res = res[0] if res else None
            if not res:
                return output_str

            output_str += res
            i += offset_1 if offset_1_version else offset_2
            offset_1_version = not offset_1_version


    def convert(self, s: str, numRows: int) -> str:

        if len(s) == numRows or numRows==1:
            return s

        output_str = ''
        for i in range(numRows):

            offset_1 = (numRows-i) * 2 - 2
            if offset_1 == 0:
                offset_1 = numRows * 2 - 2
            offset_2 = (i+1) * 2 - 2
            if offset_2 == 0:
                offset_2 = numRows * 2 - 2

            output_str += self.calc_row(i, s, offset_1, offset_2)

        return output_str









class Test:
    import pytest

    @pytest.mark.parametrize("s, num_rows, expected",
                             [
                                 ('AB', 1, 'AB'),
                                 ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
                                 ('ABCD', 3, 'ABDC'),
                                 ('ABCD', 2, 'ACBD'),
                                 ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
                                 ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
                                 ('A', 1, 'A')
                             ])
    def test(self, s, num_rows, expected):
        assert  Solution().convert(s, num_rows) == expected