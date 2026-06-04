class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_index = {}
        min_sum_index = []
        for index, num in enumerate(nums):
            sub = target - num
            if num in sum_index:
                sum_index[num].append(index)
                current_pair_idx = sum_index[num]
                if not min_sum_index:
                    min_sum_index = current_pair_idx
                elif min_sum_index and sum(min_sum_index) > sum(current_pair_idx):
                    min_sum_index = current_pair_idx
            else:
                sum_index[sub] = [index]
        return min_sum_index

        