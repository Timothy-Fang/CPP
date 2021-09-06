#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        ##for i in (slow,nums):
        print ('数组长度为 :', slow)
        print ('当前数组:', nums) 
        print ('当前数组:', nums[0:slow])
        a = nums[slow-1] 
        return slow

List=[0,1,1,2,2,3]

so = Solution()

so.removeDuplicates(List)


# @lc code=end

