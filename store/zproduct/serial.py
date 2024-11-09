from rest_framework.serializers import ModelSerializer
from .models import usersInfos, verificationSystem

class userInfosSerial(ModelSerializer):
    class Meta:
        model = usersInfos
        fields = ['FirstName', 'LastName', 'UserName', 'Email', 'Password']

class verificationSysSerial(ModelSerializer):
    class Meta:
        model = verificationSystem
        fields = ['Username', 'verCode']