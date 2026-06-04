class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_count = {}

        for num in nums:
            if num in element_count:
                element_count[num] += 1
            else:
                element_count[num] = 1
        
        freq_bucket = []
        for num in nums:
            freq_bucket.append([])
        
        for key,v in element_count.items():
            freq_bucket[v-1].append(key)
        
        values = []
        # print(freq_bucket)

        for key in range(len(freq_bucket)-1, -1, -1):
            v = freq_bucket[key]
            remaining = k - len(values)
            if not remaining:
                return values
            if v:
                values.extend(v[:remaining])
            # print(values)
        return values

            