class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        total_water = 0
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]

        while l < r:
            if height[l] <= height[r]:
                l += 1
                left_max = max(left_max, height[l])
                total_water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total_water += right_max - height[r]
        return total_water

        # for i in range(1, n - 1):
        #     left_max = 0
        #     right_max = 0

        #     for l in range(i + 1):
        #         left_max = max(left_max, height[l])
        #     for r in range(i, n):
        #         right_max = max(right_max, height[r])

        #     water_at_i = min(left_max, right_max) - height[i]
        #     if water_at_i > 0:
        #         total_water += water_at_i
        # return total_water
