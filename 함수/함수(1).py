#함수 작성 예 power() 도전 문제 1
def factorial1(n) :
    if n==1 :
        return 1
    return n*factorial1(n-1)

def factorial2(n) :
    result=1
    for i in range(1,n+1) :
        result=result*i
    return result

print(factorial1(3))
print(factorial2(5))

#함수 작성 예 power() 도전 문제 2
username=input("이름을 입력하세요 : ")
def happyBirthday(username) :
    print("생일 축하합니다~\n"+"생일 축하합니다~")
    print("사랑하는",username,"(호우)")
    print("생일 축하합니다!")

happyBirthday(username)

#함수 작성 예 power() 도전 문제 3
def FtoC(user_f):
    result = (user_f-32)/1.8
    return result

user_f=float(input("화씨 온도를 입력하세요 : "))
print("섭씨 온도는 {} 도 입니다.".format(FtoC(user_f)))

#함수 작성 예 power() 도전 문제 4
def is_prime(n) :
    divisor_list=[]
    for i in range(1,n+1) :
        if n%i==0 :
            divisor_list.append(i)
    if len(divisor_list)<=2 :
        result=True
    else:
        result=False
    return result
user_integer=int(input("정수를 입력하세요 : "))
if is_prime(user_integer) :
    print("{}은(는) 소수입니다.".format(user_integer))
else:
    print("{}은(는) 소수가 아닙니다.".format(user_integer))

def find_prime(n) :
    prime_list=[]
    for i in range(1,n+1) :
        if is_prime(i) :
            prime_list.append(i)
    return prime_list
user_number = int(input("어디까지 찾으시겠습니까? : "))
out_prime_list=""
for item in find_prime(user_number) :
    out_prime_list+=str(item)+" "
print("1 부터 {} 사이의 모든 소수는 {}입니다.".format(user_number,out_prime_list))


