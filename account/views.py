from django.shortcuts import render
from django.apps import apps
from django.db.models import fields
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from rest_framework.generics import GenericAPIView
from .models import UserAccount
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from datetime import datetime
import random



from employees.models import *




# def cookieAuth(request):
#     token = request.COOKIES.get('session')
#     print('token', request.COOKIES)
#     if token is None:
#         raise AuthenticationFailed('unauthenticated')
#     try:
#         payload = jwt.decode(token, 'secret', 'HS256')
#         # print('payload', payload)
#     except jwt.ExpiredSignatureError:
#         raise AuthenticationFailed('unauthenticated')
#     id = payload['id']
#     user = Users.objects.filter(id=id).first()
#     return {'user': user, 'id': id}


def getProduct(emp):
    product = employee_official.objects.filter(employee_id = emp).first()
    return product.product

def getUserRole(emp):
    pass
    # # print('working till here')
    # print(emp.id)
    # # user = UserAccount.objects.filter(employee_id = emp).first()
    # # user_id = user.id
    # product = employee_official.objects.select_related.filter(emp = emp).first()
    # # print(product)
    # return "sdfsdf"

def getTeamLeader(emp):
    team_leader = employee_official.objects.filter(employee_id = emp).first()
    return team_leader.team_leader

def getLeadId():
    date = datetime.now()
    date = date.strftime('%Y%m%d%H%M%S%f')
    random_int = random.randint(100,499) + random.randint(100,499)
    lead_id = f'L{str(date) + str(random_int)}'
    return lead_id

def getClientId():
    date = datetime.now()
    date = date.strftime('%Y%m%d%H%M%S%f')
    random_int = random.randint(100,499) + random.randint(100,499)
    lead_id = f'C{str(date) + str(random_int)}'
    return lead_id

def getAssociates(emp):
    pass
    # data = employee_official.objects.filter(team_leader = emp)
    # data = list(data.values())
    # emp_list = []
    # for d in data:
    #     associate_data = employee_basic.objects.filter(employee_id = d['employee_id']).first()
    #     emp_list.append({'employee_id' : associate_data.employee_id, 'name' : associate_data.name})
    # return emp_list


def getModelFields(model):
    allfields = []
    for f in model._meta.get_fields():
        if isinstance(f, fields.AutoField):
            continue
        allfields.append({'field': f.name, 'type': f.get_internal_type()})
    return allfields


    # print(emp_list)
    # return 

# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
#     return {
#         "access" : str(refresh),
#         "refresh": str(refresh.access_token)
#     }










class IgnoreBearerTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        # Check if the "Authorization" header is present in the request
        if 'Authorization' in request.headers:
            # Get the value of the "Authorization" header
            auth_header = request.headers['Authorization']

            # If the header starts with "Bearer", ignore it and return None for authentication
            if auth_header.startswith('Bearer'):
                return None

        # Return the result of the super method, even if it's None
        return super().authenticate(request)
    
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
    
class LoginView(GenericAPIView):
   serializer_class=loginSerializer
   authentication_classes = [IgnoreBearerTokenAuthentication]
   def post(self,request,format=None):
      serializer=loginSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
         email=serializer.data.get('email')
         password=serializer.data.get('password')
         try:
            user_obj=UserAccount.objects.get(email=email)
         except:
            return Response({'status': status.HTTP_404_NOT_FOUND,'message':'Please Registerd user first','data':{"xyz":"123"}}, status=status.HTTP_404_NOT_FOUND)          
         user=authenticate(email=email,password=password)
         if user is not None:
            token=get_tokens_for_user(user)
            data={"Token":token}

            res = Response()
            res.status_code = status.HTTP_200_OK
            res.data = {
                'status': 200,
                'message': "registrations successful",
                'data': {
                    'user_details': user_VF(user.id),
                    "token": token,
                },
            } 
            res.token = {
                "token": token,
            }   
            return res
         else:
             return Response({'status': status.HTTP_404_NOT_FOUND,'message':'Email or password is not Valid','data':{}}, status=status.HTTP_404_NOT_FOUND)
         
         
# class TestView(GenericAPIView):
#    permission_classes=[IsAuthenticated]
#    def get(self,request,format=None):
#        print(request.user.username,"work")  
#        return Response({'status': status.HTTP_404_NOT_FOUND,'message':'','data':[request.user.username,request.user.id,request.user.employee_id]}, status=status.HTTP_404_NOT_FOUND)
   







# new functions from core


class registration_VF(GenericAPIView):
    serializer_class = registrationSerializer
    def post(self, request, format=None, *args, **kwargs):
        # print('asdfasf',request.user, request.headers)
        # print('request as view', request.data.get('email'))
        employee_id = request.data.get('employee_id')
        name = request.data.get('name')

        res = Response()
        if employee_id == None:
            res.status_code = status.HTTP_204_NO_CONTENT
            res.data = {'error': 'employee_id field id is required'}
            return res
        
        if name == None:
            res.status_code = status.HTTP_204_NO_CONTENT
            res.data = {'error': 'name field is required'}
            return res

        serializer = registrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # emp_basic = employee_basic.objects.create(employee_id = employee_id, name = name)
        # emp_basic = employee_official.objects.create(employee_id = employee_id)

        if user is not None:
            res.data = {'message': 'user registered'}
            res.status_code = status.HTTP_201_CREATED 
            return res
        



class userSpecificLinkHeader(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = userSpecificLinkSerializer
    def get(self, request, format=None, *args, **kwargs):
        print(request.user)
        user = request.user
        from .models import xsup_user_links, Users, employee_official
        # user = cookieAuth(request)
        user_id = user.id
        employee_id = user.employee_id

        usr_role = employee_official.objects.filter(employee_id = employee_id).first()
        print(usr_role)
        usr_role = usr_role.user_role
        links = xsup_user_links.objects.filter(access_department = usr_role, link_status = True)
        # print(links)
        usr_link = []
        for link in links:
            usr_link.append({"title": link.title, 'link_type': link.link_type, 'link': link.user_link })

        serializer = userSpecificLinkSerializer(data=usr_link, many=True)
        serializer.is_valid(raise_exception=True)
        # print()
        res = Response()
        res.status_code = status.HTTP_200_OK
        res.data = {"user_link" : serializer.data}
        return res
    
        # return Response({"data": request.headers})



def user_VF(id):
    
    print('id', id)
    # user = cookieAuth(request)
    # user = employee_official.objects.select_related().filter(emp=id).values()
    user = employee_official.objects.get(emp=id)
    data = {
        'user_role' : user.user_role,
        'product' : user.product,
        'name' : user.emp.name,
        'employee_id' : user.emp.employee_id,
        'email' : user.emp.email,
    }

    # user_role = user.user_role
    # print('user', user.employee_id)
    # employee_id = user.employee_id
    # user_role = getUserRole(employee_id)
    serializer = userSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    # if serializer.is_valid(raise_exception=True):
    return  {'user': serializer.data}
