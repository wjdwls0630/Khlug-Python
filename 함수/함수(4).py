
def gradiednt_yintercept(x1,y1,x2,y2) :
    gradiednt=(y2-y1)/(x2-x1)
    yintercept=gradiednt*(0-x1)+y1
    return gradiednt,yintercept

x1=float(input("x1 = "))
y1=float(input("y1 = "))
x2=float(input("x2 = "))
y2=float(input("y2 = "))
gradient, yintercept=gradiednt_yintercept(x1,y1,x2,y2)
print("기울기 = {}, y절편 = {}".format(gradient,yintercept))
