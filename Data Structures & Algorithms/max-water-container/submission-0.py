class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_capacity = 0
        for idx, bar_h1 in enumerate(heights):
            for idx2 in range(idx+1, len(heights)):
                bar_distance = idx2-idx
                bar_h2 = heights[idx2]
                min_bar_heights = min(bar_h2, bar_h1)
                capacity = min_bar_heights * bar_distance
                if capacity > max_capacity:
                    max_capacity = capacity
        return max_capacity
        