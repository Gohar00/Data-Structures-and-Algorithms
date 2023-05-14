class Solution:
    def checkIfExist(self, nums: List[int]) -> bool:
        extra_arr = [2*i for i in nums]
        for i in range(0,len(nums)):
            if nums[i] in extra_arr and i != extra_arr.index(nums[i]):
                return True
        return False