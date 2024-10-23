class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for x in range(nums):
            if nums[0:] // x == 1:
                return True
        return False
    hasDuplicate('1, 2, 3, 4')