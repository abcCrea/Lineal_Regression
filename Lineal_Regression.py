# <abc Crea 2020> - <Oscar Eduardo Ochoa Velasco>
import math

#Enter the values or dates in order on the x y array
x = [40,39.5,41.5,42,39,30,41,42.5,39.5,41,40,31]
y = [150,151,157.5,165,150,125,150,170,157.5,165,155,120]

#Iteration variable - Modify agree with the number of input values
VAR = 12

#Simple declaration of the ouput array - *IMPORTANT* If you increase the VAR value more than 12, increase the number of elements on these array:
xy = [0,0,0,0,0,0,0,0,0,0,0,0]
x2 = [0,0,0,0,0,0,0,0,0,0,0,0]
xx = [0,0,0,0,0,0,0,0,0,0,0,0]
yy = [0,0,0,0,0,0,0,0,0,0,0,0]
a = [0,0,0,0,0,0,0,0,0,0,0,0]
b2 = [0,0,0,0,0,0,0,0,0,0,0,0]
c = [0,0,0,0,0,0,0,0,0,0,0,0]

#Declaration of simple total variable for the posterior use
X = 0
Y = 0
XY = 0
X2 = 0
XX = 0
YY = 0
XXYY = 0

#Starting the operations and loops

#Loop for obtain the total addition of the array x y 
for i in range(VAR):
    X = X + x[i]
    Y = Y + y[i]
#Obtain the x per y array "xy" and the total multiplication "XY"
    xy[i] = x[i]*y[i]
    XY = XY + xy[i]
#Obtain the total x square
    x2[i] = pow(x[i],2)  
    X2 = X2 + x2[i]

#Operations for obtain the respective variables
m = ( (VAR*XY) - (X*Y) ) / ( (VAR*X2) - pow(X,2) )
b = (Y/VAR) - (m*X/VAR)
t = (m*x[VAR-1]) + b 

medx = X/VAR
medy = Y/VAR

#Second loop for obtain the rest of our dates
for i in range(VAR):
    xx[i] = pow(x[i] - medx,2)
    a[i] = x[i] - medx
    XX = XX + xx[i]
    yy[i] = pow(y[i] - medy,2)
    b2[i] = y[i] - medy
    YY = YY + yy[i]
    c[i] = a[i] * b2[i]
    XXYY = XXYY + c[i]

#Operation for obtain r value
r = (XXYY) / (math.sqrt(XX) * math.sqrt(YY))

#Showing the dates on a table format with a loop
print("xi       yi          xy          x^2     (x-X)^2   (y-Y)^2   (x-X)(y-Y)")
for i in range(VAR):
    print("{:.1f}".format(x[i]),"   ","{:.1f}".format(y[i]),"   ","{:.2f}".format(xy[i]),"   ","{:.2f}".format(x2[i]),"   ","{:.2f}".format(xx[i]),"   ","{:.2f}".format(yy[i]),"     ","{:.2f}".format(c[i]))
print("{:.1f}".format(X),"  ","{:.1f}".format(Y),"  ","{:.1f}".format(XY),"   ","{:.1f}".format(X2),"  ","{:.1f}".format(XX),"   ","{:.1f}".format(YY),"    ","{:.1f}".format(XXYY))
print("m: ","{:.2f}".format(m))
print("b: ","{:.2f}".format(b))
print("y: ","{:.2f}".format(t))
print("r: ","{:.2f}".format(r))