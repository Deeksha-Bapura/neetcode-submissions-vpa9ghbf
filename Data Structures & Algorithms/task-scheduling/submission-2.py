from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxFreq = max(count.values())
        countMax = list(count.values()).count(maxFreq)

        time = (maxFreq - 1) * (n + 1) + countMax
        return max(len(tasks), time)