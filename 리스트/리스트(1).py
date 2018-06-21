user_input=int(input("몇까지 하시겠습니까? : "))
pythagoras_list=[(x,y,z) for x in range(1,user_input+1) for y in range(1,user_input+1) for z in range(1,user_input+1) if x**2+y**2==z**2]
print(pythagoras_list)