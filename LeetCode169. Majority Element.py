class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = nums.count(nums[i])
        sorted_dict = sorted(dic.items(), key=lambda x: x[1])
        return sorted_dict[-1][0]


