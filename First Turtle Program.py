import turtle

wn = turtle.Screen()
wn.bgcolor("orange")

graphic=turtle.Turtle()


graphic.shape('classic')
graphic.color('white')

head = 5

pen = 10

graphic.setheading(head)
graphic.pensize(pen)

graphic.left(90)

graphic.forward(100)

graphic.right(90)
graphic.forward(50)
graphic.right(90)
graphic.forward(50)
graphic.right(90)
graphic.forward(50)



s=turtle.Turtle()
s.shape('circle')
s.color('blue')

s.penup()


s.setposition(200,120)
s.pendown()
s.left(180)
s.forward(50)
s.left(90)
s.forward(50)
s.left(90)
s.forward(50)
s.right(90)
s.forward(50)
s.right(90)
s.forward(50)

s.penup()


wn.exitonclick()
