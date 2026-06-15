class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or len(s)< len(t):
            return ""

        countT = {}
        countT2 = {}
        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
            countT2[ch] = 1 + countT2.get(ch, 0)
        
        t_len = len(t)
        char_cover_count = 0
        final_str_len = float("infinity")
        final_str = ""

        l = 0
        for r, ch in enumerate(s):
            if ch in countT2:

                if countT2[ch] > 0:
                    char_cover_count +=1
                countT2[ch] -= 1
                # print("1", countT2, char_cover_count)
                
                if char_cover_count >= t_len:
                    while char_cover_count >= t_len:
                        # print(l,r)
                        temp_min = r - l + 1
                        if final_str_len > temp_min:
                            # print(final_str_len, temp_min)
                            final_str_len = temp_min
                            final_str = s[l:r+1]
                        
                        if s[l] in countT2:
                            # print("3", countT2, s[l], l)
                            countT2[s[l]] += 1
                            if countT2[s[l]]>0:
                                char_cover_count -= 1
                        
                        l += 1
        
                    # print("outside while loop")
                    # print(final_str, ch)
                    # print(l,r)
                    # print(countT2)
                    # print("=====")
        if final_str:
            return final_str
        else:
            return s[l : r+1] if char_cover_count >= t_len else ""