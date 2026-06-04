class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        three_sum = []

        for idx, value in enumerate(nums):
            remains = 0 - value
            lookup_map = {}
            for j in range(idx+1, len(nums)):
                value2 = nums[j]

                if value2 in lookup_map:
                    arr = [
                        value, lookup_map[value2],  value2]
                    arr.sort()
                    if arr not in three_sum:
                        three_sum.append(arr)
                    
                lookup_map[remains-value2] = value2
        return three_sum


        