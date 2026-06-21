class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        
        num_len = len(nums)
        s,e = 0, num_len-1
        mid = (s+e)//2

        while s<=e:
            mid_val = nums[mid]
            mid_l = nums[mid-1]
            mid_r = nums[mid+1]
            if mid_l < mid_val > mid_r:
                return mid_r
            elif mid_l > mid_val < mid_r:
                return mid_val
            elif mid_val < mid_r and mid_r > nums[s]:
                s = mid
                mid = (s+e)//2
            elif mid_val < mid_r and mid_r < nums[s]:
                e = mid
                mid = (s+e) // 2
        