#중첩루프 도전과제 1
sum=0
for a in range(1,101) :
    for b in range(1,101) :
        for c in range(1,101) :
            if pow(a,2)+pow(b,2)==pow(c,2) :
                print(a,b,c)
                sum=sum+1
print("총 %d가지"%sum)

print("="*60)

#중첩루프 도전과제 2

print("<주사위를 2개를 던졌을 때 합이 6이 되는 경우")
sum1=0
for a in range(1,7) :
    for b in range(1,7) :
        if a+b==6 :
            print(a,b)
            sum1=sum1+1
print("총 %d가지"%sum1)

print("="*60)

print("<주사위를 3개를 던졌을 때 합이 10이 되는 경우")
sum2=0
for a in range(1,7) :
    for b in range(1,7) :
        for c in range(1,7) :
            if a+b+c==10 :
                print(a,b,c)
                sum2=sum2+1
print("총 %d가지"%sum2)

print("="*60)

#중첩루프 도전과제 3
for a in range(1,6):
    print("x^%d"%a,end=" ")
print()
for a in range(1,11) :
    for b in range(1,6) :
        print("{}".format(pow(a,b)),end="\t")
    print()


print("="*60)




