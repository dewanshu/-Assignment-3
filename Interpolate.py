'''
class Interpolate:
    
    def solve(self,L,M,method):
        if(method=="newton"):
            return (self.Newton(L,M))
        else:
            return (self.Lagrange(L,M))

    def Lagrange(self,L,M):                                                
       
        
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(L)                                                           
        w=(-1*L[0],1)                                                      
        for i in range(1,n):
            w=P.polymul(w,(-1*L[i],1))                                    
        result=array([0.0 for i in range(len(w)-1)])                    
        derivative=P.polyder(w)                                             
        for i in range(n):
            result+=(P.polydiv(w,(-1*L[i],1))[0]*M[i])/P.polyval(L[i],derivative)   
        return(list(result))                                                
    def Newton(self,L,M):                                                   
       
        
        from numpy import array
        from numpy.polynomial import polynomial as P
        n=len(L)                                                            
        mat=[[0.0 for i in range(n)] for j in range(n)]                    
        for i in range(n):                                                 
            mat[i][0]=M[i]
        for i in range(1,n):                                               
            for j in range(n-i):
                mat[j][i]=(mat[j+1][i-1]-mat[j][i-1])/(L[j+i]-L[j])
        result=array((mat[0][0],))                                          
        for i in range(1,n):
            prod=(-1*L[0],1)                                               
                                                                            
            for j in range(1,i):
                prod=P.polymul(prod,(-1*L[j],1))                              
            result=P.polyadd(result,array(prod)*mat[0][i])                  
        return (list(result))                                               

apx=Interpolate()                                                          
for method in ["newton","lagrange"]:
    solution=apx.solve([1,2,3],[0,-1,0],method)
    print(solution)
'''
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

class Interpolate:
    A=[]
    B=[]
    C=[]
    # to find limits and poly.
    x = sp.Symbol('x')
    def Lagrange_Poly(self, L, M):
        # x coordinates are stored in B
        # C stores f(x)
        self.C=M
        self.B=L
        for i in range(len(L)):
            p, q = 1, 0
            # to form the list of polynimials
            # summation of which is Lagrange polynomial
            while q < len(L):
                if i != q:
                    p *= (self.x-L[q])/(L[i]-L[q])
                q += 1   
            p *= M[i] 
            self.A.append(p)
        # plot Lagrange Polynomial
        self.plot_the_graph()      
    
    def plot_the_graph(self, temp = []):
        arr = np.arange(0,max(self.B)+0.2,0.1)
        pol_sum = 0
        # plot function in the list
        for  i in self.A:
            pol_sum += i
            for q in arr:
                temp.append(sp.limit(i,self.x,q))
            plt.plot(arr, temp)             
            temp = []       
        # plot Lagrange Polynomial in Black Color
        for q in arr:
                temp.append(sp.limit(pol_sum,self.x,q))
        plt.plot(arr, temp,'p')
        # plot node points
        plt.plot(self.B,self.C,'ro')
        plt.show()                  

   
