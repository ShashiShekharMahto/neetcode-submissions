class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_map = {}
        t_map = {}

        for ch in s:
            s_map[ch] = 1 + s_map.get(ch, 0)
        for ch in t:
            t_map[ch] = 1 + t_map.get(ch, 0)
        
        for k,v in s_map.items():
            if k not in t_map or t_map[k] != v:
                return False
        
        return True
        