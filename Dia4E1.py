class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        cols = len(mat[0])
        rows = len(mat)
        output = []
        nums = []
        if r * c != cols * rows:
            return mat
        else:
            for i in range(rows):
                for j in range(cols):
                    nums.append(mat[i][j])          #pasar la matriz a una sola lista
            for i in range(r):
                output.append(nums[i*c:(i+1)*c])        #formar las nuevas filas
            return output
