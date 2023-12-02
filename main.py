import math
import numpy as np
import cv2
from sympy import symbols, Eq, solve
import functions
import json
import tkinter
import time

width, height = 800, 600  
black_background = np.zeros((height, width, 3), dtype=np.uint8)  

green_bgr = (0, 255, 0)
red_bgr = (0, 0, 255)
blue_bgr = (255, 0, 0)
while True:
    time.sleep(1)
    
    black_background = np.zeros((height, width, 3), dtype=np.uint8)  # Her döngüde arka planı sıfırla

    print("ok")
    with open('param.json', 'r') as file:
        data = json.load(file)

    print(data)
    #region 3d to 2d transform

    #corners of screen
    S1 = data["S1"]#(x,y,z)
    S2 = data["S2"]#(x,y,z)
    S3 = data["S3"]#(x,y,z)
    S4 = data["S4"]#(x,y,z)

    h = data["h"] # camera distance
    m_p = data["m_p"]# mid point of screen (mx,my,my)

    #global size
    axis = data["axis"]# global x ,global y , global z

    #plane
    plane = data["plane"] #a,b,c

    #vectors
    Vx = data["Vx"]#(x,y,z)
    Vy = data["Vy"]#(x,y,z)
    Vz =data["Vz"]#(x,y,z)
    origin = data["origin"]#(x,y,z)


    camera_W_H_result = functions.camera_W_H(axis,plane,S1,S2,S3,h)

    c = camera_W_H_result[0]
    W = camera_W_H_result[1]
    H = camera_W_H_result[2]

    Vx_2d = functions.vector_2d_to_2d(Vx,plane,S1,S2,S3,H,W,c)
    Vy_2d = functions.vector_2d_to_2d(Vy,plane,S1,S2,S3,H,W,c)
    Vz_2d = functions.vector_2d_to_2d(Vz,plane,S1,S2,S3,H,W,c)
    origin_2d = functions.vector_2d_to_2d(origin,plane,S1,S2,S3,H,W,c)


    #endregion


    transform_matris = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    #axis
    cv2.line(black_background,(int(origin_2d[0]),int(origin_2d[1])),(int(Vx_2d[0]),int(Vx_2d[1])),red_bgr,5)#x
    cv2.line(black_background,(int(origin_2d[0]),int(origin_2d[1])),(int(Vy_2d[0]),int(Vy_2d[1])),green_bgr,5)#y
    cv2.line(black_background,(int(origin_2d[0]),int(origin_2d[1])),(int(Vz_2d[0]),int(Vz_2d[1])),blue_bgr,5)#z

    
    
    cv2.imshow('Blank', black_background)
    cv2.waitKey(24)  
