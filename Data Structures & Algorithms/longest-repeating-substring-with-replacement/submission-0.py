class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count_map = {}


        l = 0
        max_ch_count = 0
        final_count = 0

        for r in range(len(s)):
            char_count_map[s[r]] = 1 + char_count_map.get(s[r], 0)
            max_ch_count = max(max_ch_count, char_count_map[s[r]])

            while (r - l + 1) - max_ch_count > k:
                char_count_map[s[l]] -= 1
                l += 1
            
            final_count = max(final_count, r-l+1)
        return final_count

                
        