class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        