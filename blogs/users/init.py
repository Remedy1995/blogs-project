import jwt 

from datetime import datetime,timedelta

from django.conf import settings


def generate_jwt(user):
    payload = {
         'id' :user.id,
        'email' : user.email,
         'username' : user.username,
         'role' : user.role,
         'exp' : datetime.utcnow() + timedelta(hours=1)
    }
    
    token = jwt.encode(payload,settings.SECRET_KEY,algorithm='HS256')
    return token.decode('utf-8')


def decode_jwt(token):
    try :
        payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError: 
        return None
    

        