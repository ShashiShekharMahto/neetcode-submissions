class Solution:
    def get_3_by_3_arr_val(self, i, j, arr):
        r = ((i//3) *3)
        c = ((j//3) *3)
        delete_idx = (((i-r)*3) + (j-c))
        idx = [
                arr[r][c], arr[r][c+1], arr[r][c+2],
                arr[r+1][c], arr[r+1][c+1], arr[r+1][c+2],
                arr[r+2][c], arr[r+2][c+1], arr[r+2][c+2]]
        del idx[delete_idx]
        return idx

    def get_col_value(self,i, j, arr):
        col = []
        for idx in range(0, 9):
            if i != idx:
                col.append(arr[idx][j])
        return col
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row_idx, row_arr in enumerate(board):
            for col_idx, col_val in enumerate(row_arr):
                if col_val != ".":
                    three_size_arr = self.get_3_by_3_arr_val(row_idx, col_idx, board)
                    col_arr = self.get_col_value(row_idx, col_idx, board)
                    if col_val in row_arr[:col_idx] or \
                    col_val in row_arr[col_idx+1 :] or \
                    col_val in three_size_arr or col_val in col_arr:
                        return False
        return True


