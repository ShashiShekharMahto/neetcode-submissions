class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for idx,text in enumerate(strs):
            v = str(9999)
            if text:
                v = ",".join(str(ord(ch)) for ch in text)
            strs[idx] = v
        f_str = ";".join(text for text in strs)
        # print(f_str)
        
        return f_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        strs_list = s.split(";")
        for idx, text in enumerate(strs_list):
            text = text.split(",")
            if len(text) == 1 and int(text[0]) == 9999:
                strs_list[idx] = ""
            else:
                v = "".join(chr(int(num)) for num in text)
                strs_list[idx] = v
        return strs_list
