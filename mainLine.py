import turtle
import math
import sys,os
from canvasvg import canvasvg
import cairosvg
import shutil
import tempfile

array = list()

start = 0
end = 0
zero = -300
scale = 1

pi = 3.141592653
t = turtle.Turtle()

width = 15
height = 100
def noTrace_goto( x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
def drawDot(flag):
    if(flag == 1): 
        t.dot(7, '#000000')
    if(flag == 2):
        t.dot(10, '#FF0000')

def plus(x,scale):

    drawDot(1)
    t.pencolor('#789CDC')
    t.fillcolor('#0000FF')

    t.pensize(3)
    pt = t.position()

    xx = int(-(x/2))
    dx = pt[0]
    dy = 0
    offs = math.sqrt(height/(x*x/4))
    ss = x/100
    y = 0
    while(y>=0):
        t.goto(dx, y)
        xx  = xx + ss
        y = (-(offs*xx)**2+height)
        dx = dx + ss*scale
        if(y == 0):
            break
    t.seth(0)
    angle = t.towards(pt[0]+x*scale, 0)
    t.goto(pt[0]+x*scale, 0)
    t.seth(angle)
    t.stamp()
    cx = pt[0] + int(x*scale/2)
    noTrace_goto(cx, height+10)
    t.write(x,font=("Arial", 16, "normal"))
    noTrace_goto(pt[0]+x*scale,0)

def minus(x,scale):
    pt = t.position()
    drawDot(1)   
    t.pencolor('#FF9282')
    t.fillcolor('#FF0000')

    xx = int((x/2))
    dx = pt[0]
    ddx = 0
    ddy = 0
    offs = math.sqrt(height/(x*x/4))
    ss = x/100
    y = 0
    while(y<=0):
        t.goto(dx, y)
        xx  = xx - ss
        y = ((offs*xx)**2-height)
        dx = dx - ss*scale
        if(y == 0):
            break
    t.seth(0)
    angle = t.towards(pt[0]-x*scale, 0)
    t.goto(pt[0]-x*scale, 0)
    t.seth(angle)
    t.stamp()
    cx = pt[0] - int(x*scale/2)
    noTrace_goto(cx-5, -height-22)
    t.write(x,font=("Arial", 16, "normal"))
    noTrace_goto(pt[0]-x*scale,0)
    print(angle)

def drawStepp(xx,num):

    t.pencolor('#000000')
    noTrace_goto(xx,5)
    t.seth(270)
    t.forward(10)
    noTrace_goto(xx-10,-20)
    t.write(str(int(num)),font=("Arial", 12, "normal"))

def drawStep(xx):

    t.pencolor('#000000')
    noTrace_goto(xx,5)
    t.seth(270)
    t.forward(10)

def mainLine():
    turtle.delay(0)
    t.speed(10)
    mi = 0
    ma=0 
    cur = 0
    scale = 1
    ran = 20
    t.hideturtle()
    i=0
    for n in array:
        cur = cur + int(n)
        i = i+1
        if(mi>cur):
            mi = cur
        if(ma<cur):
            ma = cur
    noTrace_goto(-400, 0)
    t.fillcolor('#F6D02F')
    t.begin_fill()
    t.forward(1000)
    step = 20
    scale = 600/(ma-mi)
    if(scale>1):
        scale = int(scale)
    width = int(ma - mi)
    if((ma<5000) and (ma >=1000)):
        step = 100
        ran = 500
    if((ma<1000) and (ma >=500)):
        step = 40
        ran = 200
    if((ma<500) and (ma >=150)):
        step = 20
        ran = 100            
    if((ma<150) and (ma>=90)):
        step = 10
        ran = 50            
    if((ma<90) and (ma>=0)):
        step = 5
        ran = 20
    if(ma>=5000):
        step = 500
        ran = 2000
    flag = 0
    mm = 0
    for ii in array:
        if(abs(ii)>=int(step/5)):
            flag = flag + 1
            mm = ii
    if(flag == 1):
        i = 1
        ma = mm
    if(i==1):
        if((ma<1000) and (ma >500)):
            step = 40
            ran = 200
        if((ma<500) and (ma >150)):
            step = 20
            ran = 100            
        if((ma<150) and (ma>90)):
            step = 10
            ran = 50            
        if((ma<90) and (ma>0)):
            step = 5
            ran = 20
        if(ma>1000):
            step = 100
            ran = 500


        xx = 0
        nn = ma
        scale = 1
        offset = ma%step
        xx = xx - offset*scale
        dx = 100
        nn = nn - offset        
        while (xx>-380):
            xx = xx - dx*scale
            nn = nn - step
        start = nn
        while (xx<350):
            drawStepp(xx,nn)
            xx = xx + dx*scale
            nn = nn + step

        end = nn
        t.pencolor('#000000')
        noTrace_goto(xx,5)
        t.seth(270)
        t.forward(10)
        noTrace_goto(xx,-20)
        t.write(str(end),font=("Arial", 12, "normal"))

        noTrace_goto(0,20)
        t.dot(10, '#0000FF')
        t.pencolor("#FF0000")
        noTrace_goto(-300,-120)
        t.write("start : %d, end: %d , range: %d[step: %d]" % (start,end,ran,step),font=("Arial", 20, "normal"))
        noTrace_goto(-300,-150)
        t.write("Single Dot",font=("Arial", 20, "normal"))
    else:
        # scale = int(math.ceil(600/(ma-mi)))
        zero = int(int(0-mi)*scale+(-300))
        noTrace_goto(zero, 0)
        width = int(ma - mi)
        if((width<5000) and (width >1000)):
            step = 100
            ran = 500
        if((width<1000) and (width >500)):
            step = 40
            ran = 200
        if((width<500) and (width >150)):
            step = 20
            ran = 100            
        if((width<150) and (width>90)):
            step = 10
            ran = 50            
        if((width<90) and (width>0)):
            step = 5
            ran = 20
        if(width>5000):
            step = 500
            ran = 2000
        xx = zero-int(step*scale)
        nn = -step
        noTrace_goto(xx,0)
        while (xx<=int(ma*scale+zero)):
            if(nn%ran == 0):
                drawStepp(xx,nn)
            else:
                drawStep(xx)
            nn = nn + step
            xx = xx + int(step*scale)
        start = mi  
        end = nn+step
        t.pencolor('#000000')
        noTrace_goto(xx,5)
        t.seth(270)
        t.forward(10)
        if(xx>600):
            noTrace_goto(600,0)
            t.seth(0)
            t.forward(xx-600+100)        
        noTrace_goto(xx,-20)
        t.write(str(end),font=("Arial", 12, "normal"))
        noTrace_goto(zero, 0)

        for i in array:
            if(i>0):
                plus(i,scale)
            else:
                minus(-i,scale)
        drawDot(2)

        t.pencolor("#FF0000")
        noTrace_goto(-300,-150)
        t.write("start : %d, end: %d , range: %d[step: %d]" % (start,end,ran,step),font=("Arial", 20, "normal"))

    t.hideturtle()
    nameSav = "1" + '.png'
    tmpdir = tempfile.mkdtemp() 
    tmpfile = os.path.join(tmpdir, 'tmp.svg') 
    ts = turtle.getcanvas()
    canvasvg.saveall(tmpfile, ts)
    with open(tmpfile) as svg_input, open(nameSav, 'wb') as png_output:
        cairosvg.svg2png(bytestring=svg_input.read(), write_to=png_output)
    shutil.rmtree(tmpdir)
    sys.exit()

if __name__ == '__main__':
 
    inputStr = sys.argv[1]

    total_sum = 0
    num = 0
    operation = "+"
    for val in inputStr:
        if val != "+" and val != "-":
            num = num * 10 + int(val)
        if val == "+" or val == "-":
            total_sum = total_sum + num
            if total_sum != 0:
                if (operation == "-"):            	
                    num = -num
                array.append(num)
            num = 0
            operation = val
    if (operation == "-"):              
        num = -num
    array.append(num)
    total_sum = total_sum + num
    mainLine()
