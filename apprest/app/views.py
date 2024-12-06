import pytz 
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from datetime import datetime
from django.utils import timezone

from .serializers import SessionSerializer
from .models import user, session
# Create your views here.
current_dateTime = datetime.now()
utc_now = timezone.now()
utc_now = utc_now.replace(tzinfo=pytz.utc)

TOKEN_TTL = datetime.timedelta(minute=320)
EXPIRED = utc_now - TOKEN_TTL
IDAPP = 1

@api_view(['POST'])
def authentication(request):
    print("login: ", request.data)
    user_dto = user.objects.get(email = request.data.email, 
                                active= True, password = request.data.password)
    if not user_dto:
        return Response({'error':'NO FOUND DATA', 'status': HTTP_400_BAD_REQUEST})  
    
    session_dto = session.objects.get(iduser=user_dto.id, active=True)
    if session_dto:
        print("current_dateTime:", current_dateTime)
        print("session_dto.session_out:", session_dto.session_out)
        if session_dto.session_out < current_dateTime:
            return Response({'session-on': session_dto, 'status': HTTP_200_OK})
        else:
            #actualiza la sesion expirada
            session_dto.active = False
            serializer_session_out = SessionSerializer(data=session_dto)
            if serializer_session_out.is_valid():
                serializer_session_out.save()
            else:
                Response({'error':'UPDATE OUT - NOT VALID DATA SESSION', 'status': HTTP_400_BAD_REQUEST})
            
            # crea una nueva sesion
            
            token = Token.objects.create(user=user_dto)
            token.created = utc_now
            token.save()
            print("token:", token)
            session_dto = {'session_on': current_dateTime, 'session_out': EXPIRED, 
                        'token_bearer': token.key, 'active': 'True', 
                        'iduser': user_dto.id, 'idapp': IDAPP}
            
            serializer_session_dto_on = SessionSerializer(data=session_dto)
            if serializer_session_dto_on.is_valid():
                serializer_session_dto_on.save()
                return Response({'session-on': serializer_session_dto_on, 'status':HTTP_201_CREATED})
            else:
                Response({'error':'CREATE AT - NOT VALID DATA SESSION', 'status': HTTP_400_BAD_REQUEST})
        
    # crea nueva sesion
    token = Token.objects.create(user=user_dto)
    token.created = utc_now
    token.save()
    print("token: ", token)
    session_dto = {'session_on': current_dateTime, 'session_out': EXPIRED, 
                'token_bearer': token.key, 'active': True, 
                'iduser': user_dto.id, 'idapp': IDAPP}
    
    serializer_session_dto_on = SessionSerializer(data=session_dto)
    if serializer_session_dto_on.is_valid():
        serializer_session_dto_on.save()
        return Response({'session-on': serializer_session_dto_on, 'status':HTTP_201_CREATED})
    else:
        Response({'error':'CREATE AT - NOT VALID DATA SESSION', 'status': HTTP_400_BAD_REQUEST})



