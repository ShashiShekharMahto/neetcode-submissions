class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_len = len(matrix)
        c_len = len(matrix[0])
        total_len = r_len * c_len
        s = 0
        e = total_len - 1
        while s <= e:
            m = (s+e)//2
            r = m // c_len
            c = ((m+1) % c_len) - 1
            val = matrix[r][c]

            if val == target:
                return True
            elif val < target:
                s = m+1
            else:
                e = m-1
        return False

        