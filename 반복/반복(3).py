#for 문 도전과제 5
import turtle
t=turtle.Pen()
t.shape("turtle")
for i in range(5) :
    t.forward(100)
    t.right(144)
t.reset()
for i in range(6) :
    t.forward(100)
    t.right(60)
t.reset()
for i in range(8) :
    t.forward(100)
    t.right(45)
t.reset()
t.left(15)
for l in range(3):
    t.left(15)
    for i in range(4):
        t.forward(100)
        t.left(90)
t.reset()
#for문 도전과제 6
window=turtle.Screen()
window.bgcolor("lightgreen")
color=["yellow", "red", "purple","blue"]
for i in color :
    t.pencolor(i)
    t.forward(200)
    t.left(90)



turtle.done()

