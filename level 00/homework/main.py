from turtle import*

width(5)
speed(0)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

# door

left(90)
forward(65)

color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(70)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(135)
forward(135)
left(87)
forward(140)
left(138)
forward(200)
end_fill()

# first window

penup()
goto(20, 180)
pendown()

color("black")
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)

# second window

penup()
goto(180,180)
pendown()

left(180)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

left(90)
forward(20)
left(90)
forward(40)

right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)

exitonclick()