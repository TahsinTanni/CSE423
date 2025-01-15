

####Task1#######

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500, 500

ballx = bally = 0
speed = 8
direction = 0
create_new = False

# house and details
def drawShapes():

    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 0)
    glVertex2d(100, 0)
    glVertex2d(-100, 0)
    glVertex2d(0, 75)
    glEnd()


    glBegin(GL_QUADS)
    glColor3f(0, 0, 0)
    glVertex2d(70, 0)
    glVertex2d(70, -150)
    glVertex2d(-70, -150)
    glVertex2d(-70, 0)
    glEnd()

    # Draw windows and door
    glLineWidth(5)
    glBegin(GL_LINES)
    # Right window
    glColor3f(1, 1, 1)
    glVertex2f(50, -75)
    glVertex2f(50, -45)
    glVertex2f(40, -60)
    glVertex2f(60, -60)
    glVertex2f(40, -45)
    glVertex2f(40, -75)
    glVertex2f(60, -45)
    glVertex2f(60, -75)
    glVertex2f(40, -45)
    glVertex2f(60, -45)
    glVertex2f(40, -75)
    glVertex2f(60, -75)

    # Left window
    glVertex2f(-50, -75)
    glVertex2f(-50, -45)
    glVertex2f(-40, -60)
    glVertex2f(-60, -60)
    glVertex2f(-40, -45)
    glVertex2f(-40, -75)
    glVertex2f(-60, -45)
    glVertex2f(-60, -75)
    glVertex2f(-40, -45)
    glVertex2f(-60, -45)
    glVertex2f(-40, -75)
    glVertex2f(-60, -75)

    # Door
    glVertex2f(-15, -65)
    glVertex2f(15, -65)
    glVertex2f(-15, -65)
    glVertex2f(-15, -150)
    glVertex2f(15, -65)
    glVertex2f(15, -150)
    glEnd()

raindrops = []

def generate_raindrop():
    global raindrops
    x = random.uniform(-150, 150)  
    y = W_Height / 2  
    raindrops.append([x, y])

def draw_raindrops():
    global raindrops
    glLineWidth(2) 
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)  
    for drop in raindrops:
        glVertex2f(drop[0], drop[1])         
        glVertex2f(drop[0], drop[1] - 30)    
    glEnd()

background_color = 0.0

def keyboardListener(key, x, y):
    global background_color, show_house
    if key == b'l':  
        background_color += 0.05
        if background_color > 1.0:
            background_color = 1.0
        print("Background Getting Lighter")
        show_house = True  
    elif key == b'd':  
        background_color -= 0.05
        if background_color < 0.0:
            background_color = 0.0
        print("Background Getting Darker")
        if background_color < 0.2:  
            show_house = False
        else:
            show_house = True  
    
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed, direction
    if key == GLUT_KEY_UP:
        speed *= 2
        print("Speed Increased")
    if key == GLUT_KEY_DOWN:
        speed /= 2
        print("Speed Decreased")
    if key == GLUT_KEY_RIGHT:
        direction += 0.02
    if key == GLUT_KEY_LEFT:
        direction -= 0.02
    glutPostRedisplay()

def mouseListener(button, state, x, y):
    global direction
    if state == GLUT_DOWN:
        if button == GLUT_LEFT_BUTTON:  
            direction -= 0.05
        elif button == GLUT_RIGHT_BUTTON :  
            direction += 0.05
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(background_color, background_color, background_color, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)

    draw_raindrops()
    drawShapes()

    if create_new:
        m, n = create_new
        glBegin(GL_POINTS)
        glColor3f(0.7, 0.8, 0.6)
        glVertex2f(m, n)
        glEnd()

    glutSwapBuffers()

def animate():
    glutPostRedisplay()
    global raindrops, speed, direction

 
    for drop in raindrops[:]:
        drop[0] += speed * direction
        drop[1] -= speed
        if drop[1] < -75: 
            raindrops.remove(drop)
    
    
    generate_raindrop()

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"Building a house in Rainfall")
init()

glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()


###################Task2#########################
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random

# W_Width, W_Height = 500, 500
# speed = 0.05

# blink = False
# frozen = False
# points = []

# def convert_coordinate(x, y):
#     global W_Width, W_Height
#     a = x - (W_Width / 2)
#     b = (W_Height / 2) - y 
#     return a, b

# def draw_points():
#     global points, color, blink
#     glPointSize(10)
#     glBegin(GL_POINTS)
#     for i in points:
#           x, y, dx, dy, color, visible = i
#           if visible or not blink:
#             glColor3f(*color)
#             glVertex2f(x, y)
#     glEnd()



# def drawBox():
#     glBegin(GL_LINES)
#     glColor3f(1.0, 1.0, 0.0)
#     glVertex2d(-200, -150)
#     glVertex2d(-200, 150)
#     glVertex2d(200, -150)
#     glVertex2d(200, 150)
#     glVertex2d(-200, -150)
#     glVertex2d(200, -150)
#     glVertex2d(-200, 150)
#     glVertex2d(200, 150)
#     glEnd()

# def display():
   
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glClearColor(0,0,0,0);	
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
   
#     glMatrixMode(GL_MODELVIEW)
  
#     glLoadIdentity()
   
#     gluLookAt(0,0,200,	0,0,0,	0,1,0)
#     glMatrixMode(GL_MODELVIEW)


#     drawBox()
#     draw_points()

#     glutSwapBuffers()
    
# def animate():
#     glutPostRedisplay()
#     global points, speed, blink, frozen

#     if frozen:
#         return
    
#     for i in range(len(points)):
#         points[i][0] += points[i][2] * speed
#         points[i][1] += points[i][3] * speed

#         if points[i][0] >= 200 or points[i][0] <= -200:
#             points[i][2] *= -1
#         if points[i][1] >= 150 or points[i][1] <= -150:
#             points[i][3] *= -1

#     if blink:
#         for i in range(len(points)):
#             points[i][5] = not points[i][5]




# def mouseListener(button, state, x, y): 
#     global points, speed, blink, frozen
    
#     if frozen:
#         return       
    
#     if button == GLUT_RIGHT_BUTTON:
#         if (state == GLUT_DOWN):
#             if 30<x<470 and 100<y<400:
#                 print(x,y)
#                 pointx, pointy = convert_coordinate(x,y)
#                 dirx, diry = random.choice([(1, 1), (-1, 1), (1, -1), (-1, -1)])
#                 color = [random.random(), random.random(), random.random()]
#                 points.append([pointx, pointy, dirx, diry, color, True])
#                 print(points)

#     elif button == GLUT_LEFT_BUTTON:
#         if state == GLUT_DOWN:
#             blink = not blink

# def keyboardListener(key, x, y):
#     global frozen
#     if key == b' ':  
#         frozen = not frozen
        
# def specialKeyListener(key, x, y):
#     global speed, frozen
#     if frozen:
#         return
    
#     if key == GLUT_KEY_UP:
#         # speed= fast
#         speed = min(5, speed + 0.05)
#     elif key == GLUT_KEY_DOWN:
#         # speed -= slow
#         speed = max(0.005, speed - 0.05)


# def init():
    
#     glClearColor(0,0,0,0)
  
#     glMatrixMode(GL_PROJECTION)
   
#     glLoadIdentity()
   
#     gluPerspective(104,	1,	1,	1000.0)
  

# glutInit()
# glutInitWindowSize(W_Width, W_Height)
# glutInitWindowPosition(0, 0)
# glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

# wind = glutCreateWindow(b"Task - 2")
# init()

# glutDisplayFunc(display)
# glutIdleFunc(animate)
# glutMouseFunc(mouseListener)
# glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(specialKeyListener)

# glutMainLoop()