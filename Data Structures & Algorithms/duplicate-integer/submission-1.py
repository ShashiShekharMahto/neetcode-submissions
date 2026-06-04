class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx in range(len(nums) - 1):
            if  nums[idx] == nums[idx+1]:
                return True
        return False
        