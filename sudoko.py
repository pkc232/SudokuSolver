from math import sqrt


class SudokuSolver():

    def preprocess_mat(self, mat):
        if isinstance(mat, str):
            lst = mat.split()
            mat = [[int(x) for x in lst[i*9:i*9+9]] for i in range(0,9)]
            return mat
        elif isinstance(mat, list):
            return mat
        else:
            raise ValueError("Sudoku can be inputted only as string or list of lists.")

    def __init__(self, N, mat):
        self.N = N # no of rows, no of cols, no of digits
        self.SQ_N = int(sqrt(N))
        self.VALID_SET = set(range(1,N+1))
        self.mat = self.preprocess_mat(mat)

    def print_sudoku(self):
        for i in range(self.N):
            if i%self.SQ_N == 0:
                print("-"*38)
            for j in range(self.N):
                if j%self.SQ_N == 0:
                    print('|', end='  ')
                print(self.mat[i][j], end='  ')
            print('|')
        print("-"*38)

    def is_valid_square(self, start_row, start_col):
        current_set = set()
        for i in range(start_row, start_row+self.SQ_N):
            for j in range(start_col, start_col+self.SQ_N):
                current_set.add(self.mat[i][j])
        return current_set == self.VALID_SET

    def check_squares(self):
        is_valid_conf = True
        start_row = 0
        for i in range(self.SQ_N):
            start_col = 0
            for j in range(self.SQ_N):
                is_valid_conf &= self.is_valid_square(start_row, start_col)
                start_col += self.SQ_N
            start_row += self.SQ_N
        return is_valid_conf

    def is_valid_row(self, row_no):
        current_set = set()
        for i in range(self.N):
            current_set.add(self.mat[row_no][i])
        return current_set == self.VALID_SET

    def check_rows(self):
        valid_rows = True
        for i in range(self.N):
            valid_rows&= self.is_valid_row(i)
        return valid_rows
    
    def is_valid_col(self, col_no):
        current_set = set()
        for i in range(self.N):
            current_set.add(self.mat[i][col_no])
        return current_set == self.VALID_SET
    
    def check_cols(self):
        valid_cols = True
        for i in range(self.N):
            valid_cols &= self.is_valid_col(i)
        return valid_cols
    
    def is_valid_configuration(self):
        is_valid_conf = True
        is_valid_conf &= self.check_squares()
        is_valid_conf &= self.check_rows()
        is_valid_conf &= self.check_cols()
        return is_valid_conf
    


    def solve_sudoku(self, mat):
        return self.is_valid_configuration()