class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower().strip()
        l = 0
        r = len(s) - 1

        while l<r:
            ch_l = s[l]
            while not ch_l.isalnum() and l < r:
                l += 1
                ch_l = s[l]
            
            ch_r = s[r]
            while not ch_r.isalnum() and l<r:
                r -= 1
                ch_r = s[r]
            
            if ch_l != ch_r:
                return False
            if ch_l == ch_r:
                l += 1
                r -= 1
        
        return True

        