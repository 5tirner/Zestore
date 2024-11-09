from .models import usersInfos
import random, string

def checkPass(Pass:str):
    digits:int = 0
    upperChar:int = 0
    lowerChar:int = 0
    uniqueChar:int = 0
    for i in Pass:
        if i.islower():
            lowerChar += 1
        elif i.isupper():
            upperChar += 1
        elif i.isdigit():
            digits += 1
        elif i.isprintable():
            uniqueChar += 1
    print("ALL:", digits, upperChar, lowerChar, uniqueChar)
    if digits == 0 or upperChar == 0 or lowerChar == 0 or uniqueChar == 0:
        print("Password Is Weak")
        return False
    return True

def checkUsername(Username:str):
    usernameLen:int = len(Username)
    if usernameLen < 4 or usernameLen > 12:
        print('Username To Short/long.')
        return "\\"
    while True:
        try:
            Username += '_' + ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = 7))
            print(f'Check This Username={Username}')
            usersInfos.objects.get(UserName=Username)
            print(f'Used')
        except:
            print('Not Used')
            break
    return Username

def checkEmail(Email:str):
    saveEmail = Email.lower()
    Sufix:str = saveEmail[-10::]
    print(Sufix)
    if Sufix != "@gmail.com" or saveEmail.count("@gmail.com") != 1:
        print("Gmail Is Invalid")
        return False
    try:
        DupEmail = usersInfos.objects.get(Email=saveEmail)
        print(DupEmail)
        return False
    except:
        print("Not Usable Email")
    return True