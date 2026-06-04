class Solution:
    def get_next_ch_right_direction(self, s, i, j):
        while i <= j and not s[i].isalnum():
            i += 1
        return i
    
    def get_next_ch_left_direction(self, s, i, j):
        while j >= i and not s[j].isalnum():
            j -= 1
        return j

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        if len(s) == 1:
            return True
        print(i, j)
        while i <= j:
            i = self.get_next_ch_right_direction(s, i, j)
            j = self.get_next_ch_left_direction(s, i, j)
            if i > j:
                return True
            print(i, j, s[i], s[j])
            if s[i].lower() != s[j]:
                return False
            i += 1
            j -= 1
        return True
        