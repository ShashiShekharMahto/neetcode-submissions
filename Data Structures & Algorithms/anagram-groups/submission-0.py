class Solution:

    def character_count(self, s:str):
        chr_count = {}

        for num in range(97,123):
            chr_count[chr(num)] = 0
        for c in s:
            chr_count[c] = chr_count.get(c, 0) + 1
        
        str_count = ''.join(f"{k}{v}" for k, v in chr_count.items() if v != 0)
        return str_count

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        unique_str_count = {}
        for idx, s in enumerate(strs):
            str_count = self.character_count(s)
            if str_count in unique_str_count:
                unique_str_count[str_count].append(s)
            else:
                unique_str_count[str_count] = [s]
        
        output = []
        for k,v in unique_str_count.items():
            output.append(v)
        return output
        
        