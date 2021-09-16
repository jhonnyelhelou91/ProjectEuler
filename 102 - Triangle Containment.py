# point p in triangle abc => Area{abc} = Area{abp} + Area{apc} + Area{pbc}
import math

def area(Ax, Ay, Bx, By, Cx, Cy):    
    return abs(Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By))

Px = 0
Py = 0
count = 0
triangles = [points.split(',') for points in open('p102_triangles.txt', 'r').read().split('\n') if len(points) > 0]

for points in triangles:
    Ax = int(points[0])
    Ay = int(points[1])
    Bx = int(points[2])
    By = int(points[3])
    Cx = int(points[4])
    Cy = int(points[5])

    abc = area(Ax, Ay, Bx, By, Cx, Cy)
    abp = area(Ax, Ay, Bx, By, Px, Py)
    apc = area(Ax, Ay, Px, Py, Cx, Cy)
    pbc = area(Px, Py, Bx, By, Cx, Cy)

    if abc == abp + apc + pbc:
        print (Ax, Ay, Bx, By, Cx, Cy)
        count += 1

print count