class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        len_arr = len(nums)
        prefix_mul = [1] * len_arr
        suffix_mul = [1] * len_arr
        prefix_mul[0] = nums[0]
        suffix_mul[-1] = nums[-1]

        for idx in range(1,len_arr):
            prefix_mul[idx] = nums[idx] * prefix_mul[idx-1]
        
        suffix_mul[len_arr-1] = nums[len_arr - 1]
        for idx in range(len_arr-2, -1, -1):
            suffix_mul[idx] = nums[idx] * suffix_mul[idx+1]
        
        output = [1]*len_arr
        output[0] = suffix_mul[1]
        output[-1] = prefix_mul[-2]

        for idx in range(1, len_arr-1):
            prefix_val = prefix_mul[idx-1]
            suffix_val = suffix_mul[idx+1]
            output[idx] = prefix_val * suffix_val
        return output
        