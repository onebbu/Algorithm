str = input()
answer = ""
for i in range(len(str)):
    if str[i:i+1].isupper() == True :
        answer = answer+str[i:i+1].lower()
    else:
        answer = answer + str[i:i + 1].upper()
print(answer)