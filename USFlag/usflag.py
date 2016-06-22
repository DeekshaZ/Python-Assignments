'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  4
Description :  Program to draw US Flag
----------------------------------------------------------------------------------------------------------'''
import turtle
import time

#drawRectangle() method takes turtle object, length and breadth of rectangle, x position , y position  and fill color
def drawRectangle( myTurtle , length , breadth , x , y ,fillcolor ):
    myTurtle.up()
    myTurtle.setpos(x,y)
    myTurtle.color(fillcolor)
    myTurtle.begin_fill()
    myTurtle.down()
    myTurtle.forward(length)
    myTurtle.right(90)
    myTurtle.forward(breadth)
    myTurtle.right(90)
    myTurtle.forward(length)
    myTurtle.right(90)
    myTurtle.forward(breadth)
    myTurtle.end_fill()

#drawStar() method takes turtle object, size of star, x position , y position  and fill color
def drawStar( myTurtle , size , x , y , fillcolor ):
    myTurtle.up()
    myTurtle.setpos(x,y)
    myTurtle.color(fillcolor)
    myTurtle.begin_fill()
    myTurtle.down()
    myTurtle.forward(size)
    myTurtle.left(144)
    myTurtle.forward(size)
    myTurtle.left(144)
    myTurtle.forward(size)
    myTurtle.left(144)
    myTurtle.forward(size)
    myTurtle.left(144)
    myTurtle.forward(size)
    myTurtle.left(144)
    myTurtle.end_fill()


t = turtle.Turtle()
#drawing outer rectangle
breadth = 200
length = breadth*1.9
x = -150
y = 150
t.speed(10)
drawRectangle(t, length, breadth,-150,150,'red')

#drawing white stripes
stripeWidth = float(round(breadth/13,1))  #width of each stripe = breadth of rectangle/13
y = 150-2*stripeWidth #y position of the white stripe
for i in range(6): #to draw 6 white stripes
    t.setheading(90)
    drawRectangle(t, stripeWidth,length,x,y,'white')
    y -= 2*stripeWidth #update position of each white stripe

#drawing inner blue Rectangle
innerRectb = breadth*(7/13) #breadth of blue rectangle
innerRectl = length*(2/5)  #length of blue rectangle
x = -150+innerRectl
y = 150-innerRectb
drawRectangle(t, innerRectl,innerRectb,x,y,'navy')

#drawing stars
t.speed(100)
y = 140
for i in range(5):  #to draw 5 rows
    x = -160
    for j in range(10): # to draw 10 stars in each of the 5 rows
        x += 15  #horizontal distance between two stars
        drawStar(t , 6 , x , y , 'white')
    y -= 20 #distance between two rows
t.hideturtle() 
time.sleep(3)

