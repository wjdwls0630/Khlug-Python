from math import pi
def space_length(user_radius) :
    space=pi*(user_radius**2)
    length=2*pi*user_radius
    return space, length
user_radius=float(input("원의 반지름을 입력하세요. : "))
space, length = space_length(user_radius)

print("원의 넓이는 {}이고 원의 둘레는 {}입니다.".format(space,length))