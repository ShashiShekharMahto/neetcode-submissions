class Solution:
    def number_exist(self, nums:List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                return True, mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid-1
        return False, -1

    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        l = 0
        r = nums_len - 1
        while l < r:
            mid = l + (r-l) //2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        # after this while loop will get the index of lowest value which "l"
        v, idx = self.number_exist(nums[:l], target)
        if v:
            return idx
        else:
            v, idx = self.number_exist(nums[l:], target)
            if v:
                return l + idx
            return -1
