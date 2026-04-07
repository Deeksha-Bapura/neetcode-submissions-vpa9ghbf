class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if temperatures[i] < temperatures[j]:
        #             result[i] = j - i
        #             break
        # return result
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result