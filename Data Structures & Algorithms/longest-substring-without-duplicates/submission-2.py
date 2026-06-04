class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest_str_len = 0
        if len(s) < 2:
            return len(s)

        prev = 0
        l = 0
        str_len = len(s)
        temp_max_s = 0
        char_c = {} # character count
        while l<str_len:
            l_c = s[l]
            if l_c not in char_c:
                temp_max_s += 1
                char_c[l_c] = 1
            else:
                if temp_max_s > longest_str_len:
                    longest_str_len = temp_max_s
                
                # reset variables
                char_c = {}
                temp_max_s = 0
                prev += 1
                l = prev
                continue
            l += 1
        if temp_max_s > longest_str_len:
            longest_str_len = temp_max_s
        return longest_str_len
                
        