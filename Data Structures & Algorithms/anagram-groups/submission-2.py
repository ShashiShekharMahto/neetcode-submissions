class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = {}
        
        for word in strs:
            w = [0]*26
            for ch in word:
                w[97- ord(ch)] += 1
            
            s = []
            for idx, v in enumerate(w):
                if v != 0:
                    s.extend([chr(97+idx), str(v)])
            s = "".join(s)

            if s in ana_map:
                ana_map[s].append(word)
            else:
                ana_map[s] = [word]
        
        return [v for _, v in ana_map.items()]