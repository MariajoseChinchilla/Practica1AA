from math import comb
class Solution:
    def generate(self, numRows: int):
        answer = [ [] for l in range(numRows)]
        for i in range(0,numRows):
            for j in range(0,i+1):
                entrada = comb(i,j)
                answer[i].append(entrada)
        return answer