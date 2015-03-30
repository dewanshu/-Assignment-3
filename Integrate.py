'''
__author__ = 'Mayank'
import math
from math import *
class Integrate:

    def __init__(self):
        self.function=None
        self.interval=None
        self.no_of_partitions=None
        self.result=None

    def solve(self,S,interval,method,N=10000):

        # N is an optional argument used for controlling the number of partitions

        if(method=="trapezoid"):
            return (self.TrapezoidalRule(S,interval,N))
        else:
            return (self.SimpsonsRule(S,interval,N))

    def TrapezoidalRule(self,S,interval,N):                                 # The function takes 3 user inputs

        # S is the string containing the function to be
        # integrated. The string must contain only those
        # functions which are available in "math" module,
        # and the syntax used in S must be the same as is
        # used in Python. e.g.,
        # If f(x)=sin(x)^2 + cos(x) + e^(x^0.5) + log(x), then --
        # S=sin(x)**2+cos(x)+exp(x**0.5)+log(x) OR
        # S=pow(sin(x),2)+cos(x)+exp(pow(x,0.5))+log(x)
        # L is a list of two values containing the lower
        # and upper limits of integration. e.g.,-
        # If we have to integrate f(x) from 1.5 to 6, then--
        # L=[1.5,6]
        # N is the variable used for controlling the number
        # of partitions.

        self.interval=interval
        self.no_of_partitions=N
        try:
            (lambda x:eval(S))(self.interval[0])
            self.function=lambda x:eval(S)                                  # lambda function which converts user input into a function
        except:
            return("Input is not in proper Python syntax")
        length=(self.interval[1]-self.interval[0])/self.no_of_partitions    # variable to store the length of each sub-interval
        sum_of_values=self.function(self.interval[0])                       # variable to store sum of function values
        for i in range(1,N):                                                # calculating sum of function values
            sum_of_values+=2*self.function(self.interval[0]+length*i)
        sum_of_values+=self.function(self.interval[1])
        self.result=((self.interval[1]-self.interval[0])*sum_of_values)/(2*self.no_of_partitions)  # calculating result
        return (self.result)                                                # return result

    def SimpsonsRule(self,S,interval,N):                                    # The function takes 3 user inputs

        # S is the string containing the function to be
        # integrated. The string must contain only those
        # functions which are available in "math" module,
        # and the syntax used in S must be the same as is
        # used in Python. e.g.,
        # If f(x)=sin(x)^2 + cos(x), then --
        # S=sin(x)**2+cos(x)+exp(x**0.5)+log(x) OR
        # S=pow(sin(x),2)+cos(x)+exp(pow(x,0.5))+log(x)
        # L is a list of two values containing the lower
        # and upper limits of integration. e.g.,-
        # If we have to integrate f(x) from 1.5 to 6, then--
        # L=[1.5,6]
        # N is the variable used for controlling the number
        # of partitions.

        self.interval=interval
        self.no_of_partitions=N
        try:
            (lambda x:eval(S))(self.interval[0])
            self.function=lambda x:eval(S)                                  # lambda function which converts user input into a function
        except:
            return("Input is not in proper Python syntax")
        length=(self.interval[1]-self.interval[0])/(2*self.no_of_partitions)    # variable to store the length of each sub-interval
        sum_of_values=self.function(self.interval[0])                       # variable to store sum of function values
        for i in range(1,2*N):                                              # calculating sum of function values
            temp=self.function(self.interval[0]+length*i)
            sum_of_values+=2*temp if i%2==0 else 4*temp
        sum_of_values+=self.function(self.interval[1])
        self.result=((self.interval[1]-self.interval[0])*sum_of_values)/(6*self.no_of_partitions)      # calculating result
        return (self.result)                                                # return result

#igr=Integrate()                                                     # object creation
#for method in ["trapezoid","simpson"]:
#    solution=igr.solve("2*x+x*x",[1,2],method,10000)
#    print (solution)
#    OUTPUT is:   5.333333335000004
#                 5.333333333333322
'''
imfort numpy as np
imfort matplotlib.pyplot as plt
class Integrate:
    rec_wid, p = 0.0, ''
    X_initial, X_final= 0.0, 0.0
    sum=0.0 
    Lowlimit, Uplimit = 0, 0
    def TrapezoidalRule(self, p, Lowlimit, Uplimit, nop):
        self.p = p
        self.Uplimit = Uplimit
        self.Lowlimit = Lowlimit
        self.X_initial = Lowlimit
        self.rec_wid = (Uplimit-Lowlimit)/(nop*1.0)
        self.X_final = Lowlimit + self.rec_wid
        self.plotcurve()
        for i in range(nop):
           self.plot_trapezium()
           self.sum += 0.5*self.rec_wid*(p(self.X_initial)+p(self.X_final)) 
           self.X_initial = self.X_final
           self.X_final += self.rec_wid
        plt.show() 
        return self.sum  
    def plotcurve(self):   
        my_arr = np.arange(self.Lowlimit-1.0,self.Uplimit+1.0,10**(-4))
        plt.plot(my_arr,self.p(my_arr),color = 'red', linewidth = 2.0)
    def plot_trapezium(self):
        plt.fill_between([self.X_initial, self.X_final],
        [self.p(self.X_initial), self.p(self.X_final)])
