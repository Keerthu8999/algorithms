#Actual code of the function given in question 3 of assessment 2
# This code will generate a series of 24 values-
import matplotlib.pyplot as plt

def recursive(n):
    global t
    t += 1
    if n == 1:        
        return 1        
    else:
        return recursive(n-1) + recursive(n-1)            
t = 0
a = []
for i in range (1,25):
    a.append(i)
y = []
for i in a:
    print i, ":",
    r = recursive (i)
    y.append(r)
    print r

print "x = ",  a
print "y= ", y

plt.plot(a,y,color = "red", linewidth = 2.0, linestyle = "-")
plt.grid()
plt.show()
