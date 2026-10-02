class Solution:
    def get_times_to_eat(self, piles, v):
        s = 0
        for p in piles:
            d = p // v
            r = 1 if p % v else 0

            s += d
            s += r
        return s
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        if len(piles) == h:
            return max_val
        
        s = 1

        k = float('inf')
        while s <= max_val:
            m= (s+max_val) // 2
            temp_k = self.get_times_to_eat(piles, m)

            if temp_k <= h and m < k:
                k = m
                max_val = m -1
            if temp_k > h:
                s = m + 1
            print(s, max_val)
            print()
        return k
        

        