#조건문 2
import turtle
t=turtle.Pen()
t.shape("turtle")
t.pencolor("red")

time=10
while time>0 :
    time=time-1
    command=input("명령을 입력하십시오.(왼쪽은 left, 오른쪽은 right) : ")
    if command=="left":
        t.left(60)
        t.forward(50)
    else :
        t.right(60)
        t.forward(50)

