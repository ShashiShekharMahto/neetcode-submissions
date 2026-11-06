class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique_num = set(nums)
        longest = 0

        for num in unique_num:
            if num-1 not in unique_num:
                length = 1
                while num + length in unique_num:
                    length += 1
                
                longest = max(length, longest)
        
        return longest
        