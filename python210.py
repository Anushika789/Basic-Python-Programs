#WAP to transpose a given matrix using list comprehension.
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]] 
transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))] 

print(transpose_matrix)