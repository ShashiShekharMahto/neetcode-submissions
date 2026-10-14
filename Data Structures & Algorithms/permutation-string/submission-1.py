class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        if len1 > len2:
            return False

        s1_count = [0]*26
        s2_count = [0]*26

        a_uni = ord("a")

        for i in range(len1):
            s1_count[ord(s1[i]) - a_uni] += 1
            s2_count[ord(s2[i]) - a_uni] += 1
        
        if s1_count == s2_count:
            return True

        for i in range(len1, len2):

            s2_count[ord(s2[i]) - a_uni] += 1

            s2_count[ord(s2[i-len1]) - a_uni] -= 1

            if s1_count == s2_count:
                return True

        return False