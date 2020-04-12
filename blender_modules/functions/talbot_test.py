import talbot_effect as tb


print("Running talbot test")
soln = tb.TalbotSolution()
    
soln.calculateLinearSolution()
soln.plot()

import matplotlib.rcsetup as rcsetup
print(rcsetup.all_backends)