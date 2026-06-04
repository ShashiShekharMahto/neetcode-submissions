class Solution:

    def char_count(self, text: str) -> str:
        char_count = [0]*26
        for ch in text:
            num = ord(ch)
            char_count[num-97]  = char_count[num-97] + 1
        
        return "".join(f"{chr(97+idx)}{v}" for idx,v in enumerate(char_count) if v!=0)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        unique_text = {}
        for text in strs:
            char_count_str = self.char_count(text)
            if char_count_str in unique_text:
                unique_text[char_count_str].append(text)
            else:
                unique_text[char_count_str] = [text]
        
        return[v for k,v in unique_text.items()]
