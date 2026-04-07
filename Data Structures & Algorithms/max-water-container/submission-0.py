class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxim = 0
        l = 0
        r = n - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            curr = width * height

            maxim = max(curr,maxim)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1 
        return maxim
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         width = j - i
        #         height = min(heights[i], heights[j])
        #         curr = width * height
        #         if curr > maxim:
        #             maxim = curr
        # return maxim