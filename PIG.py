MAX_FRAMES=64*10

FRAME_SPEED=1

MEMORY=50

SET={
    'a' : {
        'NUMBER' : 5,
        'RADIUS' : 10,
        'VELOCITY' : 2,
        'MEMORY' : MEMORY,
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
        'MEMORY' : MEMORY,
        'TOGGLE' : 80/100,
    },

    'd' : {
        'NUMBER' : 40,
        'RADIUS' : 5,
        'VELOCITY' : 2,
    },

};



# ------------------------------------------------------------------------------


var PARTICLES=[];

var DIRECTION=function(x1,y1,x2,y2){
    var d=dist(x1,y1,x2,y2);
    var dx=(x2-x1)/d;
    var dy=(y2-y1)/d;
    return [dx,dy];
};

var getAC=function(A,B){
    if(A.type === 'a' || A.type === 'c'){
        if(B.type === 'a' || B.type === 'c'){
            return 0;
        }else{
            return [A,B];
        }
    }else{
        if(B.type === 'a' || B.type === 'c'){
            return [B,A];
        }else{
            return 0;
        }
    }
};

var particle=function(type){
    //COMPLETE

    this.x=random(0,400);
    this.y=random(0,400);

    this.type=type;

    var a=random(0,360);
    this.direction=[sin(a),cos(a)];

    this.memory=[];
    this.pointer=0;

    if(this.type === 'a' || this.type === 'c'){
        var memoryN=SET[this.type].MEMORY;
        if(this.type === 'a'){
            for(var i=0; i<memoryN; i++){
                this.memory.push('d');
            }
        }else if(this.type === 'c'){
            for(var i=0; i<memoryN; i++){
                this.memory.push('b');
            }
        }
    }
};

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

particle.prototype.move=function(){
    //COMPLETE

    this.moveon();
    this.edge();
};

particle.prototype.moveon=function(){
    //COMPLETE

    this.x+=this.direction[0]*SET[this.type].VELOCITY;
    this.y+=this.direction[1]*SET[this.type].VELOCITY;
};

particle.prototype.edge=function(){
    //COMPLETE

    if(this.x>400){
        this.x-=400;
    }else if(this.x<0){
        this.x+=400;
    }

    if(this.y>400){
        this.y-=400;
    }else if(this.y<0){
        this.y+=400;
    }

};

particle.prototype.toggle=function(){
    //COMPLETE

    if(this.type === 'a' || this.type === 'c'){
        this.toggleAC();
    }else if(this.type === 'b' || this.type === 'd'){
        this.toggleBD();
    }
};

particle.prototype.toggleAC=function(){
    //COMPLETE

    var memory=this.readMemory();
    if(this.type === 'a' && memory.b >= SET.a.MEMORY*SET.a.TOGGLE){
        this.type = 'c';
    }else if(this.type === 'c' && memory.d >= SET.c.MEMORY*SET.c.TOGGLE){
        this.type = 'a';
    }
};

particle.prototype.readMemory=function(){

    //COMPLETE

    var ret={
        b : 0,
        d : 0,
    };

    for(var i=0;i<this.memory.length;i++){
        ret[this.memory[i]]+=1;
    }

    return ret;
};

particle.prototype.writeMemory=function(input){
    //COMPLETE
    this.memory[this.pointer] = input;

    this.pointer++;

    this.pointer %= this.memory.length;
};

particle.prototype.toggleBD=function(){
    //COMPLETE

    if(this.type === 'b'){
        this.type = 'd';
    }else if(this.type === 'd'){
        this.type = 'b';
    }

};

particle.prototype.runself=function(){

    //this.show();
    this.move();

};

particle.prototype.detectDist=function(that){

    //COMPLETE

    var d = dist(this.x,this.y,that.x,that.y);

    if(d < SET[this.type].RADIUS + SET[that.type].RADIUS){
        this.collide(that);
    }

};

particle.prototype.collide=function(that){
    //COMPLETE

    var R=getAC(this,that);
    if(R){
        var AC=R[0];
        var BD=R[1];

        AC.writeMemory(BD.type);

        if((AC.type === 'a' && BD.type === 'd')||(AC.type === 'c' && BD.type === 'b')){
            BD.toggle();
        }

        AC.toggle();

    }
    this.COLLIDE(that);
};

particle.prototype.COLLIDE=function(that){
    //COMPLETE
    var direction = DIRECTION(this.x,this.y,that.x,that.y);

    var avgPos = [(this.x+that.x)/2 , (this.y+that.y)/2];

    this.x = avgPos[0]-direction[0]*(SET[this.type].RADIUS+0.02);
    this.y = avgPos[1]-direction[1]*(SET[this.type].RADIUS+0.02);
    this.direction = [-direction[0],-direction[1]];

    that.x = avgPos[0]+direction[0]*(SET[that.type].RADIUS+0.02);
    that.y = avgPos[1]+direction[1]*(SET[that.type].RADIUS+0.02);
    that.direction = direction;

};

particle.prototype.runw=function(that){
    //COMPLETE

    if(dist(this.x,this.y,that.x,that.y)>0){
        this.detectDist(that);
    }

};

particle.prototype.run=function(){
    //COMPLETE
    this.runself();

    for(var i=0;i<PARTICLES.length;i++){
        this.runw(PARTICLES[i]);
    }
};


var COUNT = 0;

var RUNNING = 1;


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
