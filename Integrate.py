__author__ = 'Mayank'
class Integrate:
    def __init__(self):
        self.l=[]
        self.s=0
        self.even_s=0
    def solve(self, a, b, n, f, method):
        if method is 'TrapezoidalRule':
                for i in range(n+1):
                    self.l.append(a+((b-a)*i)/n)
                for j in range(0, n+1):
                    if j is 0 or j is n:
                        self.s=self.s+f(self.l[j])
                    else:
                        self.s=self.s+2*f(self.l[j])
                return ((b-a)*(self.s))/(2*n)
        elif method is 'SimpsonsRule':
                for i in range(2*n+1):
                    self.l.append(a+((b-a)*i)/(2*n))
                for j in range(1, n+1):
                    self.s=self.s+f(self.l[2*j-1])
                for g in range(2, n+1):
                    self.even_s=self.even_s+f(self.l[2*g-2])
                return ((b-a)*(f(self.l[0])+f(self.l[2*n])+4*self.s+2*self.even_s))/(6*n)
#example
#def f(x):
 #   return 2*x

#p=Integrate()
#k=p.solve(1,5,10,f,'SimpsonsRule')
#print(k)
#ouput is: 24.0
