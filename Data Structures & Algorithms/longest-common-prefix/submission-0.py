class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)

        prefix = ""
        for i in range(min_len):
            char = strs[0][i]
            for word in strs[1:]:
                if word[i] != char:
                    return prefix
            prefix += char
        return prefix