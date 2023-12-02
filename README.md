# 3D-vectors-to-2d-plane
i just create a script that transfrom 3d vectors to 2d plane 

# Mapping 3D World to 2D Screen

This project includes the necessary steps to project a 3-dimensional world image onto a 2-dimensional screen.
# Mapping 3D World to 2D Screen

![image](https://github.com/furkan-hub/3D-vectors-to-2d-plane/assets/72547366/a0908138-dab1-4f7a-a064-8f4ba4085f88)


This project includes the necessary steps to project a 3-dimensional world image onto a 2-dimensional screen.

### Steps:

1. **Define the Left Top Point of the Screen (S1)**:
   This step defines the top-left corner of the screen in the 3D world. It has coordinates (x1, y1, z1).

2. **Define the Right Top Point of the Screen (S2)**:
   This step defines the top-right corner of the screen in the 3D world. It has coordinates (x2, y2, z2). The screen width (W) is determined by the distance between these two points.

3. **Define the Left Bottom Point of the Screen (S3)**:
   This step defines the bottom-left corner of the screen in the 3D world. It has coordinates (x3, y3, z3). The screen height (H) is calculated using the dot product of the vectors S1S2 and S1S3.

4. **Find the Middle Point of the Screen**:
   The middle point of the screen is defined as M(x0, y0, z0).

5. **Determine the Distance from the Camera to the Screen (h)**:
   Determines the distance between the camera and the screen.

6. **Find the Camera Point (C)**:
   The coordinates (xc, yc, zc) of the camera point are found by solving a plane equation.

7. **Find the Projection of A onto the Screen Plane (A′)**:
   A line between the camera point and point A is defined, and where this line intersects the screen plane, the projection A′ is found.

8. **Find Screen Angles**:
   The angles of A with respect to the screen are calculated using cosine and sine.

9. **If A′ is Inside the Screen**:
   Cosine and sine values are checked to determine if A′ lies within the screen.

10. **Find m and n Values**:
    If A′ is inside the screen, m and n values are calculated, representing the pixel values of A.

These steps involve mathematical and geometrical operations required to project a 3D world onto a 2D screen.

### Steps:

1. **Define the Left Top Point of the Screen (S1)**:
   This step defines the top-left corner of the screen in the 3D world. It has coordinates (x1, y1, z1).

2. **Define the Right Top Point of the Screen (S2)**:
   This step defines the top-right corner of the screen in the 3D world. It has coordinates (x2, y2, z2). The screen width (W) is determined by the distance between these two points.

3. **Define the Left Bottom Point of the Screen (S3)**:
   This step defines the bottom-left corner of the screen in the 3D world. It has coordinates (x3, y3, z3). The screen height (H) is calculated using the dot product of the vectors S1S2 and S1S3.

4. **Find the Middle Point of the Screen**:
   The middle point of the screen is defined as M(x0, y0, z0).

5. **Determine the Distance from the Camera to the Screen (h)**:
   Determines the distance between the camera and the screen.

6. **Find the Camera Point (C)**:
   The coordinates (xc, yc, zc) of the camera point are found by solving a plane equation.

7. **Find the Projection of A onto the Screen Plane (A′)**:
   A line between the camera point and point A is defined, and where this line intersects the screen plane, the projection A′ is found.

8. **Find Screen Angles**:
   The angles of A with respect to the screen are calculated using cosine and sine.

9. **If A′ is Inside the Screen**:
   Cosine and sine values are checked to determine if A′ lies within the screen.

10. **Find m and n Values**:
    If A′ is inside the screen, m and n values are calculated, representing the pixel values of A.

These steps involve mathematical and geometrical operations required to project a 3D world onto a 2D screen.
