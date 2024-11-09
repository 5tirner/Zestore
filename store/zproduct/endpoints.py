from rest_framework import status, response
from rest_framework.decorators import api_view
from .serial import userInfosSerial, verificationSysSerial
from .checkInput import checkPass, checkEmail, checkUsername

@api_view(['POST'])
def setData(req):
    print("DATA TO POST:")
    print(req.data)
    serial = userInfosSerial(data=req.data)
    if serial.is_valid():
        Email:str = req.data.get('Email')
        Pass:str = req.data.get('Password')
        if checkPass(Pass) == False or len(Pass) < 8 or checkEmail(Email) == False:
            return response.Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        # serial.save()
        print("USERS INFOS STORED, NOT VERIFIED YET.")
        return response.Response(status=status.HTTP_201_CREATED)
    return response.Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

@api_view(['POST'])
def createVerification(req):
    print('Data To Post:')
    print(req.data)
    serial = verificationSysSerial(data=req.data)
    if serial.is_valid():
        # serial.save()
        print("CREATE VERIFICATION CODE")
        return response.Response(status=status.HTTP_201_CREATED)
    return response.Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)