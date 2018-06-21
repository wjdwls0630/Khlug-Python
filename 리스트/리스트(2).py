friend_list=[]
def template() :
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")

def menu_1() :
    print(friend_list)
    show_menu()

def menu_2() :
    new_friend=input("이름을 입력하세요. (메뉴로 돌아가려면 9 입력) : ")
    if new_friend=="9" :
        show_menu()
    else:
        friend_list.append(new_friend)
        print("추가 완료!")
        show_menu()


def menu_3() :
    del_friend=input("삭제하려는 이름을 입력하세요. (메뉴로 돌아가려면 9 입력) :  ")
    if del_friend=="9" :
        show_menu()
    else:
        if del_friend in friend_list:
            friend_list.remove(del_friend)
            print("삭제 완료!")
            show_menu()
        else:
            print("이름이 발견되지 않았습니다.")
            menu_3()


def menu_4() :
    change_friend=input("변경하려는 이름을 입력하세요 (메뉴로 돌아가려면 9 입력) : ")
    if change_friend=="9" :
        show_menu()
    else:
        if change_friend in friend_list :
            update_friend = input("새로운 이름을 입력하세요 : ")
            change_friend_index=0
            for i in range(len(friend_list)) :
                if friend_list[i]==change_friend :
                    change_friend_index=i
            friend_list[change_friend_index]=update_friend
            print("수정 완료!")
            show_menu()
        else:
            print("이름이 발견되지 않았습니다.")
            menu_4()

def show_menu():
    print("=" * 60)
    template()
    choice_menu = int(input("메뉴를 선택하세요 : "))
    if choice_menu == 1:
        menu_1()
    elif choice_menu == 2:
        menu_2()
    elif choice_menu == 3:
        menu_3()
    elif choice_menu == 4:
        menu_4()
    elif choice_menu == 9:
        print("프로그램 종료!")
    else:
        print("메뉴를 잘못 입력했습니다 다시 입력하세요!")
        show_menu()



show_menu()
print("=" * 60)



