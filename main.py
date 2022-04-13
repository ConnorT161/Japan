
import turtle

t = turtle.Turtle()

t.forward(100)
t.right(180)
for x in range (2):
  t.forward(200)
  t.right(90)
  t.forward(100)
  t.right(90)

t.forward(100)
t.right(90)
t.pu()
t.forward(20)
t.right(90)
t.pd()
t.color("red", "red")
t.begin_fill()
for x in range (180):
  t.forward(1)
  t.left(2)
t.end_fill()
t.color("black","white")
t.pu()
t.right(90)
t.forward(20)
t.right(90)
t.forward(100)
t.left(180)
t.pd()
for x in range (2):
  t.forward(200)
  t.right(90)
  t.forward(100)
  t.right(90)
t.forward(66)
t.color("blue","blue")
t.right(90)
t.forward(100)