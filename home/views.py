from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from home.models import Person
from home.serializer import LoginSerializer, PersonSerializer, RegisterSerializer
from django.contrib.auth import authenticate
from django.core.paginator import Paginator

@api_view(['GET','POST'])
def index(request):
    if request.method == "POST":
        data = request.data
        data = f"Name of the Person is {data.get('name')} and age is {data.get('age')}"
        return Response({"message": "This is post method!", 'data': data})

    return Response({"message": "Hello, World!"} , status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        user = authenticate(**serializer.validated_data)
        if not user:
            return Response({"message": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        # return Response(serializer.validated_data)
        return Response({"message": "Log in successful!", "token": token.key}, status=status.HTTP_200_OK)
    else:
        return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def register(request):
    data = request.data
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User Created"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PersonView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        try:
            objs = Person.objects.all()
            page = request.GET.get('page', 1)
            page_size = 1
            paginator = Paginator(objs, page_size)
            serializer = PersonSerializer(paginator.page(page), many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'message':"Empty Page!"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    
    def put(self, request):
        try:
            data = request.data
            obj = Person.objects.get(id=data.get('id'))
            serializer = PersonSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors)
        except:
            return Response({'message':"Person Not Found!"})
    
    def patch(self, request):
        try:
            data = request.data
            obj = Person.objects.get(id=data.get('id'))
            serializer = PersonSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

            return Response(serializer.errors)
        except:
            return Response({'message':"Person Not Found!"})
    
    def delete(self, request):
        try:
            data = request.data
            obj = Person.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'message':"Person Deleted!"})
        except:
            return Response({'message':"Person Not Found!"})


# @api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])
# def person(request):
#     if request.method == "GET":
#         try:
#             objs = Person.objects.all()
#             serializer = PersonSerializer(objs, many=True)
#             return Response(serializer.data)
#         except:
#             return Response({'message':"Person Not Found!"})

#     elif request.method == "POST":
#         try:
#             data = request.data
#             serializer = PersonSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)

#             return Response(serializer.errors)
#         except:
#             return Response({'message':"Person Not Found!"})
    
#     elif request.method == "PUT":
#         try:
#             data = request.data
#             obj = Person.objects.get(id=data.get('id'))
#             serializer = PersonSerializer(obj, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)

#             return Response(serializer.errors)
#         except:
#             return Response({'message':"Person Not Found!"})
    
#     elif request.method == "PATCH":
#         try:
#             data = request.data
#             obj = Person.objects.get(id=data.get('id'))
#             serializer = PersonSerializer(obj, data=data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)

#             return Response(serializer.errors)
#         except:
#             return Response({'message':"Person Not Found!"})
    
#     elif request.method == "DELETE":
#         try:
#             data = request.data
#             obj = Person.objects.get(id=data.get('id'))
#             obj.delete()
#             return Response("Person Deleted.")
#         except:
#             return Response({'message':"Person Not Found!"})

#     return Response({"message": "Method Not Supported"})

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def list(self, request):
        search = request.GET.get('search')
        if search:
            self.queryset = self.queryset.filter(name__contains=search)
        serializer = PersonSerializer(self.queryset, many=True)

        if serializer.data != []:
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        
        return Response({"message": "Person Not Found!"}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['POST'])
    def send_email(self, request):
        email = request.data.get('email')
        subject = request.data.get('subject')
        message = request.data.get('message')
        return Response({"message": "Email sent successfully!"}, status=status.HTTP_200_OK)