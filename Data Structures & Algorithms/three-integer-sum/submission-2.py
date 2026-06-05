class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        has_map = {}
        for idx, num in enumerate(nums):
            if num in has_map:
                has_map[num].append(idx)
            else:
                has_map[num] = [idx]
        

        zero_map = {}
        arr_sum = []
        
        for i1 in range(0, len(nums)):
            n1 = nums[i1]
            for i2 in range(i1+1, len(nums)):
                n2 = nums[i2]
                diff = 0 - (n1 + n2)
                if n1 == n2 and diff == n1:
                    if diff in has_map and len(has_map[diff]) > 2:
                        d = [n1, n2, diff]
                        d.sort()
                        # print(d)
                        arr_3 = ",".join(str(c) for c in d)
                        if arr_3 not in zero_map:
                            zero_map[arr_3] = 1
                            arr_sum.append(d)
                elif (diff == n1 or diff == n2) and diff in has_map and len(has_map[diff]) > 1:
                    d = [n1, n2, diff]
                    d.sort()
                    # print(d)
                    arr_3 = ",".join(str(c) for c in d)
                    if arr_3 not in zero_map:
                        zero_map[arr_3] = 1
                        arr_sum.append(d)
                elif diff != n1 and diff != n2 and diff in has_map:
                    d = [n1, n2, diff]
                    d.sort()
                    # print(d)
                    arr_3 = ",".join(str(c) for c in d)
                    if arr_3 not in zero_map:
                        zero_map[arr_3] = 1
                        arr_sum.append(d)
        
        return arr_sum
        
                    



        
        