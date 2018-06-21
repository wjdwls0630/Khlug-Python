ID_Password={}
ID=input("Set a new ID : ")
Password=input("Set Password : ")
ID_Password[ID]=Password
print(ID_Password)
while True :
    Service_ID=input("Enter ID : ")
    Service_Password=input("Enter Password : ")
    if Service_ID in ID_Password.keys() :
        if ID_Password.get(Service_ID)==Service_Password :
            print("환영합니다! 이제 사용하실 수 있습니다!")
            break
        else : print("잘못된 패스워드 입니다! 다시 입력해주십시오.")
    else : print("알 수 없는 사용자입니다!")
print("You can use service!")
nick=input("Set your nick name : ")
print("you can use Calculation Program")
class FourCal :
    def setdata(self,first,second):
        set.first=first
        self.second=second
    def sum(self):
        result= self.first+self.second
        return result
    def sub(self):
        result= self.first-self.second
        return result
    def mul(self):
        result= self.first*self.second
        return result
    def div(self):
        result= self.first/self.second
        return result
a=Fourcal()
