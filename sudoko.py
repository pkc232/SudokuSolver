from math import sqrt


class SudokuSolver():

    def __init__(self, N):
        self.N = N # no of rows, no of cols, no of digits
        self.SQ_N = int(sqrt(N))
        self.VALID_SET = set(range(1,N+1))

    def print_sudoku(self, mat):
        for i in range(self.N):
            if i%self.SQ_N == 0:
                print("-"*38)
            for j in range(self.N):
                if j%self.SQ_N == 0:
                    print('|', end='  ')
                print(mat[i][j], end='  ')
            print('|')
        print("-"*38)

    def is_valid_square(self, mat, start_row, start_col):
        current_set = set()
        for i in range(start_row, start_row+self.SQ_N):
            for j in range(start_col, start_col+self.SQ_N):
                current_set.add(mat[i][j])
        return current_set == self.VALID_SET

    def check_squares(self, mat):
        is_valid_conf = True
        start_row = 0
        for i in range(self.SQ_N):
            start_col = 0
            for j in range(self.SQ_N):
                is_valid_conf &= self.is_valid_square(mat, start_row, start_col)
                start_col += self.SQ_N
            start_row += self.SQ_N
        return is_valid_conf

    def is_valid_row(self, mat, row_no):
        current_set = set()
        for i in range(self.N):
            current_set.add(mat[row_no][i])
        return current_set == self.VALID_SET

    def check_rows(self, mat):
        valid_rows = True
        for i in range(self.N):
            valid_rows&= self.is_valid_row(mat, i)
        return valid_rows
    
    def is_valid_col(self, mat, col_no):
        current_set = set()
        for i in range(self.N):
            current_set.add(mat[i][col_no])
        return current_set == self.VALID_SET
    
    def check_cols(self, mat):
        valid_cols = True
        for i in range(self.N):
            valid_cols &= self.is_valid_col(mat, i)
        return valid_cols
    
    def is_valid_configuration(self, mat):
        is_valid_conf = True
        is_valid_conf &= self.check_squares(mat)
        is_valid_conf &= self.check_rows(mat)
        is_valid_conf &= self.check_cols(mat)
        return is_valid_conf
    
    def solve_sudoku(self, mat):
        return self.is_valid_configuration(mat)