from unittest import TestCase
from unittest import main as unit_main
from sudoko import SudokuSolver
  
class SudokuTest(TestCase): 

    sudoku = SudokuSolver(3)

    def rotate(self, l, n):
        return l[n:] + l[:n]

    def get_sample_mat(self):
        sample_mat = []
        for i in range(self.sudoku.N):
            sample_list = list(self.sudoku.VALID_SET)
            sample_mat.append(self.rotate(sample_list, i))
        return sample_mat
    
    def test_valid_rows(self):
        mat = self.get_sample_mat()
        self.assertTrue(self.sudoku.check_rows(mat))
    
    def test_valid_cols(self):
        mat = self.get_sample_mat()
        self.assertTrue(self.sudoku.check_cols(mat))
    
    def test_valid_squares(self):
        mat = self.get_sample_mat()
        self.assertTrue(self.sudoku.check_squares(mat))
    
    def test_valid_conf(self):
        mat = self.get_sample_mat()
        self.assertTrue(self.sudoku.is_valid_configuration(mat))

if __name__ == '__main__': 
    unit_main() 
