class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        list_len = len(nums)
        s = 0
        e = list_len - 1
        m = (s+e)//2
        if nums[s] == target:
            return s
        if nums[e] == target:
            return e

        while(s != m and e !=m ):
            val = nums[m]
            if val == target:
                return m
            elif val > target:
                e = m
                m = (s+e)//2
            else:
                s = m
                m = (s+e)//2
        if nums[m] == target:
            return m
        return -1