import math
import numpy as np
import matplotlib.pyplot as plt

# A one dimensional solution to a linear dispersive PDE
class TalbotSolution:
    
    ##### Constants #####
    pi = np.pi
    NFourier = 500
    
    ##### Fields #####
    t = np.pi/6                       # Time to graph solution at 
    resolution = 500              # Number of values in solution
    bounds = (-1, 1)                # Bounds that the solution will be graphed on
    solution = []                   # Linear solution data
    disp_poly  = [0, 2]             # Coefficients for the dispersion relation
        
    xlist = []
    uReal = []
    uImag = []
    ##### Functions #####

    def __init__(self):
        
        ##### Constants #####
        pi = np.pi
        NFourier = 1000
        
        ##### Fields #####
        t = pi/6                        # Time to graph solution at 
        resolution = 1000               # Number of values in solution
        bounds = (-1, 1)                # Bounds that the solution will be graphed on
        solution = []                   # Linear solution data
        disp_poly  = [0, 2]             # Coefficients for the dispersion relation
        
        uReal = []
        uImag = []
        
        return
        
    # Returns the value of the dispersion relation for this soln
    def w(self, n):  
        output = 0
        power = 1
        
        for coeff in self.disp_poly:
            
            output += coeff*(n**power)
            power += 1
        
        return output
    
    
    def calculateLinearSolution(self):    
       ##### Approx. Solution to iut + uxx = 0  #####
        
        soln_length = 3000 
        self.xlist = np.linspace(self.bounds[0], self.bounds[1], self.resolution)
        
        t = self.t
        
        for x in self.xlist:
        
            Rsum = 0
            Isum = 0
            n = 0
        
            # Defining time slice to graph solution at
            #t = x        
        
            while n < self.NFourier:
        
                if (n % 2 != 0):
        
                    argpos = n*x + self.w(n)*t     # Positive argument
                    argneg = -n*x + self.w(-n)*t   # Negative argument
        
                    Rsum += (2/n)*np.sin(argpos)
                    Rsum += (-2/n)*np.sin(argneg)
        
                    Isum += -(2/n)*np.cos(argpos)
                    Isum += (2/n)*np.cos(argneg)
        
                n += 1
        
            self.uReal.append(Rsum)
            self.uImag.append(Isum)
    
    def stepFunction1(x):         # 2pi periodic function  

        w = x % (2*np.pi)
    
        #print(w)
    
        if w >= 0 and w < np.pi:
    
            return 0
    
        if w >= np.pi and w < 2*np.pi:
    
            return 1

    def plot(self):
        print("Showing solutions...")
        plt.close()

        f, axarr = plt.subplots(2, sharex=True,figsize = (30,10))
        plt.plot(self.xlist, self.uReal)
        plt.plot(self.xlist, self.uReal)

        plt.show()

        return
                   
    def setVertexList(self, vertexField):
        self.vertexField = vertexField
        
        return
    
    def getVertexField(self):
        return self.vertexField
    