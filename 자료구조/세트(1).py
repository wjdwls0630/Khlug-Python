first=["김봉민", "김태민", "이주형", "임연수"]
second=["김봉민", "이주형", "임연수", "임채언"]
first_set=set(first)
second_set=set(second)
print("2개의 모임에 모두 참여한 사람은 다음과 같습니다.")
print(first_set&second_set)

file=open("CountingStars.txt","r")
words=[]
for line in file :

    lineword=line.split()
    words.extend(lineword)


print(words)
words_set=set()
for word in words :
    if "'" in word :
        word_input1=word.replace("'","")
        words_set.add(word_input1.lower())
    elif "," in word :
        word_input1=word.replace(",","")
        words_set.add(word_input1.lower())
    elif " " in word :
        word_input1=word.replace(" ","")
        words_set.add(word_input1.lower())
    else:
        word_input1=word.lower()
        words_set.add(word_input1)

print("사용된 단어의 개수 :",len(words_set))
print(words_set)

