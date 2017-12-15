import json
from rest_framework.decorators import api_view
from rest_framework.response import Response as Res
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# region Server Constants
RES_OK = 0
RES_FAIL = 1
RES_BAD = 2
user = None


# endregion


@api_view(['POST'])
def login(request):
    req_body = request.body.decode('utf-8')
    body = json.loads(req_body)
    global user

    if 'username' in body and 'password' in body:
        user = authenticate(username=body['username'], password=body['password'])
        if user is None:
            return Res(data={'result': RES_FAIL})
        else:
            return Res(data={'result': RES_OK})
    else:
        return Res(data={'result': RES_BAD})


@api_view(['POST'])
def register(request):
    req_body = request.body.decode('utf-8')
    body = json.loads(req_body)
    if 'username' in body and 'password' in body:
        if User.objects.filter(username=body['username']).exists():
            return Res(data={'result': RES_FAIL})
    else:
        User.objects.create_user(username=body['username'], password=body['password'])
        return Res(data={'result': RES_OK})
    return Res(data={'result': RES_BAD})
