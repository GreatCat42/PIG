# PIG / Python Version
from random import randint
from math import pi, sin, cos

RUN={
    'MAX_FRAMES' : 64*10,
    'FRAME_SPEED' : 1, #Useless, unless with TKinter
    'COUNT' : 0,
    'RUNNING' : 1,
}

SET_MEMORY = 50

SET={
    'a' : {
        'NUMBER' : 5,
        'RADIUS' : 10,
        'VELOCITY' : 2,
        'MEMORY' : SET_MEMORY,
        'TOGGLE' : 80/100,
    },

    'b' : {
        'NUMBER' : 0,
        'RADIUS' : 5,
        'VELOCITY' : 2,
    },

    'c' : {
        'NUMBER' : 0,
        'RADIUS' : 10,
        'VELOCITY' : 2,
        'MEMORY' : SET_MEMORY,
        'TOGGLE' : 80/100,
    },

    'd' : {
        'NUMBER' : 40,
        'RADIUS' : 5,
        'VELOCITY' : 2,
    },

    'SIM' : {
        'SIZE_X' : 400,
        'SIZE_Y' : 400,
    },
}

PARTICLES=[]

def dist(x1,x2,y1,y2):
    dx = x2-x1
    dy = y2-y1

    d = (dx**2 + dy**2)**0.5

    return d

def DIRECTION(x1,y1,x2,y2):

    d=dist(x1,y1,x2,y2)

    dx=(x2-x1)/d
    dy=(y2-y1)/d

    return [dx,dy]

def getAC(A,B):
    if A.type == 'a' or A.type == 'c':
        if B.type == 'a' or B.type == 'c':
            return 0;
        else:
            return [A,B];
    else:
        if B.type == 'a' or B.type == 'c':
            return [B,A];
        else:
            return 0;

class particle(type):

    def __init__(this, type):
        this.x = randint(0,SET['SIM']['SIZE_X'])
        this.y = randint(0,SET['SIM']['SIZE_Y'])

        this.type = type

        a = randint(0,1000)*pi/1000
        this.direction = [sin(a),cos(a)]

        this.memory = []
        this.pointer = 0

        if this.type == 'a' or this.type == 'c':
            memoryN = SET[this.type]['MEMORY']

            ch = ''

            if this.type == 'a':
                ch = 'd'
            else:
                ch = 'c'

            for i in range(memoryN):
                this.memory.append(ch)

    def show(this):
        pass
        #With TKinter

    def move(this):

        this.moveon()
        this.edge()

    def moveon(this):

        this.x += this.direction[0]*SET [this.type] ['VELOCITY']
        this.y += this.direction[1]*SET [this.type] ['VELOCITY']

    def edge(this):

        x = SET ['SIM'] ['SIZE_X']
        y = SET ['SIM'] ['SIZE_Y']

        if this.x > x:
            this.x -= x
        elif this.x < 0:
            this.x += x

        if this.y > y:
            this.y -= y
        elif this.y < 0:
            this.y += y

    def toggle(this):
        if this.type in ['a','c']:
            this.toggleAC()
        elif this.type in ['b','d']:
            this.toggleBD()

    def toggleAC(this):
        memory=this.readMemory()
        if this.type == 'a' and memory['b'] >= SET ['a'] ['MEMORY'] * SET ['a'] ['TOGGLE']:
            this.type = 'c'
        elif this.type == 'c' and memory['d'] >= SET ['c'] ['MEMORY'] * SET ['c'] ['TOGGLE']:
            this.type = 'a'

    def toggleBD(this):
        if this.type == 'b':
            this.type = 'd'
        elif this.type == 'd':
            this.type = 'b'

    def readMemory(this):
        ret={
            'b':0,
            'd':0,
            }

        for i in this.memory:
            ret[i]+=1

        return ret

    def writeMemory(this,INPUT):
        this.memory[this.pointer] = INPUT

        this.pointer+=1
        this.pointer%=this.memory.length

    def runself(this):
        this.move()

    def detectDist(this,that):

        d = dist(this.x,this.y,that.x,that.y);

        if d < SET[this.type]['RADIUS'] + SET[that.type]['RADIUS'] and not(d == 0):
            this.collide(that)

    def collide(this,that):

        R=getAC(this,that)

        if R:
            AC=R[0]
            BD=R[1]

            AC.writeMemory(BD.type)

            if (AC.type == 'a' and BD.type == 'd') or (AC.type == 'a' and BD.type == 'd'):
                BD.toggle()

            AC.toggle()

        this.COLLIDE(that)

    def COLLIDE(this,that):
        direction = DIRECTION(this.x,this.y,that.x,that.y)
        avgPos = [(this.x+that.x)/2 , (this.y+that.y)/2]

        this.direction = [-direction[0],-direction[1]]
        this.moveon()

        that.direction = direction
        that.moveon()

    def runw(this,that):
        this.detectDist(that)

    def run():
        this.runself()

        for particle in PARTICLES:
            this.runw(particle)


        

# DIVISION LINE / PYTHON / JS




var INIT=function(){
    var types=['a','b','c','d'];

    for(var i=0;i<types.length;i++){
        var type=types[i];

        for(var j=0;j<SET[type].NUMBER;j++){
            PARTICLES.push(new particle(type));
        }

    }
};

var RUN_FRAME=function(){

    for(var i=0;i<PARTICLES.length;i++){
        PARTICLES[i].run();
    }

    COUNT++;

};

var SHOW=function(){
    background(255, 250, 184);
    for(var i=0;i<PARTICLES.length;i++){
        PARTICLES[i].show();
    }
};

var PROGBAR=function(){

    noStroke();

    fill(255,255,255,100);
    rect(50,330,300,25);

    var progRatio=COUNT/MAX_FRAMES;
    fill(255,255,255,255);
    rect(50,330,300*progRatio,25);
};

var CHECK_COMPLETE=function(){
    if(COUNT>=MAX_FRAMES){
        RUNNING=0;
    }
};

INIT();

draw= function() {
    if(RUNNING){
        for(var i=0;i<FRAME_SPEED;i++){
            RUN_FRAME();
            CHECK_COMPLETE();
        }

        SHOW();
        PROGBAR();
    }

};

# Special Difficulty

#Requires TKinter
particle.prototype.show=function(){
    //COMPLETE

    noStroke();

    if(this.type === 'a'){

        fill(255, 108, 92);

    }else if(this.type === 'b'){

        fill(155, 255, 115);

    }else if(this.type === 'c'){

        fill(232, 205, 86);

    }else if(this.type === 'd'){

        fill(83, 219, 208);

    }

    ellipse(this.x,this.y,SET[this.type].RADIUS*2,SET[this.type].RADIUS*2);
};
