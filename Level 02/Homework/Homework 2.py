from turtle import *

width(3)
speed(10000000000000)

#step 1: draw a field

color("green")
penup()
goto(950,349)
pendown()
begin_fill()

right(90)
forward(995)

right(90)
forward(1905)

right(90)
forward(995)

right(90)
forward(1905)

end_fill()


#step 2: draw a tower

color("gray")
penup()
goto(-250,-250)
pendown()
begin_fill()

forward(250)
left(90)

forward(550)
left(90)

forward(50)
left(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
right(90)

left(90)
forward(500)

left(90)
forward(90)

end_fill()


#step 3: make a door

color("chocolate4")
begin_fill()

left(90)
forward(115)

right(90)
forward(70)

right(90)
forward(115)

end_fill()

#step 4: make window 1

color("gray")

left(180)
forward(200)

left(90)
forward(10)

color("black")
begin_fill()

left(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

end_fill()


#step 4: make window 2

color("gray")

left(90)
forward(60)

color("black")

begin_fill()

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)

end_fill()


#step 4: make window 3

color("gray")

left(90)
forward(100)

color("black")

begin_fill()

forward(50)
left(90)

forward(50)
left(90)


forward(50)
left(90)


forward(50)
left(90)


end_fill()


#step 5: make a sky

color("cyan")

penup()
goto(950,350)
pendown()

begin_fill()

left(90)
forward(1905)

right(90)
forward(155)

right(90)
forward(1905)

end_fill()


#step 6: make an apple tree

color("chocolate3")

begin_fill()

penup()
goto(700,-300)
pendown()

left(90)
forward(270)

left(90)
forward(50)

left(90)
forward(270)

left(90)
forward(50)

end_fill()

color("dark green")


penup()


left(90)
forward(270)

pendown()

begin_fill()

right(90)
forward(90)

left(90)
forward(200)

left(90)
forward(230)

left(90)
forward(200)

left(90)
forward(90)

end_fill()

#step 7: make a second tower

color("gray")
penup()
goto(100,-250)
pendown()
begin_fill()

forward(250)
left(90)

forward(550)
left(90)

forward(50)
left(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
right(90)

forward(50)
right(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
right(90)

left(90)
forward(500)

left(90)
forward(90)

end_fill()



color("chocolate4")
begin_fill()

left(90)
forward(115)

right(90)
forward(70)

right(90)
forward(115)

end_fill()


color("gray")

left(180)
forward(200)

left(90)
forward(10)

color("black")
begin_fill()

left(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

end_fill()



color("gray")

left(90)
forward(60)

color("black")

begin_fill()

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)

end_fill()



color("gray")

left(90)
forward(100)

color("black")

begin_fill()

forward(50)
left(90)

forward(50)
left(90)


forward(50)
left(90)


forward(50)
left(90)


end_fill()


#step 8: make a bridge between towers

color("gray")

penup()
goto(0,0)
pendown()

begin_fill()

right(90)
forward(100)

left(90)
forward(50)

left(90)
forward(100)

left(90)
forward(50)

end_fill()


#step 9: make a river

color("blue")

penup()
goto(-955,-250)
pendown()

begin_fill()

left(90)
forward(360)

right(90)
forward(100)

left(90)
forward(300)

right(90)
forward(50)

left(90)
forward(300)

right(90)
forward(100)

right(90)
forward(960)

end_fill()


#step 10: make a berry bush

color("Darkgreen")

penup()
goto(-850,100)
pendown()

begin_fill()

right(90)
forward(50)

right(90)
forward(50)

left(90)
forward(50)

right(90)
forward(200)

right(90)
forward(50)

left(90)
forward(50)

right(90)
forward(50)

right(90)
forward(300)

end_fill()

color("red")

penup()
goto(-800,120)
pendown()

forward(1)

penup()
goto(-750,170)
pendown()

forward(1)

penup()
goto(-700,120)
pendown()

forward(1)

penup()
goto(-650,160)
pendown()

forward(1)

penup()
goto(-600,130)
pendown()

forward(1)


#step 11: make a normal bush

color("darkgreen")

penup()
goto(-700,-170)
pendown()

begin_fill()

right(180)
forward(300)

left(90)
forward(50)

left(90)
forward(30)

right(90)
forward(50)

left(90)
forward(200)

left(90)
forward(50)

right(90)
forward(70)

left(90)
forward(50)

end_fill()


#step 12: add some clouds

color("white")
penup()
goto(800,400)
pendown()

begin_fill()

right(180)
forward(30)

left(90)
forward(400)

left(90)
forward(30)

left(90)
forward(400)

end_fill()



penup()
goto(200,440)
pendown()

begin_fill()

left(90)
forward(30)

left(90)
forward(400)

left(90)
forward(30)

left(90)
forward(400)

end_fill()



penup()
goto(-350,420)
pendown()

begin_fill()

right(90)
forward(30)

right(90)
forward(500)

right(90)
forward(30)

right(90)
forward(500)

end_fill()







exitonclick()

