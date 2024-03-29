import turtle
from playsound import playsound
playsound('HAPPY BIRTHDAY INSTRUMENTAL.mp3')
t=turtle.Turtle()
t.width(2)
t.color('pink')
t.pencolor('Black')
t.begin_fill()
t.speed(10)
t.hideturtle()
#moving down
t.penup()
t.right(90)
t.forward(150)
t.left(90)
t.pendown()
#bottom layer
t.forward(160)
t.left(90)
t.forward(50)
t.left(90)
t.forward(320)
t.left(90)
t.forward(50)
t.left(90)
t.forward(160)
t.end_fill()

#1st layer
t.color('pink')
t.pencolor('black')
t.begin_fill()
t.penup()
t.setpos(0,-100)
t.pendown()
t.forward(120)
t.left(90)
t.forward(50)
t.left(90)
t.forward(240)
t.left(90)
t.forward(50)
t.left(90)
t.forward(120)
t.end_fill()
#top layer
t.penup()
t.setpos(0,-50)
t.pendown()
t.color('black','pink')
t.begin_fill()
t.forward(80)
t.left(90)
t.fd(50)
t.left(90)
t.fd(160)
t.left(90)
t.fd(50)
t.left(90)
t.fd(80)
t.end_fill()
#circle botton
t.penup()
t.color('black','pink')
t.setpos(-160,-100)
t.color('black','cyan')
t.pendown()
t.begin_fill()
t.right(90)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.end_fill()
#circle 1st
t.penup()
t.setpos(-120,-50)
t.pendown()
t.color('black','cyan')
t.begin_fill()
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.end_fill()
#circle top
t.penup()
t.setpos(-80,0)
t.pendown()
t.color('black','cyan')
t.begin_fill()
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.right(180)
t.circle(20,180)
t.end_fill()
#candels
t.penup()
t.setpos(-53.4,0)
t.pendown()
t.color('black','green')
t.begin_fill()
t.fd(20)
t.right(90)
t.forward(10)
t.right(90)
t.fd(20)
t.end_fill()
t.color('black','yellow')
t.penup()
t.setpos(-26.8,0)
t.pendown()
t.begin_fill()
t.right(180)
t.fd(20)
t.right(90)
t.forward(10)
t.right(90)
t.fd(20)
t.end_fill()
t.color('black','red')
t.penup()
t.setpos(-0.2,0)
t.pendown()
t.begin_fill()
t.right(180)
t.fd(20)
t.right(90)
t.forward(10)
t.right(90)
t.fd(20)
t.end_fill()
t.color('black','blue')
t.penup()
t.setpos(26.4,0)
t.pendown()
t.begin_fill()
t.right(180)
t.fd(20)
t.right(90)
t.forward(10)
t.right(90)
t.fd(20)
t.end_fill()
t.color('black','purple')
t.penup()
t.setpos(53,0)
t.pendown()
t.begin_fill()
t.right(180)
t.fd(20)
t.right(90)
t.forward(10)
t.right(90)
t.fd(20)
t.end_fill()
#flames
#1
t.penup()
t.setpos(-52.4,20)
t.pendown()
t.color('black','orange')
t.right(180)
t.fd(5)
t.begin_fill()
t.circle(-4)
t.end_fill()
#2
t.penup()
t.setpos(-25.8,20)
t.pendown()
t.color('black','orange')
t.fd(5)
t.begin_fill()
t.circle(-4)
t.end_fill()
#3
t.penup()
t.setpos(0.8,20)
t.pendown()
t.color('black','orange')
t.fd(5)
t.begin_fill()
t.circle(-4)
t.end_fill()
#4
t.penup()
t.setpos(27.4,20)
t.pendown()
t.color('black','orange')
t.fd(5)
t.begin_fill()
t.circle(-4)
t.end_fill()
#5
t.penup()
t.setpos(54,20)
t.pendown()
t.color('black','orange')
t.fd(5)
t.begin_fill()
t.circle(-4)
t.end_fill()
#centre circles
#top
#1
t.penup()
t.setpos(-40,-35)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#2
t.penup()
t.setpos(0,-35)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#3
t.penup()
t.setpos(40,-35)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#center
#1
t.penup()
t.setpos(-80,-85)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#2
t.penup()
t.setpos(-40,-85)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#3
t.penup()
t.setpos(0,-85)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#4
t.penup()
t.setpos(40,-85)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#5
t.penup()
t.setpos(80,-85)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#bottom
#1
t.penup()
t.setpos(-120,-135)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#2
t.penup()
t.setpos(-80,-135)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#3
t.penup()
t.setpos(-40,-135)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#4
t.penup()
t.setpos(0,-135)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#5
t.penup()
t.setpos(40,-135)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#6
t.penup()
t.setpos(80,-135)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#7
t.penup()
t.setpos(120,-135)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(6)
t.end_fill()
#balloon
t.penup()
t.setpos(-140,-100)
t.pendown()
t.fd(180)
t.penup()
t.right(90)
t.fd(10)
t.color('red')
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()
#b2
t.pencolor('black')
t.penup()
t.setpos(140,-100)
t.left(90)
t.pendown()
t.fd(180)
t.penup()
t.right(90)
t.fd(10)
t.color('yellow')
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()
#b3
t.pencolor('black')
t.penup()
t.setpos(-140,-100)
t.pendown()
t.left(115)
t.fd(180)
t.penup()
t.right(90)
t.fd(10)
t.color('blue')
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()
#b4
t.pencolor('black')
t.penup()
t.setpos(-140,-100)
t.left(45)
t.pendown()
t.fd(180)
t.penup()
t.right(90)
t.fd(10)
t.color('green')
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()
#b5
t.pencolor('black')
t.penup()
t.setpos(140,-100)
t.left(130)
t.pendown()
t.fd(180)
t.penup()
t.right(90)
t.fd(10)
t.color('orange')
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()

#b6
t.pencolor('black')
t.penup()
t.setpos(140,-100)
t.left(48)
t.pendown()
t.fd(180)
t.penup()
t.right(90)
t.fd(10)
t.color('orange')
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()
t.penup()
t.setx(-350)
t.sety(-250)
t.pendown()
t.pencolor("red")
t.write('HAPPY BIRTHDAY ANJALI MAM',font=("Arial", 35, "normal"))
t.hideturtle()
turtle.done()


