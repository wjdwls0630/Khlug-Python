#2차원 리스트란? 도전과제
num_list=list(range(1,7))
all_list=[]
for i in num_list :
    result_list=[]
    for j in num_list :
        item=i+j
        result_list.append(item)
    all_list.append(result_list)

for k in all_list :
    print(k,end="\n")
print()