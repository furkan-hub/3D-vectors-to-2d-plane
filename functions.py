import math
import numpy as np
import cv2
from sympy import symbols, Eq, solve


def camera_W_H(axis,plane,S1,S2,S3,h):
    
    W = ((S2[0]-S1[0])**2+(S2[1]-S1[1])**2+(S2[2]-S1[2])**2)**(1/2)
    H = ((S3[0]-S1[0])**2+(S3[1]-S1[1])**2+(S3[2]-S1[2])**2)**(1/2)

    pp_s1 = (plane[0]*S1[0]+plane[1]*S1[1]+plane[2]*S1[2])
    pp_s2 = (plane[0]*S2[0]+plane[1]*S2[1]+plane[2]*S2[2])
    pp_m = (plane[0]*S3[0]+plane[1]*S3[1]+plane[2]*S3[2])

    n = [(plane[0])/((plane[0]**2+plane[1]**2+plane[2]**2)**(1/2)),(plane[1])/((plane[0]**2+plane[1]**2+plane[2]**2)**(1/2)),(plane[2])/((plane[0]**2+plane[1]**2+plane[2]**2)**(1/2))]

    print("n: ",n)

    if not pp_s1 and pp_s2 and pp_m == 1:
        print("plane parameters can not define a plane change value")

    c = [axis[0]+h*n[0],axis[1]+h*n[1],axis[2]+h*n[2]]# camera point

    print("Camera cordinate: ",c)

    camera_W_H_result = [c,W,H]
    
    return camera_W_H_result

def vector_2d_to_2d(Vector,plane,S1,S2,S3,H,W,c):#Vector must be 
    
    #calculations for Vector vector 3d to 2d transformation cordinates
    x, y, z, k = symbols('x y z k')

    equation1 = Eq((x - Vector[0]) / (c[0] - Vector[0]), k)
    equation2 = Eq((y - Vector[1]) / (c[1] - Vector[1]), k)
    equation3 = Eq((z - Vector[2]) / (c[2]- Vector[2]), k)

    plane_equation = Eq(plane[0]*x + plane[1]*y + plane[2]*z, 1)

    solutions = solve([equation1, equation2, equation3, plane_equation], (x, y, z, k))

    # v′
    x_prime_a = solutions[x]
    y_prime_a = solutions[y]
    z_prime_a = solutions[z]

    Vectors =[x_prime_a,y_prime_a,z_prime_a] # new vector for Vector


    cos_u = ((S2[0]-S1[0])*(Vectors[0]-S1[0])+(S2[1]-S1[2])*(Vectors[1]-S1[1])+(S2[2]-S1[2])*(Vectors[2]-S1[2]))/((W*((Vectors[0]-S1[0])**2+(Vectors[1]-S1[1])**2+(Vectors[2]-S1[2])**2)**(1/2)))

    cos_v = ((S3[0]-S1[0])*(Vectors[0]-S1[0])+(S3[1]-S1[2])*(Vectors[1]-S1[1])+(S3[2]-S1[2])*(Vectors[2]-S1[2]))/((H*((Vectors[0]-S1[0])**2+(Vectors[1]-S1[1])**2+(Vectors[2]-S1[2])**2)**(1/2)))

    angle_u = math.acos(cos_u)

    sin_u = math.sin(angle_u)

    angle_v = math.acos(cos_v)

    sin_v = math.sin(angle_v)
    
    if cos_u and cos_v > 0:
        print("cos_u and cos_v is bigger than 0")
    
    m = (((Vector[0]-S1[0])**2+(Vector[1]-S1[1])**2+(Vector[2]-S1[2]))**(1/2))*cos_u

    n = (((Vector[0]-S1[0])**2+(Vector[1]-S1[1])**2+(Vector[2]-S1[2]))**(1/2))*sin_u
    
    cord = [m,n]
    
    return cord