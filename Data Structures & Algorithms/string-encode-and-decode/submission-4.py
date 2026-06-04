class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for elem in strs:
            elem_len = len(elem)
            encode_str = f"{encode_str}{elem_len}#{elem}"
        return encode_str
        
    def get_str_len(self, s, idx):
        str_len = ""
        while s[idx] != '#':
            str_len += s[idx]
            idx += 1
        return int(str_len), len(str_len)


    def decode(self, s: str) -> List[str]:
        decoded_list = []

        if len(s) == 0:
            return []
        if len(s)==2:
            return [""]
        
        s_len = len(s)
        idx = 0
        str_len, ch_len = self.get_str_len(s, idx)
        idx = idx + ch_len + 1
        # 2#qa3#qwe
        while idx < s_len:
            decode_str = ""
            for cursor in range(idx, idx+str_len):
                char = s[cursor]
                decode_str = f"{decode_str}{char}"
            decoded_list.append(decode_str)
            idx += str_len
            if idx < s_len:
                str_len, ch_len = self.get_str_len(s, idx)
                idx = idx + ch_len + 1
        if str_len == 0:
            decoded_list.append("")
        return decoded_list