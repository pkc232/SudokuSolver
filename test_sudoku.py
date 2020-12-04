from unittest import TestCase
from unittest import main as unit_main
from sudoko import SudokuSolver
  
class SudokuTest(TestCase): 

    sudoku = SudokuSolver(9)

    def rotate(self, l, n):
        return l[n:] + l[:n]

    def get_sample_mat_valid(self):
        sudoku =    """
                    7	2	6	4	9	3	8	1	5
                    3	1	5	7	2	8	9	4	6
                    4	8	9	6	5	1	2	3	7
                    8	5	2	1	4	7	6	9	3
                    6	7	3	9	8	5	1	2	4
                    9	4	1	3	6	2	7	5	8
                    1	9	4	8	3	6	5	7	2
                    5	6	7	2	1	4	3	8	9
                    2	3	8	5	7	9	4	6	1
                    """
        lst = sudoku.split()
        mat = [[int(x) for x in lst[i*9:i*9+9]] for i in range(0,9)]
        return mat
    
    def get_sample_mat_invalid(self):
        sample_mat = []
        for i in range(self.sudoku.N):
            sample_list = list(self.sudoku.VALID_SET)
            sample_mat.append(self.rotate(sample_list, i))
        return sample_mat
    
    def test_valid_rows(self):
        mat = self.get_sample_mat_valid()
        self.assertTrue(self.sudoku.check_rows(mat))
    
    def test_valid_cols(self):
        mat = self.get_sample_mat_valid()
        self.assertTrue(self.sudoku.check_cols(mat))
    
    def test_valid_squares(self):
        mat = self.get_sample_mat_valid()
        self.assertTrue(self.sudoku.check_squares(mat))
    
    def test_valid_conf(self):
        mat = self.get_sample_mat_valid()
        self.assertTrue(self.sudoku.is_valid_configuration(mat))

if __name__ == '__main__': 
    unit_main() 
