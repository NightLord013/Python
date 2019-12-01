from math import *
def qwerty(x,y):
    z = (x+((2+y)/(x**2)))/(y+(1/(sqrt(x**2+10))))
    q = 2.8*sin(x)+fabs(y)
    print (z, "\n", q)
qwerty(1,2)
