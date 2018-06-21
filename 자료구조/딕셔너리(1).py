file=open("CountingStars.txt","r")
words=[]
for line in file :
    lineword=line.split()
    words.extend(lineword)

print(words)
words_dict=dict()
for word in words :
    words_dict[word]=words_dict.get(word,0)+1

print(words_dict)

string="Red velvet is one of the most famous idol girlgroup in the universe"
string_dict=dict()
for letter in string :
    string_dict[letter]=string_dict.get(letter,0)+1

items_list=list(string_dict.items())
items_list.sort(key=lambda tup : tup[1] , reverse=True)
print(items_list)


user_want=int(input("원하는 피보나치 수열의 번호를 입력하세요! : "))
fib_table={}
for i in range(1,user_want+1) :
    if i<=2 :
        fib_table[i]=1
    else:
        fib_table[i] = fib_table.get(i, 0) + fib_table[i - 1] + fib_table[i - 2]


def fib(n) :
    return fib_table[n]

print(fib(user_want))

rows=int(input("원하는 행의 개수를 입력하세요! : "))
cols=int(input("원하는 열의 개수를 입력하세요! : "))
matrix_table={}
for i in range(1,rows+1) :
    for j in range(1,cols+1) :
        if i!=1 and j==3:
            matrix_table[(i,j)]=matrix_table.get((i,j),0)+i-1
        else:
            matrix_table[i, j] = matrix_table.get((i, j), 0)

for i in range(1,rows+1) :
    for j in range(1,cols+1) :
        print(matrix_table[i,j],end='\t')
    print()


