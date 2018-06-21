#while문 도전과제 1
print("="*60)

number1=int(input("정수 입력 : "))
a=0
while a<number1 :
    print(a, end=" ")
    a=a+1


print("\n"+"="*60)
#while문 도전과제 2

number2=int(input("정수 입력 : "))
b=0
sum=0
while b<=number2 :
    sum=sum+b
    b = b + 1
print("합계 :",sum)

print("="*60)
#whil문 도전과제 3

number3=int(input("정수를 입력하세요 : "))
c=1
mul=1
while c<=number3 :
    mul=mul*c
    c=c+1

print("{0} !은 {1}입니다.".format(number3,mul))

print("="*60)

#while문 도전과제 4
number4=int(input("정수 입력 : "))
d=1
while d<10 :
    print("{0} * {1} = {2}".format(number4,d,number4*d))
    d = d + 1

print("="*60)

#while문 도전과제 5
number5=input("정수 입력 : ")
e=0
sum1=0
while e<len(number5) :
    sum1=sum1+int(number5[e])
    e=e+1

print("자리수의 합은 %d 입니다." %sum1)

print("="*60)

#whil문 도전과제 6
number6=int(input("정수 입력 : "))
print("범위는 처음 숫자는 포함 마지막 숫자는 포함하지 않습니다.")
number7=int(input("처음 숫자를 정하세요. : "))
number8=int(input("마지막 숫자를 정하세요 : "))
number9=number7
sum2=0
while number7<number8 :
    if number7%number6==0 :
        sum2=sum2+number7

    number7=number7+1

print("{0} 과 {1} 사이의 모든 {2}의 배수의 합은 {3}입니다.".format(number9,number8,number6,sum2))

print("="*60)

#while문 도전과제 7
x=int(input("정수를 입력하세요 (큰 수) : "))
y=int(input("정수를 입력하세요 (작은 수) : "))
while y!=0 :
    r=x%y
    x=y
    y=r

print("최대 공약수는 %d 입니다." %x)

print("="*60)






