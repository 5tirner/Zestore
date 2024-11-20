from django.shortcuts import render
import requests, os, dotenv, random, string
from django.http import HttpResponseRedirect
from .checkInput import checkUsername
from .sendVerfCode import sendCodeVerefication
from .models import verificationSystem, usersInfos

dotenv.load_dotenv()
SET_DATA_API = os.getenv("SET_DATA_API")
CODE_VEREFICATION_API = os.getenv("CODE_VEREFICATION_API")
EMAIL = os.getenv("EMAIL")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def welcomePage(req):
    return render(req, 'welcome.html')

def signin(req):
    if req.method == "POST":
        print("USER TRYING TO SIGN UP")
        FirstName:str = req.POST.get('fname')
        LastName:str = req.POST.get('lname')
        UserName:str = req.POST.get('uname')
        Email:str = req.POST.get('mail')
        Password:str = req.POST.get('pass')
        UserName = checkUsername(UserName)
        if  UserName == '\\':
            return render(req, 'informations.html')
        myData = {
            'FirstName': FirstName, 'LastName': LastName, 'UserName': UserName,
            'Email': Email, 'Password': Password,
        }
        print(f"Set Data With The API: {SET_DATA_API}")
        saveAPI = requests.post(url=SET_DATA_API, json=myData)
        if saveAPI.status_code == 201:
            virefyCode = ''.join(random.choices(string.digits, k=6))
            saveAPI2 = requests.post(url=CODE_VEREFICATION_API, json={'Username': UserName, 'verCode': virefyCode})
            if saveAPI2.status_code != 201:
                return render(req, 'serverError.html')
            sendCodeVerefication(EMAIL, EMAIL_PASS, Email, virefyCode, FirstName + LastName)
            return HttpResponseRedirect(f'activation?username={UserName}')
        else:
            return render(req, 'informations.html')
    return render(req, 'sign.html')

def activate(req):
    try:
        theUser = verificationSystem.objects.get(Username=req.GET.get('username'))
        if req.method == "POST":
            print(f"{theUser.Username}, TRYING TO ACTIVATE THE ACCOUNT")
            print("Activation Code = ", req.POST.get('code'))
            if theUser.verCode == req.POST.get('code'):
                print(f"User Of The UserName: {theUser.Username} Have The Right Code\nACTIVATING...")
                userInfos = usersInfos.objects.get(UserName=theUser.Username)
                userInfos.ACTIVATION = True
                userInfos.save()
                theUser.delete()
                return HttpResponseRedirect('log')
            else:
                #Bad Code
                return render(req, 'activationFailed.html')
    except:
        return render(req, '404.html')
    return render(req, 'activation.html')

def login(req):
    if req.method == "POST":
        print("TRY TO LOG WITH")
        print("MAIL: ", req.POST.get('mail'))
        print("PASS: ", req.POST.get('pass'))
    return render(req, 'log.html')