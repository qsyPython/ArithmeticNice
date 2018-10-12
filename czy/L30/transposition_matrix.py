# 给定一个矩阵
# A， 返回
# A
# 的转置矩阵。
#
# 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
#
#
#
# 示例
# 1：
#
# 输入：[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出：[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# 示例
# 2：
#
# 输入：[[1, 2, 3], [4, 5, 6]]
# 输出：[[1, 4], [2, 5], [3, 6]]
#
# 提示：
#
# 1 <= A.length <= 1000
# 1 <= A[0].length <= 1000

def transposition_matrix(matrix):
    if matrix is not None:
        matrix_row_length = len(matrix)
        matrix_line_length = len(matrix[0])
        if matrix_row_length >= 1 and matrix_row_length <= 1000 and matrix_line_length >= 1 and matrix_line_length <= 1000:

            transpositionMatrix = [[0]*matrix_row_length]*matrix_line_length
            for i in  range(matrix_line_length):
              subTranspositionMatrix = [0]*matrix_row_length
              for j in range(matrix_row_length):
                subTranspositionMatrix[j] = matrix[j][i]

              transpositionMatrix[i] = subTranspositionMatrix
            return transpositionMatrix
        return matrix


if __name__ == '__main__':
   matrix = transposition_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
   print(matrix)