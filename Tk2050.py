from tkinter import *
from time import sleep
from math import sin, cos, pi

class MAIN:
    def __init__(this):
        #One step from arguments
        this.ROOT = Tk()
        this.MAIN = Canvas(this.ROOT, bg='#222222', width = 400, height = 400)
        this.MAIN.pack()

        #The 'settings' dict, for storing color info
        this.settings={
            'bg':'#222222',
            'stroke':'#22cc22',
            'fill':'#228822'
        }

        this.vertices=[]

    def set(this,key,value):
        this.settings[key] = value

    def stroke(this,color):
        this.set('stroke',color)

    def fill(this,color):
        this.set('fill',color)

    def loop(this):
        #The main loop
        while True:
            this.loop_content()
            this.ROOT.update()
            sleep(0.01)

    def line(this,x1,y1,x2,y2):
        #Draws a line
        this.MAIN.create_line(x1,y1,x2,y2,fill=this.settings['fill'])

    def polygon(this,arr):
        #Draws a polygon with given vertices
        this.MAIN.create_polygon(arr,outline=this.settings['stroke'],fill=this.settings['fill'])

    def vertex(this,x,y):
        #Sets a vertex
        this.vertices.append((x,y))

    def endshape(this):
        #Ends a polygon
        this.polygon(this.vertices)
        this.vertices=[]

    def delete(this,target):
        #Deletes selected target
        this.MAIN.delete(target)

    def clear(this):
        #Clears the canvas
        this.MAIN.delete(ALL)


CANVAS=MAIN()

def line(x1,y1,x2,y2):
    CANVAS.line(x1,y1,x2,y2)

def clear():
    CANVAS.clear()

def stroke(color):
    CANVAS.stroke(color)

def fill(color):
    CANVAS.fill(color)

def vertex(x,y):
    CANVAS.vertex(x,y)

def endshape():
    CANVAS.endshape()

def rect(x,y,x_len,y_len,align='TOP LEFT'):

    align=align.split(' ')
    
    p0=[None,None]
    p1=[None,None]
    p2=[None,None]
    p3=[None,None]
    vs=[p0,p1,p2,p3]

    # Algorithm will be improved in 2075
    
    if align[0] == 'TOP':
        p0[1] = y
        p1[1] = y
        p2[1] = y+y_len
        p3[1] = y+y_len

    if align[0] == 'CENTER':
        p0[1] = y-y_len/2
        p1[1] = y-y_len/2
        p2[1] = y+y_len/2
        p3[1] = y+y_len/2

    if align[0] == 'BOTTOM':
        p0[1] = y-y_len
        p1[1] = y-y_len
        p2[1] = y
        p3[1] = y

    # The X Coordinates
    
    if align[1] == 'LEFT':
        p0[0] = x+x_len
        p1[0] = x
        p2[0] = x
        p3[0] = x+x_len

    if align[1] == 'CENTER':
        p0[0] = x+x_len/2
        p1[0] = x-x_len/2
        p2[0] = x-x_len/2
        p3[0] = x+x_len/2

    if align[1] == 'RIGHT':
        p0[0] = x
        p1[0] = x-x_len
        p2[0] = x-x_len
        p3[0] = x

    for v in vs:
        vertex(v[0],v[1])

    endshape()
        
def ellipse(x,y,x_rad,y_rad):
    divs=4*(x_rad+y_rad)
    a=2*pi/divs
    alpha = 0
    while alpha < 2*pi:
        vertex(cos(alpha)*x_rad+x,-1*sin(alpha)*y_rad+y)
        alpha+=a
    endshape()
    
    

def raiser():
    raise Exception('Import loop again, after defining the draw function!')

def passer():
    pass



def loop():

    try:
        from __main__ import draw
    except ImportError:
        pass

    try:
        CANVAS.loop_content = draw
    except NameError:
        CANVAS.loop_content = raiser
    CANVAS.loop()





#This program comes with a strange name... It doesn't matter.
