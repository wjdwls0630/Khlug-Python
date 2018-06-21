#조건문 도전과제 1
weather=input("Enter Today's weather : ")
umb=input("Do you have umbrella now? : ")
if weather=="rainy":
    if umb=="yes":
        print("You can go outside!")
    else :
        print("You must stay until the rain stops!")

else : print("You can go outside!")

#조건문 도전과제 3

number=int(input("Enter a integer number :"))
if number%2==0 :
    print("입력된 정수",number,"짝수입니다.")
else : print("입력된 정수",number,"홀수입니다.")

if number%3==0 :
    print("입력된 정수", number," 3의 배수입니다.")
else : print("입력된 정수", number,"은 3의 배수가 아닙니다.")

#조건문 도전과제 4
first_number=int(input("첫 번째 정수 입력 : "))
second_number=int(input("두 번째 정수 입력 : "))
if first_number>second_number:
    print("큰 수는",first_number,"작은 수는",second_number)
elif first_number<second_number:
    print("큰 수는",second_number,"작은 수는",first_number)
else: print("두 수는 똑같습니다.")