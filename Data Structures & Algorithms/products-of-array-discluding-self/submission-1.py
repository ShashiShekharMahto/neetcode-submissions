class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mul = [1]
        for idx in range(1, len(nums)):
            num = nums[idx-1]
            left_mul.append(num * left_mul[idx-1])
        
        # print(nums)
        # print(left_mul)
        
        right_mul = [1]*(len(nums))
        # print(right_mul)
        for idx in range(len(nums)-2, -1, -1):
            consider_idx = idx+1
            # print(consider_idx)
            right_mul[idx] = nums[consider_idx]*right_mul[consider_idx]
            # print(right_mul)
        # print("---",right_mul)
        final_array = []
        for idx in range(len(nums)):
            val = left_mul[idx] * right_mul[idx]
            final_array.append(val)
        return final_array
        