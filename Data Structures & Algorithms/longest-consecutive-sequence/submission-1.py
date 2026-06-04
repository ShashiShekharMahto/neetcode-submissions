class Solution:

    def find_seq_length(self, num:int, has_map: dict) -> int:
        
        run = True
        count = 1
        while run:
            if num-1 in has_map:
                count += 1
                num = num-1
            else:
                run = False
        return count
            

    def longestConsecutive(self, nums: List[int]) -> int:
        has_map = {}
        visited_num = {}

        for idx, num in enumerate(nums):
            if num not in visited_num:
                visited_num[num] = 1
                if num-1 in has_map:
                    has_map[num-1] = [num]
                if num+1 in has_map:
                    has_map[num] = [num+1]
                else:
                    has_map[num] = []
        
        num_without_map = [] # this list will have the any possible sequence larget values
        for k,v in has_map.items():
            if not v:
                num_without_map.append(k)

        # print(has_map)
        # print(num_without_map)
        max_val = 0
        for num in num_without_map:
            value = self.find_seq_length(num, has_map)
            max_val = max(max_val, value)
        
        return max_val


        