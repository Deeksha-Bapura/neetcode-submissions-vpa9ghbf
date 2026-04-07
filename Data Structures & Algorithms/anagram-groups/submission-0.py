class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            sort = tuple(counts)
            if sort in m:
                m[sort].append(word)
            else:
                m[sort] = [word]
        return list(m.values())        