#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums,target) :
        res = 0
        d = abs(nums[0] + nums[1] + nums[2])
        nums.sort()
        for i in range(len(nums)):
            l = i + 1;
            r = len(nums) - 1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                cur_d = target - ( cur_sum )
                if abs(cur_d) < d:
                    d = abs(cur_d)
                    res = cur_sum
                if cur_d == 0:
                    return cur_sum
                elif cur_d<0:
                    l += 1
                else:
                    r -= 1
        return res

a = Solution()
print(a.threeSumClosest([-1,2,1,-4],1))