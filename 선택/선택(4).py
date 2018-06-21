#논리연산자 도전과제 1
sum_grade=int(input("이수한 학점을 입력하세요 : "))
gpa=float(input("평점을 입력하세요 : "))
if sum_grade>=140 and gpa>=2.0 :
    print("졸업 가능합니다!")
else: print("졸업 불가능합니다.")

#논리연산자 도전과제 2
result=int(input("실적을 입력하세요 (단위 : 만원) : "))
if result >=1000:
     bonus=round((result-1000)*0.1,1)
     print("실적 달성 보너스 :",bonus)
else :
    print("실적 목표에 도달하지 못했습니다.")