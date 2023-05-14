class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums1 = []
        for i in nums:
            nums1.append(i ** 2)
        return sorted(nums1)
