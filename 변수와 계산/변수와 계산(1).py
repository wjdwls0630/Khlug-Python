#변수의 소개 도전과제
x=10
y=20
x,y=y,x
print("x :",x)
print("y :",y)

x=10
y=20
tmp=x
x=y
y=tmp
print("x :",x)
print("y :",y)


#수식과 연산자 도전과제 1
f=lambda x : 3*pow(x,2)+7*x+9
print(f(2))
g=lambda x : pow(x,3)+3*pow(x,2)+7*x+10
print(g(3))

#수식과 연산자 도전과제 2
number=int(input("참석자의 수를 입력하시오. :"))
print("치킨의 수 : {0}".format(number))
print("맥주의 수 : {0}".format(number*2))
print("과자의 수 : {0}".format(number*4))

#연산자의 우선수위 도전과제
day=0
week=0
potato=35

while day<365:
    day=day+1
    if potato>0:
        potato=potato-3
    else :
        pass
    if day%7==0:
        week=week+1
        potato=potato-10+40
    if day==365:
        print("1년이 지났습니다.")
print("Week: {0},Day : {1}, Potato : {2}".format(week,day,potato))




