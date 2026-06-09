class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        str_len = len(s)
        if str_len < 2:
            return str_len
        
        l,r = 0,0
        char_idx_map = {}
        max_len = 0
        while r < str_len:
            ch = s[r]

            if ch not in char_idx_map:
                char_idx_map[ch] = r
            else:
                temp_max_len = r-l
                max_len = max(max_len, temp_max_len)
                temp_l = char_idx_map[ch] + 1 #cbbcd
                l = max(temp_l, l)
                char_idx_map[ch] = r
            r += 1
        
        temp_max_len = r-l
        max_len = max(max_len, temp_max_len)
        return max_len




        