from tkinter import *
from time import sleep

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
