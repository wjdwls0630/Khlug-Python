#함수 호출이란? 도전과제
from math import sqrt
line_length=lambda a,b : sqrt(pow(a,2)+pow(b,2))

time=10/20+line_length(3,4)/10+line_length(3,4)/30+8/20

print(str(round(time,2))+"시간이 걸립니다")


#자료형 도전과제 1
from math import pi
rAdius=int(input("반지름을 입력하시오.: "))
vOlume=4/3*pi*pow(rAdius,3)
sUrface=4*pi*pow(rAdius,2)
print("반지름이 {0}인 구의 부피는 {1} , 구의 면적은{2} 입니다.".format(rAdius,vOlume,sUrface))

#자료형 도전과제 2
pRice=int(input("물건값을 입력하시오 : "))
my_thousand=int(input("1000원 지폐 개수 : "))
my_five_hundred=int(input("500원 동전 개수 : "))
my_hundred=int(input("100원 동전 개수 : "))

remain=((1000*my_thousand+500*my_five_hundred+100*my_hundred)-pRice)

remain_thousand=remain//1000
remain_five_hundred=(remain-1000*remain_thousand)//500
remain_hundred=(remain-1000*remain_thousand-500*remain_five_hundred)//100
remain_ten=(remain-1000*remain_thousand-500*remain_five_hundred-100*remain_hundred)//10
remain_one=(remain-1000*remain_thousand-500*remain_five_hundred-100*remain_hundred-10*remain_ten)

print("거스름돈은 {0} 결과는 1000원 {1}개, 500원 {2}개, 100원 {3}개, 10원 {4}개, 1원 {5}개입니다.".format
    (remain,remain_thousand,remain_five_hundred,remain_hundred,remain_ten,remain_one))

#문자열 도전과제
first_word=input("첫 번째 단어를 입력해주세요 :")
second_word=input("두 번째 단어를 입력해주세요 :")
third_word=input("세 번째 단어를 입력해주세요 :")
print(first_word[0]+second_word[0]+third_word[0])

