class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
        # n = len(s)
        # max_len = 0
        # for i in range(n):
        #     for j in range(i,n):
        #         seen = set()
        #         valid = True
        #         for k in range(i, j + 1):
        #             if s[k] in seen:
        #                 valid = False
        #                 break
        #             seen.add(s[k])
        #         if valid:
        #             max_len = max(max_len, j - i + 1)
        # return max_len