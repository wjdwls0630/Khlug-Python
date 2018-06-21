#블록 도전과제 1
pRice=int(input("구입 금액을 입력하시오. :"))
if pRice >= 100000 :
    pRice=pRice*0.95
    print("지불 금액은",int(pRice),"원 입니다.")
else :
    need_pRice=100000-pRice
    print(need_pRice,"원 만큼 더 구입하시면 5% 더 할인 받으실 수 있습니다.")
    print("지불 금액은", pRice, "원 입니다.")

#블록 도전과제 2
word=input("문자열을 입력하시오 : ")
if len(word)%2!=0:
    a=len(word)//2
    print("중앙 글자는",word[a])

else :
    a=len(word)//2
    print("중앙 글자는",word[a-1:a+1])

#블록 도전과제 3
work_time=int(input("근무 시간을 입력하세요 : "))
work_pay=int(input("시간 당 임금을 입력하세요 : "))
if work_time>=40:
    total_pay=int(40*work_pay+(work_time-40)*(work_pay*1.5))
    print("이번주 주급은",total_pay,"원 입니다.")
else :
    total_pay=int(work_pay*work_time)
    print("이번주 주급은",total_pay,"원 입니다.")
