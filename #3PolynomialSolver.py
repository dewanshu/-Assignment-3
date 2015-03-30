'''
class PolynomialSolver:
	def F(self,n,L,val):
		k=0
		for i in range(n+1):
			k+=L[i]*(val**i)
		return k
	def Fder(self,n,L,val):
		k=0
		for i in range(1,n+1):
			k+=i*L[i]*(val**(i-1))
		return k
	def solve(self,n,L,method):
		if(method=='bisection'):
			print("Enter lower bound of root interval")
			l=int(input())
			print("Enter upper bound of root interval")
			u=int(input())
			print("Enter max of itertions")
			it=int(input())
			while(abs(self.F(n,L,l)-self.F(n,L,u))>0.00001 and it>0):
				m=(l+u)/2
				if(self.F(n,L,l)*self.F(n,L,m)<0):
					u=m
				else:
					l=m
				print (l,u,self.F(n,L,l),self.F(n,L,u))
				it-=1
			return([l,u])
		if(method=='secant'):
			print("Enter lower bound of interval in which root lies")
			l=int(input())
			print("Enter upper bound of interval in which root lies")
			u=int(input())
			print("Enter maximum number of itertions")
			it=int(input())
			while(abs(self.F(n,L,l))>0.00001 and it>0):
				f1=self.F(n,L,l)
				f2=self.F(n,L,u)
				l,u=u,u-(((u-l)*f2)/(f2-f1))
				print (l,u,f1,f2)
				it-=1
			return(l)
		if(method=='secantRF'):
			print("Enter lower bound of interval in which root lies")
			l=int(input())
			print("Enter upper bound of interval in which root lies")
			u=int(input())
			m=l
			print("Enter maximum number of itertions")
			it=int(input())
			while(abs(self.F(n,L,m))>0.00001 and it>0):
				f1=self.F(n,L,l)
				f2=self.F(n,L,u)
				m=u-(((u-l)*f2)/(f2-f1))
				fm=self.F(n,L,m)
				if(f1*fm<0):
					u=m
				else:
					l=m
				print (m)
				it-=1
			return(l)
		if(method=='newtonraphson'):
			print("Enter lower bound of interval in which root lies")
			l=int(input())
			print("Enter maximum number of itertions")
			it=int(input())
			while(abs(self.F(n,L,l))>0.00001 and it>0):
				l=l-self.F(n,L,l)/self.Fder(n,L,l)
			return(l)
		else:
			return NULL
'''
import matplotlib.pyplot as plt
import numpy as np
def poly_plot(p,q,u):
    min_range,max_range=q,u
    func=lambda x: sum([(x**(len(p)-p.index(i)-1))*i for i in p])
    w=0.001
    plot_point,y=[],[]#y will have f(x) points to help trace curve
    lowlim,uplim=[q],[u]
    while u-q>w:
          m=(q+u)/2.0
    if func(m)*func(l)<=0:
          u=m
          uplim.append(u)
    else:
          q=m
          lowlim.append(q)

    point=lowlim+uplim
    #point list contains point to be located on x axis
    
    for i in point:
          plot_point.append(func(i))#points to be located on curve ie f(x) will be in plot_point
    #now,we plot curve
    #print(plot_point)
    x=np.arange(min_range-0.2,max_range+0.3,0.01)
    for j in x:
          y.append(func(j))
    plt.plot(x,y,'k-')
    #plt.legend([pl1],('root point'),'best')
    plt.plot(point,plot_point,'bo')
    pl1=plt.plot(m,func(m),'ro')
    plt.title('finding roots by Bisection Method')
    plt.x('X-Axis')
    plt.y('Y-Axis')
    plt.show()
        
        
        
   
