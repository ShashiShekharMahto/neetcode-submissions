class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occur_count = {}
        for num in nums:
            num_occur_count[str(num)] = num_occur_count.get(str(num), 0) + 1
        
        
        num_occur_count = sorted(
            num_occur_count.items(), key = lambda item:item[1], reverse=True)
        
        most_k = []
        for idx,elem in enumerate(num_occur_count):
            if idx  == k:
                break
            else:
                most_k.append(elem[0])
        return most_k
        
        # if k == 1:
        #     v_ = 0
        #     k_ = 0
        #     for k,v in num_occur_count.items():
        #         if v >v_ :
        #             k_ = k
        #     return [k_]

        
        # most_k = []
        # min_v = 0
        # max_v = 0

        # k_count = 0
        # most_k_dict = {}
        # # find min and max in first k values
        # for num_k,v in num_occur_count.items():
        #     if k_count < num_k:
        #         k_count += 1
        #         most_k_dict[num_k] = v

        # for num_k,v in num_occur_count.items():
        #     if k_count == 0:

        #     else:
        #         k_count -= 1


         
        
        
        
        