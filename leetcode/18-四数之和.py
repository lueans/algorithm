# -*- coding: utf-8 -*-
class Solution:
    def fourSum(self, nums,target):
        nums.sort()
        res = []
        for i in range(len(nums)):

            for j in range(i+1,len(nums)):
                l = j + 1
                r = len(nums) -1
                if nums[j] == nums[j-1]:
                    continue
                while l < r:
                    cur_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if cur_sum == target:
                        res.append([nums[i] , nums[j] , nums[l] , nums[r]])
                        while (l < r and nums[l] == nums[l + 1]): l += 1
                        while (l < r and nums[r] == nums[r - 1]): r -= 1
                        l += 1
                        r -= 1
                    elif cur_sum < target:
                        l += 1
                    else:
                        r -= 1
        return res


a = Solution()
print(a.fourSum([1,0,-1,0,-2,2],0))