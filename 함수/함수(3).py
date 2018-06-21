# 함수가 정의됩니다.
def sub(mylist):
	# 리스트가 함수로 전달됩니다.
	mylist = [1, 2, 3, 4]	# 새로운 리스트가 매개변수로 할당됩니다.
	print("함수 내부에서의 mylist :", mylist)
	return

# 여기서 sub() 함수를 호출합니다.
mylist = [10, 20, 30, 40]
sub(mylist)
print("함수 외부에서의 mylist :", mylist)

from math import pi

constant=pi
def space_length(user_radius) :
    space=constant*(user_radius**2)
    length=2*constant*user_radius
    result="원의 면적 : {}\n원의 둘레 : {}".format(space,length)
    return result

user_radius=float(input("원의 반지름을 입력하세요. : "))
print(space_length(user_radius))