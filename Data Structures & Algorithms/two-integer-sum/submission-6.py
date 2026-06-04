class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_map = {}
        for idx, num in enumerate(nums):
            if num in number_map:
                number_map[num].append(idx)
            else:
                number_map[num] = [idx]
        
        for idx, num in enumerate(nums):
            diff  = target - num
            if diff == num and diff in number_map and len(number_map[diff]) > 1:
                idx_val = number_map[diff]
                return idx_val[:2]
            if diff!= num and diff in number_map:
                return [idx, number_map[diff][0]]
        
        return []
