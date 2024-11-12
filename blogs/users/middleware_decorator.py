from django.http import JsonResponse
from blogs.users.init import decode_jwt
from functools import wraps


def jwt_required(view_func):
    @wraps(view_func)
    def wrapper(request,*args,**kwargs):
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
             return JsonResponse({
                     'status' : False,
                    'error' :'No Headers Found'
                },status=401)
        if token:
            try:
                token = token.split(' ')[1]
                payload = decode_jwt(token)
                
                if payload:
                    request.user_data = payload
                    return view_func(request,*args,**kwargs)
                
                else :
                    return JsonResponse({
                        'error' :' Invalid or expired token'
                    },status=401)
            except IndexError:
                     return JsonResponse({
                    'error' :'Token not provided'
                },status=401)
        return JsonResponse({
                    'error' :'Unauthorized, token expired'
                },status=401)
        
        
    return wrapper