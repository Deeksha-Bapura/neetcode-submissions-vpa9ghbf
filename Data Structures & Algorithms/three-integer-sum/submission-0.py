class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res 

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         for k in range(j + 1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = tuple(sorted([nums[i],nums[j],nums[k]]))
        #                 res.add(triplet)
        # return list(res)