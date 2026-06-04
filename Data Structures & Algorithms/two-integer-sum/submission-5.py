class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        for idx1 in range(len(nums)-1):
            num1 = nums[idx1]
            for idx2 in range(idx1+1, len(nums)):
                num2 = nums[idx2]
                if num1 + num2 == target:
                    return [idx1, idx2]
                