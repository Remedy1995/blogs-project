from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from blogs.models import User,Blogs
from blogs.users.init import generate_jwt
from django.contrib.auth import authenticate
from blogs.users.middleware_decorator import jwt_required
# from PyPDF2 import PdfReader
# from openai import OpenAI

import json


# from .models import User
# Create your views here.

def index(request):
    return JsonResponse('Hello this is my pdf app')


@csrf_exempt
def signup(request):
    if request.method =='POST':
        if not request.body:
            return JsonResponse({'status':False,'message':'No Data provided'},status= 422)
        try:
            data = json.loads(request.body)
            print(f'my  ata',data)
            required_fields = ['email','username','password','role']
            #extract the keys from the json payload
            json_keys = list(data.keys())
            json_data = data.items()
            missing_fields = [field for field in required_fields if field not in json_keys ]
            print(json_data)
            if missing_fields:
                return JsonResponse({'status':422,'message' :f'The {missing_fields} key field does not exist'},status=422)
            for index,value in json_data:
                if value =='':
                    return JsonResponse({'status':422,'message' :f'The {index} value is required'},status=422)
            username = data['username']
            password = data['password']
            email = data['email']
            role = data['role']
            userRole = ['admin','user']
            try :
                userExists = User.objects.filter(email=email,username =username)
                if(len(userExists)> 0):
                        return JsonResponse({
                                'message':'Sorry User already Exists','status':False  
                            },status =400)
                user = User.objects.create(username=username,email=email,role=role)
                print('User created',user)
                token = generate_jwt(user)
                print('my token',token)
                user.set_password(password)
                user.save()
                if user:
                    return JsonResponse({
                        'message':'User has been created successfully',
                        
                    },status =201)
            except Exception as error:
                    print(f'error {error.args}')
                    error_message = error.args[1] if isinstance(error.args,tuple) and len(error.args) > 1 else str(error)
                    return JsonResponse({'status': 500,'error': 'Creation Failed','message':error_message},status =500)
        except Exception as error:
                return JsonResponse({'status': 500,'error': 'Creation Failed','message':"Sorry an error occured"},status =500)

@jwt_required
def fetch_users(request):
    print(f'This user',request)
    all_users = []
    try :
        users = User.objects.all()
        for user in users:
            all_users.append({
                'username' : user.username,
                'password' : user.password,
                 'role' : user.role              
            })
            
        return JsonResponse({'message':'Success','data':all_users},status=200)
    except Exception as error:
       return JsonResponse({'message':'Error','error': str(error)},status=500)
   
   
   
   
@csrf_exempt 
def login(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    auth_user = authenticate(username=username,password=password)
    if auth_user is None:
        return JsonResponse({'status' : False,'error':'Invalid Credentials provided'},status=422)
    token = generate_jwt(auth_user)
    
    return JsonResponse({'status':True,'message':'User has successfully logged in','token': token})
 
@csrf_exempt 
@jwt_required
def makeBLogs(request):
    if request.method =='POST':
        if not request.body :
            return JsonResponse({'status': False, 'message' : 'Sorry no payload provided'})
        data = json.loads(request.body)
        try:
            posts = Blogs.objects.create(
            title = data['title'],
            slug =  data['slug'],
            author = data["author"],
            content = data["content"],
            categories = data["categories"],
            # publication_date = data["publication_date"]
            )
            if posts:
                return JsonResponse({'status': True, 'message' : 'Blogs has been created successfully'},status=201)
        except Exception as error:
            print(error.args)
            return JsonResponse({'status': True, 'message' : error.args}) 
    else :
        return JsonResponse({"status": False, "message":"Sorry the method is not supported"}) 

@csrf_exempt   
@jwt_required
def viewBlogs(request):
    if request.method =='GET':
        try :
            posts = Blogs.objects.all()
            values = list(posts.values())
            print(posts)
            return JsonResponse({'status': True, 'data' : values},status =200)
        except Blogs.DoesNotExist:
            return JsonResponse({'status':False, 'message' : 'No Blogs Exists'}) 
        except Exception as error:
            return JsonResponse({'status':False, 'message' : error.args}) 
    else :
        return JsonResponse({"status": False, "message":"Sorry the method is not supported"}) 
@csrf_exempt
@jwt_required
def viewBlogById(request,id):
    if request.method =='GET':
        try :
            posts = Blogs.objects.get(id = id)
            print('fggdf',posts)
            single_data = {
            'title' : posts.title,
            'slug' : posts.slug,
            'author': posts.author,
            'content': posts.content,
            'categories': posts.categories,
            'publication_date': posts.publication_date.strftime('%Y-%m-%d') if posts.publication_date else None
            }
            print('ppp',single_data)
            return JsonResponse({'status': True, 'data':single_data},status=200)
        except Blogs.DoesNotExist:
            return JsonResponse({'status': False, 'data':'Blog does not Exist'},status=404)
        except Exception as error:
            return JsonResponse({'status': False, 'message' : error.args}) 
    else :
        return JsonResponse({"status": False, "message":"Sorry the method is not supported"}) 
@csrf_exempt
def updateBlogById(request,id):
    if request.method =='PUT':
        print('i want to update')
        data = json.loads(request.body)
        try :
            posts = Blogs.objects.get(id = id)
            posts.title = data['title']
            posts.slug=data['slug']
            posts.author= data['author']
            posts.content= data['content']
            posts.categories= data['categories']
            posts.save()
            return JsonResponse({'status': True, 'message' : 'Blogs has been updated successfully'}) 
        except Blogs.DoesNotExist:
            return JsonResponse({'status': False, 'message' : 'Blogs does not exist'},status=404) 
        except Exception as error:
            return JsonResponse({'status': True, 'message' : error.args}) 
    else :
        return JsonResponse({"status": False, "message":"Sorry the method is not supported"})

@csrf_exempt      
def deleteBlogById(request,id):
    if request.method =='DELETE':
        print('hello delete')
        try:
            posts = Blogs.objects.get(id=id)
            posts.delete()
            return JsonResponse({"message":"The blog has been deleted"})
        except Blogs.DoesNotExist:
            return JsonResponse({'status': False, 'message' : 'Blogs does not exist'},status=401)  
    else :
        return JsonResponse({"status": False, "message":"Sorry the method is not supported"})