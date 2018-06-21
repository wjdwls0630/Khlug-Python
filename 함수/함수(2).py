#인수와 매개변수 도전문제 1
def sphereVolume(user_radius) :
    from math import pi
    result = pow(user_radius,3)*((4*pi)/3)
    return result



user_radius=float(input("구의 반지름을 입력하세요 : "))
print(sphereVolume(user_radius))


def make_password() :
    from string import ascii_lowercase,ascii_uppercase
    from random import choice,randint
    alpha_lower_list=list(ascii_lowercase)
    alpha_upper_list=list(ascii_uppercase)
    number_list=list(range(10))
    all_list=[alpha_lower_list,alpha_upper_list,number_list]
    password_length=randint(8,16)
    password=""
    for i in range(password_length) :
        choice_first_step=choice(all_list)
        choice_one=choice(choice_first_step)
        password+=str(choice_one)
    return password



def test_password(password) :
    password_list=list()
    digit_list=list()
    lower_list=list()
    upper_list=list()
    for item in password :
        if item.isdigit() :
            digit_list.append(item)
        elif item.islower() :
            lower_list.append(item)
        else:
            upper_list.append(item)
    if len(digit_list)>=1 and len(lower_list)>=1 and len(upper_list)>=1 :
        result=True
    else:
        result=False
    return result

password=make_password()
while test_password(password)!=True :
    password=make_password()

print(password)








