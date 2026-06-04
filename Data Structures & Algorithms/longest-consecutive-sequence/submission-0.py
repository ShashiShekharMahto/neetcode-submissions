class Solution:
    def get_destination_key(self, chain_map, num):
        while not isinstance(chain_map[num], list):
            num = chain_map[num]
        return num
    
    def longestConsecutive(self, nums: List[int]) -> int:
        chain_map = {}
        for num in nums:
            if num in chain_map:
                continue
            if num-1 in chain_map:
                value = self.get_destination_key(
                                        chain_map, num-1)
                chain_map[num] = chain_map[value]
                chain_map[num].append(num)
                chain_map[value] = num
                # print(chain_map, value)
            if num + 1 in chain_map:
                value = self.get_destination_key(
                                        chain_map, num+1)
                if num not in chain_map:
                    chain_map[num] = [num]

                chain_map[num].extend(chain_map[value])
                chain_map[value] = chain_map[num]
                chain_map[num] = value
                # print(chain_map,value)
            if num not in chain_map:
                chain_map[num] = [num]
                # print(chain_map)
            
        # print(chain_map)
    
        max_consec_len = 0
        for k,v in chain_map.items():
            if isinstance(v, list):
                list_len = len(v)
                if list_len > max_consec_len:
                    max_consec_len = list_len
        return max_consec_len

                
        