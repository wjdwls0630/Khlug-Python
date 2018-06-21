#연속적인 if-else문 도전과제 1
while True :
    try :
        score=int(input("성적을 입력하시오. : "))
        if score in range(0,101):
            if 95<=score<=100  :
                print("학점 A+")
            elif score>=90 :
                print("학점 A0")
            elif score>=85 :
                print("학점 B+")
            elif score>=80 :
                print("학점 B0")
            elif score>=75 :
                print("학점 C+")
            elif score>=70 :
                print("학점 C0")
            elif score>=65 :
                print("학점 D+")
            elif score>=60 :
                print("학점 D0")
            else: print("학점 F")
            break
        else :
            print("You can only choose integer between 0 and 100! please enter again!")
    except ValueError :
        print("You can only enter integer!")

#연속적인 if-else문 도전과제 2
number=int(input("정수를 입력하시오 : "))
if number>0:
    print("입력된 정수",number,"는 양수입니다.")
elif number==0:
    print("입력된 정수 0은 0입니다")
else : print("입력된 정수",number,"는 음수입니다.")

#연속적인 if-else문 도전과제 2


