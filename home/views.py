from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from home.models import Person
from home.serializer import LoginSerializer, PersonSerializer

@api_view(['GET','POST'])
def index(request):
    if request.method == "POST":
        data = request.data
        data = f"Name of the Person is {data.get('name')} and age is {data.get('age')}"
        return Response({"message": "This is post method!", 'data': data})

    return Response({"message": "Hello, World!"})

# class PersonView(APIView):
#     def get(self, request):
#         objs = Person.objects.all()
#         serializer = PersonSerializer(objs, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         data = request.data
#         serializer = PersonSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors)
    
#     def put(self, request):
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
    
#     def patch(self, request):
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
    
#     def delete(self, request):
#         try:
#             data = request.data
#             obj = Person.objects.get(id=data.get('id'))
#             obj.delete()
#             return Response({'message':"Person Deleted!"})
#         except:
#             return Response({'message':"Person Not Found!"})

# @api_view(['POST'])
# def login(request):
#     data = request.data
#     serializer = LoginSerializer(data=data)

#     if serializer.is_valid():
#         return Response(serializer.validated_data)

#     return Response(serializer.errors)

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