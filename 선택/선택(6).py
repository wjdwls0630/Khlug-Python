#중첩 if-else문 도전과제 2
while True :
    try :
        month_31 = (1, 3, 5, 7, 8, 10, 12)
        month_30 = (4, 6, 9, 11)
        user_year = int(input("연도를 입력하세요 : "))
        user_month = int(input("월을 입력하세요 :"))
        if user_year>=0 and 0<user_month<13 :
            if (user_year%4==0 and not user_year%100==0) or user_year%400==0 :
                if user_month in month_31 :
                    print("월의 날 수는 31일입니다.")
                elif user_month in month_30:
                    print("월의 날 수는 30일입니다.")
                else :
                    print("월의 날 수는 29일입니다.")
            else :
                if user_month in month_31 :
                    print("월의 날 수는 31일입니다.")
                elif user_month in month_30:
                    print("월의 날 수는 30일입니다.")
                else :
                    print("월의 날 수는 28일입니다.")
            break
        else :
            print("You can only choose integer number in year  that greater than or equal to 0\n"
                  "You can only choose integer number in month between 1 and 12")
    except ValueError:
        print("You can only choose integer number in year  that greater than or equal to 0\n"
              "You can only choose integer number in month between 1 and 12")

#중첩 if-else문 도전과제 3
while True :
    hundred = {1: "백", 2: "이백", 3: "삼백", 4: "사백", 5: "오백", 6: "육백", 7: "칠백", 8: "팔백", 9: "구백"}
    ten = {0: "", 1: "십", 2: "이십", 3: "삼십", 4: "사십", 5: "오십", 6: "육십", 7: "칠십", 8: "팔십", 9: "구십"}
    one = {0: "", 1: "일", 2: "이", 3: "삼", 4: "사", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}
    number = input("숫자를 입력하세요 :")
    if 1<=len(number)<=3 :
        if len(number)==3 :
            print("{0}{1}{2}".format(hundred.get(int(number[0])),ten.get(int(number[1])),one.get(int(number[2]))))
        elif len(number)==2 :
            print("{0}{1}".format(ten.get(int(number[0])),one.get(int(number[1]))))
        else :
            print(one.get(int(number[0])))
        break
    else :
        print("1-999사이로 입력하세요!")
        continue

#중첩 if-else문 도전과제 4
import time
now = time.localtime()
print("현재 시간은",time.asctime())
if 3<=now.tm_mon<=5:
    print("봄입니다.")
elif now.tm_mon<=8:
    print("여름입니다.")
elif now.tm_mon<=11:
    print("가을입니다.")
else : print("겨울입니다.")

if 6<=now.tm_hour<=11:
    print("Good morning")
elif now.tm_hour<=17:
    print("Good afternoon")
elif now.tm_hour<=21 :
    print("Good evening")
else : print("Good night")
