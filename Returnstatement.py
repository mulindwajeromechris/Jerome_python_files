from math import*
def f(x, y):
    return x*2+y*y-x/2

print("the result is ", f(5, 4))


def volume(L,w,h):
    return L*w*h
    
volume_pol = volume(5,6,3)
print("the volume is: ", volume_pol)

def perimeter(L,w):
    return 2*L + 2*w
perimeter_pol = perimeter(5,6)
print("the perimeter is; ", perimeter_pol)

def surface_area(l,W,H):
    return 2*l +2*W +2*H
surface_are = surface_area(8,6,5)
print("the surface area: ", surface_are)