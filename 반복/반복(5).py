#보초값(sentinel)사용하기 예제
#필요한 변수 초기화
score=0
sum=0
n=0
print("종료하려면 0미만 100 초과의 값을 입력하세요.")
#score가 0이상 100이하이면 반복합니다.
#성적을 계속 입력받아 합계를 구하고 학생 수를 센다.
#score가 0이상 100이하의 범위를 벗어나면 계산하지 않고 반복을 끝낸다.
while 0<=score<=100 :
    score=int(input("성적을 입력하세요 : "))
    if 0<=score<=100 :
        sum = sum + score
        n = n + 1
#score를 하나 이상 제대로 받으면 평균을 출력한다
if n>=1 :
    average=sum/n
#score를 처음부터 못 받으면 평균은 0으로 출력한다.
else :
    average=0

print("성적의 평균은 %f 입니다." %average)

print("="*60)
#보초값(sentinel)사용하기 도전문제 1
first=0
second=0
while first >= second :
    try:
        while first >= second:
            first = int(input("시작값을 입력하세요 : "))
            second = int(input("마지막값을 입력하세요 : "))
            if first > second:
                print("시작값이 마지막값 보다 작아야 합니다!")
            elif first == second:
                print("시작값과 마지막값은 같을 수 없습니다!")

    except ValueError:
        print("모든 값은 정수로 입력해야 합니다!")
        continue

from random import randint

answer = randint(first, second)
guess_number = round((second - first + 1) / 20)
default_guess_number = guess_number
print("{0} 과 {1} 사이의 숫자를 맞추세요. 시도 횟수는 {2}".format(first,second,guess_number))
while guess_number > 0:
    try:
        user_input = int(input("숫자를 입력하세요 : "))
        if user_input > answer:
            guess_number = guess_number - 1
            if guess_number>0 :
                print("높음 ! 더 낮은 숫자를 입력하세요.\n시도횟수가 %d번 남았습니다."%guess_number)
        elif user_input < answer:
            guess_number = guess_number - 1
            if guess_number>0:
                print("낮음 ! 더 높은 숫자를 입력하세요.\n시도횟수가 %d번 남았습니다."%guess_number)
        else:
            print("정답입니다! 시도 횟수 =", (default_guess_number - guess_number + 1))
            break
    except ValueError:
        print("모든 값은 정수로 입력해야 합니다!(시도 횟수에는 포함되지 않습니다.)")
        continue

if guess_number==0 :
    print("오답입니다! 정답은", answer)
