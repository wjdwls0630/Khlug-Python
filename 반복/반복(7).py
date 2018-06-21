#문자열 처리하기 연습과제

print("="*60)

from random import random,randint
from math import sqrt,pi
n=int(input("반복횟수를 입력하시오 : "))
inside=0
for a in range(n) :
    x=random()
    y=random()
    if sqrt(pow(x,2)+pow(y,2))<=1:
        inside=inside+1

exp_pi=4*inside/n
diff_rate=abs(exp_pi-pi)/pi*100
print("실험결과 파이는 {0} 실제 파이 값은 {1} 오차율은 약 {2}%입니다.".format(exp_pi,pi,diff_rate))

print("="*60)

#문자열 처리하기 도전과제 1
sentence=input("쓰고 싶은 문장을 입력하세요 : ")
space_number=0
number_number=0
word_number=0
for word in sentence :
    if word==" " :
        space_number=space_number+1
    elif word in ["0","1","2","3","4","5","6","7","8","9"] :
        number_number=number_number+1
    else :
        word_number=word_number+1
print("띄어쓰기 개수 : {0}\n숫자 개수 : {1}\n문자 개수 : {2}".format(space_number,number_number,word_number))

print("="*60)

#문자열 처리하기 도전과제 2
exp_num=int(input("주사위를 굴릴 횟수를 정하세요 : "))
exp_sum=[0,0,0,0,0,0,0,0,0,0,0,0,0]
ideal_sum=[0,0,0,0,0,0,0,0,0,0,0,0,0]

for a in range(exp_num):
    first=randint(1,6)
    second=randint(1,6)
    exp_sum[first+second]=exp_sum[first+second]+1

for b in range(1,7) :
    for c in range(1,7) :
        ideal_sum[b+c]=ideal_sum[b+c]+1

total=6*6
def diff_rate(a,b):
    result=round(abs(a-b)/b*100,9)
    return result

for i in range(2,13) :
    P_exp =exp_sum[i]/exp_num*100
    P_ideal=ideal_sum[i]/total*100
    print("합이 {}가 되는 실험확률은 약 {}% 이론확률은 약 {}% 오차율은 약 {}%입니다.\n".format(
        i,round(P_exp,2),round(P_ideal,2),diff_rate(P_exp,P_ideal)))


print("="*60)