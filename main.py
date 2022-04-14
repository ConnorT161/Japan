
import turtle

t = turtle.Turtle()

_input = input("France or Japan flag?\n")
  
_input = _input.lower()


def japan():
  
  t.color("black","white")
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


def france():
  t.color("black","white")
  for x in range (2):
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.begin_fill()
    
  for x in range (2):
    t.forward(66)
    t.color("blue","blue")
    t.right(90)
    t.forward(100)
    t.right(90)
  t.forward(66)
  t.end_fill()
  t.pu()
  t.forward(67)
  t.pd()
  t.color("red","red")
  t.begin_fill()
  for x in range (2):
    t.forward(66)
    
    t.right(90)
    t.forward(100)
    t.right(90)
  t.end_fill()

while True:
  if _input == ("japan"):
    japan()
  elif _input == ("france"):
    france()
  else:
    print("try again")
  _input = input("France or Japan flag?\n")
  t.clear()
  _input = _input.lower()


  
