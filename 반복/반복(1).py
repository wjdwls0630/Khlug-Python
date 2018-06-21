#반복문을 이용한 터틀 그래픽
#sin 그래프 그리기
import math
import turtle
t= turtle.Pen()
t.shape("turtle")

for angle in range(360) :
    y= math.sin(math.radians(angle))
    scaledX =angle
    scaledY = y*100
    t.goto(scaledX,scaledY)

turtle.done()
