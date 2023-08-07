# -*- coding: utf-8 -*-

#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = len(nums)-1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    print(i,l,r)
                    res.append([nums[i],nums[l],nums[r]])
                    # res.add([nums[i],nums[l],nums[r]])
                    while (l < r and nums[l] == nums[l+1]): l += 1
                    while (l < r and nums[r] == nums[r-1]): r -= 1
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return res


a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))
