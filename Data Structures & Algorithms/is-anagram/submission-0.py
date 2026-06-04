class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char_count = {}
        t_char_count = {}
        
        for cursor in s:
            if cursor in s_char_count:
                s_char_count[cursor] += 1
            else:
                s_char_count[cursor] = 1
        
        for cursor in t:
            if cursor in t_char_count:
                t_char_count[cursor] += 1
            else:
                t_char_count[cursor] = 1

        for k,v in s_char_count.items():
            if k in t_char_count and t_char_count[k] == v:
                pass
            else:
                return False
        return True

