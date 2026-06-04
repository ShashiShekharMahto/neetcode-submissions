class Solution:

    def str_char_count(self, text:str) -> dict:
        char_count_map = {}
        for c in text:
            if c in char_count_map:
                char_count_map[c] += 1
            else:
                char_count_map[c] = 1
        return char_count_map

    def isAnagram(self, s: str, t: str) -> bool:
        s_char_count_map = self.str_char_count(s)
        t_char_count_map = self.str_char_count(t)

        
        for k,v in s_char_count_map.items():
            if k not in t_char_count_map or t_char_count_map[k] != v:
                return False
        
        for k,v in t_char_count_map.items():
            if k not in s_char_count_map or s_char_count_map[k] != v:
                return False

        return True
                
            
        
        