user_string=input("문장을 입력하세요! : ")
result=[]
if len(user_string)%2==0 :
    for i in range(len(user_string)) :
        if user_string[i]==user_string[len(user_string)-1-i] :
            result.append(True)
        else:
            result.append(False)
else:
    for i in range(len(user_string)) :
        if user_string[i] == user_string[len(user_string) - 1 - i]:
            result.append(True)
        else:
            result.append(False)
if all(result) :
    print("회문입니다.")
else:
    print("회문이 아닙니다.")

user_words=user_string.split()
output_string=""
for word in user_words :
    output_string+=word[0].upper()
print(output_string)

user_email=input("이메일을 입력하세요 ! : ")
user_id, user_domain=user_email.split("@")
print(user_id)
print(user_domain)

string="please don't see just a boy caught up in dreams and fantasy"
string_dict=dict()
for letter in string :
    if letter.isalpha() :
        string_dict['alpha']=string_dict.get('alpha',0)+1
    elif letter.isdigit() :
        string_dict['digit']=string_dict.get('digit',0)+1
    elif " " is letter :
        string_dict['space']=string_dict.get('space',0)+1

print(string_dict)




