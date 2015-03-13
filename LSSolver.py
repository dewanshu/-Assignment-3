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
     def Gauss(self,A,b):
        C = []
        Ans = []
        for i in A:
            C += [[j for j in i]+[b[A.index(i)]]]
        for i in range(1,len(b)):
            run = C[i-1][i-1]
            for j in range(len(b)+1):
                    C[i-1][j] /= run
            for j in range(i,len(b)):
                run = C[j][i-1]
                for k in range(len(b)+1):
                    C[j][k] -= run*C[i-1][k]
        run = C[i][i]
        for j in range(len(b)+1):
                    C[i][j] /= run                    
        C.reverse()            
        for i in range(len(b)):
            run = 0
            for j in range(len(Ans)):
                run += C[i][len(b)-1-j]*Ans[j]
            Ans.append(C[i][len(b)]-run)
        Ans.reverse()    
        return Ans   
