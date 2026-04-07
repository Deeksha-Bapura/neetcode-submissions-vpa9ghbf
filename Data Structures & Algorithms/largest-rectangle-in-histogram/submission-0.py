class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_area = max(max_area, height*width)
            stack.append(i)
        while stack:
            height = heights[stack.pop()]
            if stack:
                width = n - stack[-1] - 1
            else:
                width = n
            max_area = max(max_area, height*width)
        return max_area
