import os 
os.system("clear")



def atoi(s: str):
    numb = ''
    
    for i in range(len(s)):
        if ord(s[i]) >= 48 and ord(s[i]) <= 57 or s[i]== "-" :
            numb+=s[i]
        else:
            if numb == '-':
                return 0
            return int(numb) if numb  else 0
        if i == len(s)-1:
            return int(numb) if numb  else 0
    
a = atoi("-01244ag323")
print(a)