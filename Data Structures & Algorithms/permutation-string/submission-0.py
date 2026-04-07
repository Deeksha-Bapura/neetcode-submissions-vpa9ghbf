class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)
        if m > n:
            return False
        freq1 = {}
        freq2 = {}
        left = 0
        for c in s1:
            freq1[c] = freq1.get(c , 0) + 1
        for right in range(n):
            freq2[s2[right]] = freq2.get(s2[right] , 0) + 1
            if right - left + 1 > m:
                freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left += 1
            if right - left + 1 == m:
                if freq1 == freq2:
                    return True
        return False
        # for i in range(len(s2) - len(s1) + 1):
        #     window = s2[i : len(s1) + i]
        #     if sorted(window) == sorted(s1):
        #         return True
        # return False