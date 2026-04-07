class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            elif nums[mid] > target:
                right -= 1
        return -1