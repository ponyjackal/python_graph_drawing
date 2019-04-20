import turtle
import math
import sys
import os
from PIL import Image, ImageFilter
from canvasvg import canvasvg
import cairosvg
import shutil
import tempfile
array = list()
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

start = 0
end = 0
zero = -300
scale = 1

ran = 20
pi = 3.141592653
t = turtle.Turtle()

width = 15
def noTrace_goto( x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def drawNumOutLine(x,cx,y=0,cy=15*11 ):
    noTrace_goto(x+7,y-5)
    t.pencolor("#000000")
    widx = cx - x - 15
    widy = cy - y
    t.seth(0)
    t.forward(widx)
    t.seth(90)
    t.forward(widy)
    t.seth(180)
    t.forward(widx)
    t.seth(270)
    t.forward(widy)
    t.seth(0)

def minus(x):
    pt = t.position()
    
    t.pencolor('#FF0000')
    t.fillcolor('#FF0000')

    t.seth(180)
    t.left(30)
    t.circle(-x,60)

    t.stamp()

def drawSquare(x,y):
    noTrace_goto(x, y)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.end_fill()

def drawGrid(x,y,angle,width):
    noTrace_goto(x, y)
    t.begin_fill()
    t.seth(angle[0])
    t.forward(width[0])
    t.seth(angle[1])
    t.forward(width[1])
    t.seth(angle[2])
    t.forward(width[2])
    t.seth(angle[3])
    t.forward(width[3])
    t.end_fill()

    for i in range(9):   
        t.seth(angle[0])
        t.forward(int(width[0]/10))
        pt = t.position()
        t.seth(angle[1])
        t.forward(width[1])
        noTrace_goto(pt[0],pt[1])

    noTrace_goto(x,y)
    
    for i in range(9):
        t.seth(angle[1])
        t.forward(int(width[1]/10))
        pt = t.position()
        t.seth(angle[0])
        t.forward(width[0])
        noTrace_goto(pt[0],pt[1])
def drawThousand(x,y):
    noTrace_goto(x, y)
    t.pencolor('#00FF00')
    t.fillcolor("#B6FEB1")
    angle = [0,90,180,270]
    widthh = [150,150,150,150]
    drawGrid(x,y,angle,widthh)
    angle = [0,30,180,210]
    widthh = [150,100,150,100]
    drawGrid(x,y+10*width,angle,widthh)
    angle = [30,90,210,270]
    widthh = [100,150,100,150]        
    drawGrid(x+10*width,y,angle,widthh)
    dx = x+10*width+90
    
    t.seth(0)
    noTrace_goto(dx, 0)

def drawHundred(x,y):
    noTrace_goto(x, y)
    t.pencolor('#FF0000')
    t.fillcolor('#FF9282')
    angle = [0,90,180,270]
    widthh = [150,150,150,150]
    drawGrid(x,y,angle,widthh)
    dx = x+150
    noTrace_goto(dx+width, 0)

def drawTen(x,y):
    noTrace_goto(x, y)  
    t.pencolor('#0000FF')
    t.fillcolor('#789CDC')
    t.begin_fill()
    t.seth(0)
    t.forward(width)
    t.seth(90)
    t.forward(width*10)
    t.seth(180)
    t.forward(width)
    t.seth(270)
    t.forward(width*10)
    t.end_fill()

    noTrace_goto(x,y)
    
    for i in range(9):
        t.seth(90)
        t.forward(width)
        pt = t.position()
        t.seth(0)
        t.forward(width)
        noTrace_goto(pt[0],pt[1])
    noTrace_goto(x+width, 0)

def drawOne(x,y,num):
    t.pencolor('#00FF00')
    t.fillcolor('#6FA219')
    wid = 5
    flag = 0
    cx = x
    dx = x
    dy = y
    nn = num
    while(num>0):
        if(flag%2 == 0):
            x = cx
            drawSquare(x,y)
            x = x + wid+width
        else:
            drawSquare(x,y)
            x = x + wid
            if(num>1):            
                y = y + wid+width
            dy = y
            dx = x
        num = num - 1
        flag = flag + 1  
    # if()      
    # drawSquare(cx,y)
    noTrace_goto(dx+width, 0)
    return dy+2*wid+width

def drawNumber(num):
    ppt = t.position()
    nn = num
    dy = 0
    ds = 0
    dd = 0
    while (num >= 1000):
        pt = t.position()
        drawThousand(pt[0]+width,0)
        ds = width*10+80
        num = num-1000;        
    while (num >= 100):
        pt = t.position()
        drawHundred(pt[0]+width,0)
        num = num-100;
    while (num >= 10):
        pt = t.position()
        drawTen(pt[0]+width,0)
        num = num-10;
    if(num>0):
        if(nn<10):
            pt = t.position()
            yy = int(math.ceil(nn/2))
            dd = int((width*11-yy*20)/2)
            dy = drawOne(pt[0]+width,dd,num)
        else:
            pt = t.position()
            dy = drawOne(pt[0]+width,0,num)
    pt = t.position()
    if(nn<10):
        drawNumOutLine(ppt[0],pt[0]+width,dd,dy)
    if(nn>=1000):
        drawNumOutLine(ppt[0],pt[0]+width,dd,ds)
    if(nn>=10 and nn<1000):
        drawNumOutLine(ppt[0],pt[0]+width)
    noTrace_goto(int((pt[0]+ppt[0])/2),-50)
    t.write(nn,font=("Arial", 20, "normal"))
    noTrace_goto(pt[0]+width,0)

def mainSquare():
    turtle.delay(0)
    t.speed(0)
    t.fillcolor('#F6D02F')
    t.begin_fill()
    
    noTrace_goto(-700, 0)

    # cnt = input()
    result = 0
    # for i in range(int(cnt)):
    #     n =  input()
    #     array.append(int(n))

    pt = t.position()
    ccx = 0
    cnt = 0;
    for i in array:
        result = result + i
        pt = t.position()
        ccx = pt[0]
        if(i>0):
            noTrace_goto(pt[0]+width,50)
            if(cnt!=0):
                t.write('+',font=("Arial", 16, "normal"))
            pt = t.position()
            noTrace_goto(pt[0]+30,0)
            drawNumber(i)
            cnt = cnt+1
        else:
            noTrace_goto(pt[0]+width,50)
            t.write('-',font=("Arial", 16, "normal"))
            pt = t.position()
            noTrace_goto(pt[0]+30,0)
            drawNumber(abs(i))
            cnt = cnt + 1

    pt = t.position()
    noTrace_goto(pt[0]+width,50)
    t.write('=',font=("Arial", 16, "normal"))
    pt = t.position()
    noTrace_goto(pt[0]+30,0)

    drawNumber(abs(result))

    t.hideturtle()
    nameSav = "2" + '.png'
    tmpdir = tempfile.mkdtemp() 
    tmpfile = os.path.join(tmpdir, 'tmpp.svg') 
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
    mainSquare()
