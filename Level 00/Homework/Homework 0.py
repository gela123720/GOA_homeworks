from turtle import *

#we want to paint a house

#step 1:  draw a square

speed(20)
width(7)
color("purple")
begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#step 2:  draw a door

forward(70)

color("yellow")
begin_fill()

left(90)

forward(120)   #height of the door
right(90)

forward(60)
right(90)

forward(120)

end_fill()

penup()
goto(200,200)
pendown()

#step 3: draw a roof

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#step 4:  draw windows

#window 1

color("brown")
begin_fill()
penup()
goto(30,150)
pendown()

right(150)
forward(25)

right(90)
forward(25)

right(90)
forward(25)

right(90)
forward(25)
end_fill()

#window 2

color("brown")
begin_fill()
penup()
goto(170,175)
pendown()

forward(25)
left(90)

forward(25)
left(90)

forward(25)
left(90)

forward(25)
left(90)
end_fill()


exitonclick()