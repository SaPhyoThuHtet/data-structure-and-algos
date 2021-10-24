class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Rotate Image 90 Degree
        Idea: Iterate each cell and replace with cell at (len(matrix)-column-1, row)
        
        0, 0  => 2 (len(n)-1-column),0(row)
        0, 1  => 1, 0
        0, 2  => 0, 0
        """
        if (len(matrix)<2):
            return matrix
        
        dict_matrix = {}
        
        for row in range(0, len(matrix)):
            for column in range(0, len(matrix[0])):                
                if (len(matrix)-column-1, row) in dict_matrix:
                    dict_matrix[(row, column)] = matrix[row][column]
                    matrix[row] [column] = dict_matrix[(len(matrix)-column-1, row)]
                else:
                    dict_matrix[(row, column)] = matrix[row][column]
                    matrix[row] [column] = matrix[len(matrix)-column-1][row]
                
        
        print(matrix[0])
