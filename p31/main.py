def _solve(i, s, words_count, word_len, s_len, substring_len):

    sub_string_count = 0

    while i < s_len:

        # get the current words
        word = s[i:i+word_len]
        if word in words_count and words_count[word] > 0:
            words_count[word] -= 1

            sub_string_count += word_len
            if sub_string_count == substring_len:
                return True

            i += word_len

        # Word is not in so exit
        else:
            return False


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:

        output = []
        word_len = len(words[0])
        s_len = len(s)
        substring_len = word_len*len(words)

        # words count
        words_count = {}
        for word in words:
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1

        # Loop over each starting index
        for i in range(len(s) - (len(words)*word_len-1)):
            if _solve(i, s, words_count.copy(), word_len, s_len, substring_len):
                output.append(i)

        return list(set(output))
class Test:
    import pytest

    @pytest.mark.parametrize("s, words, expected",
                             [
                                 ('abarfoothefoobarman', ["foo","bar"], [1,10]),
                                 ('wordgoodgoodgoodbestword', ["word","good","best","word"], []),
                                 ('barfoofoobarthefoobarman', ["bar","foo","the"], [6, 9, 12]),
                             ])
    def test(self, s, words, expected):
        assert sorted(Solution().findSubstring(s, words)) == sorted(expected)