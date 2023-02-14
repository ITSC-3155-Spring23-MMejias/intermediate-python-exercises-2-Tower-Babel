import numpy as np
import random


the_list = []
x = random.random()
# Random float number
for i in range(10):
    x=random.random()
    the_list.append(x)

print(the_list)  
a = str(np.median(the_list))
b = str(np.mean(the_list))
c = str(np.std(the_list))
#print(np.median(the_list)+np.mean(the_list)+np.std(the_list))   
print("Mean: "+a+" Median: "+b+" Standard Deviation: "+c)
