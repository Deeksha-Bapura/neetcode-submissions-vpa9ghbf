class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        window_count = {}

        have = 0
        need = len(t_count)

        res = [-1, -1]
        res_len = float('inf')
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char,0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l,r]
                    res_len = r - l + 1

                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
        # min_len = float('inf')
        # result = ""

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         substring = s[i : j + 1]
        #         window_count = Counter(substring)

        #         valid = True
        #         for char in t_count:
        #             if window_count[char] < t_count[char]:
        #                 valid = False
        #                 break
        #         if valid:
        #             if len(substring) < min_len:
        #                 min_len = len(substring)
        #                 result = substring
        # return result