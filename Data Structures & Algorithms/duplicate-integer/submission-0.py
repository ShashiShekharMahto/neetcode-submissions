class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        num_len = len(nums)
        i = 0
        while i < num_len-1:
            if nums[i] == nums[i+1]:
                return True
            i += 1
        return False
         