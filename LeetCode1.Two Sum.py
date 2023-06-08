class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            tmp = target - nums[i]
            if tmp in nums[i+1:]:
                ind = nums.index(tmp, i+1)
                return [i, ind]
