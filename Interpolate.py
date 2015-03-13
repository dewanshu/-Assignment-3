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
