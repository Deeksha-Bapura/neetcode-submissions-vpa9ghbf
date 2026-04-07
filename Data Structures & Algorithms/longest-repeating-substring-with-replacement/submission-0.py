class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_freq = 0
        max_len = 0
        left = 0
        freq = {}

        for right in range(n):
            freq[s[right]] = freq.get(s[right] , 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            win_len = right - left + 1
            if win_len - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
        # for i in range(n):
        #     for j in range(i,n):
        #         freq = {}
        #         max_freq = 0
        #         for c in s[i:j+1]:
        #             freq[c] = freq.get(c , 0) + 1
        #             max_freq = max(max_freq, freq[c])
        #         length = j - i + 1
        #         replacements = length - max_freq
        #         if replacements <= k :
        #             max_len = max(max_len, length)
        # return max_len
