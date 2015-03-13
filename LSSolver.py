class LSSolver:
     def GaussJordan(self,A,b):
        C = []
        Ans = []
        for i in A:
            C += [[j for j in i]+[b[A.index(i)]]]
        for i in range(1,len(b)+1):
            run = C[i-1][i-1]
            for j in range(len(b)+1):
                    C[i-1][j] /= run
            for j in range(len(b)):
                if j != (i-1):
                   run = C[j][i-1]
                   for k in range(len(b)+1):
                       C[j][k] -= run*C[i-1][k]                
        for i in range(len(b)):
            Ans.append(C[i][len(b)])
        return Ans
