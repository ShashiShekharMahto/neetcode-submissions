class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for idx, num in enumerate(nums):
            if num not in num_map:
                num_map[num] = [idx]
            else:
                num_map[num].append(idx)
        
        for idx, num in enumerate(nums):
            sec = target - num
            if sec == num and sec in num_map and len(num_map[sec]) > 1:
                return [idx, num_map[sec][1]]
            elif sec != num and sec in num_map:
                return [idx, num_map[sec][0]]
        
