class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        num_len = len(nums)
        pre_mul= [1]*num_len
        suf_mul = [1]*num_len
        
        for i in range(1, num_len):
            pre_mul[i] = nums[i-1] * pre_mul[i-1]
        
        for i in range(num_len-2, -1, -1):
            suf_mul[i] = nums[i+1] * suf_mul[i+1]
        
        res = []
        for i,j in zip(pre_mul, suf_mul):
            res.append(i*j)
        return res