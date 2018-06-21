while True :
    try :
        user_shape=int(input("도형을 입력하세요 (1 : 사각형, 2 : 삼각형 , 3 : 원) : "))
        if 1<=user_shape<=3 :
            if user_shape==1 :
                a=float(input("가로 : "))
                b=float(input("세로 : "))
                print("면적 =",a*b)
            elif user_shape==2 :
                a=float(input("밑변 : "))
                b=float(input("높이 : "))
                print("면적 =",0.5*a*b)
            else :
                from math import pi
                r=float(input("반지름 : "))
                print("면적 =",pi*pow(r,2))
            break
        else : print("You can only enter a interger number between 1 and 3.")
    except ValueError :
        print("You can only enter a interger number between 1 and 3.")