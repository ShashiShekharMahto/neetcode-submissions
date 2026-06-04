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
                char_c[l_c] = l
            else:
                # print(prev)
                if temp_max_s > longest_str_len:
                    longest_str_len = temp_max_s
                
                dup_c_idx = char_c[l_c]  # current char prev index
                reduce_temp_len = dup_c_idx - prev
                temp_max_s -= reduce_temp_len
                prev = dup_c_idx + 1
                
                temp_ch_c = {}
                for k,v in char_c.items():
                    if v >= prev:
                        temp_ch_c[k] = v
                # print(temp_ch_c)
                char_c = temp_ch_c
                char_c[l_c] = l

            l += 1
        if temp_max_s > longest_str_len:
            longest_str_len = temp_max_s
        return longest_str_len
                
        