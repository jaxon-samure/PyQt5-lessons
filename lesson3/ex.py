import os 
os.system("clear")



def atoi(s: str):
    numb = ''
    
    for i in range(len(s)):
        s = s.strip()
        if ord(s[i]) >= 48 and ord(s[i]) <= 57 or s[i]== "-" :
            numb+=s[i]
        else:
            if s[i] == " ":
                continue
            if numb == '-':
                return 0
            return int(numb) if numb  else 0
        if i == len(s)-1:
            return int(numb) if numb  else 0
    
a = atoi("-012 44ag323")
print(a)