#for문 도전과제 1
print("="*60)

number1=int(input("어디까지 계산할까요? : "))
sum=0
for i in range(number1+1) :
    sum=sum+i


print("1부터 {0} 까지의 정수의 합 = {1}".format(number1,sum))

print("="*60)
#for문 도전과제 2

number2=int(input("정수를 입력하세요 : "))
mul=1
for i in range(1,number2+1) :
    mul=mul*i

print("{0} !은 {1}입니다.".format(number2,mul))

print("="*60)
#for문 도전과제 3

number3=int(input("초기 숫자를 입력하세요 : "))
a=list(range(1,number3+1))
a.reverse()
for i in a :
    print(i, end=" ")

print("Happy New year!")

print("="*60)
#for문 도전과제 4

def convert_F_to_C(F) :
    C=(F-32)*5/9
    return C

for i in range(0,101,10) :
    print("{0} -> {1}".format(i,round(convert_F_to_C(i),2)))

print("="*60)


