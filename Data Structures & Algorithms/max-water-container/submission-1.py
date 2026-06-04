class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_capacity = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            bar_diff = right- left
            min_bar = min(heights[left], heights[right])
            capacity = min_bar * bar_diff
            if capacity > max_capacity:
                max_capacity = capacity

            if min_bar == heights[left]:
                left += 1
            else:
                right -= 1
        
        return max_capacity
        