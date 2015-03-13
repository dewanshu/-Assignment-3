import numpy as np

objective=[1,3]
constraint1=[10,5,4]
constraint2=[(1,2),(1,0),(0,1)]

class LPsolver():

    def solve(self,a,b,c):
        lb=len(b)
        la=len(a)
        arr=np.array(c)
        arr=np.concatenate((arr,np.identity(len(b))),1)
        b=np.array(b)
        x=[0]*l_a

        arr=np.insert(arr,len(a)+lb,b,1)
        B=np.array([0]*lb)
        C=np.array(a+[0]*lb)
        d=range(la,la+lb)
        while(1):
            maxpos=[]
            minpos=[]
            for i in range(la+lb):
                maxpos.append(C[i]-np.dot(B,arr[:,i]))


            c=maxpos.index(max(maxpos))

            if maxpos[c]<=0:
                break
            for i in range(lb):
                if arr[i,c]!=0:
                    minpos.append(arr[i,-1]/arr[i,c])
                else:
                    minpos.append(10000000000)
            q=filter(lambda x:x>0,minpos)
            if q==[]:
                return "unbounded function"
                break
            r=minpos.index(min(q))

            B[r]=C[c]
            d[r]=c
            arr[r,:]=arr[r,:]/arr[r,c]
            for i in range(lb):
                if(i!=r):
                    arr[i,:]=arr[i,:]-(arr[i,c]/arr[r,c])*arr[r,:]

        for i in range(len(d)):
            if d[i]<l_a:
                x[d[i]]=arr[i,-1]
        x=map(int,x)

        x.append(sum([x[i]*a[i] for i in range(la)]))
        return x


lps=LPsolver()
solution=lps.solve(objective,constraint1,constraint2)
print solution

