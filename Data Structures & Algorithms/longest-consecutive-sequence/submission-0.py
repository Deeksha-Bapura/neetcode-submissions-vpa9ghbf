class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                curr = num

                while curr + 1 in num_set:
                    curr += 1
                    length += 1
                    
                longest = max(longest, length)
        return longest
            


        # if not nums:
        #     return 0
        
        # nums.sort()
        # max_c = 1
        # curr_c = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         continue
        #     elif nums[i] == nums[i - 1] + 1:
        #         curr_c += 1
        #     else:
        #         curr_c = 1
        #     max_c = max(max_c,curr_c)
        # return max_c