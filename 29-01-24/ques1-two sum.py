"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i,v in enumerate(nums):
            r=target-v
            if r in d:
                return[d[r],i]
            d[v] = i
        return[]

c=Solution()
n1=[2,7,11,15]
t1 = 9
print(c.twoSum(n1,t1))

n2=[3,2,4]
target2 = 6
print(c.twoSum(n2,target2))
n3=[3,3]
target3 = 6
print(c.twoSum(n3,target3))
        
