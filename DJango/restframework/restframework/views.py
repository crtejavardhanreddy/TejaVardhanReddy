from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from restapp.serializers import StudentSerializer
from restapp.models import Student

class TestView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self,request,*args,**kwargs):
        qs = Student.objects.all()
        # student1 = qs.first()
        serializer = StudentSerializer(qs,many=True)
        return Response(serializer.data)
    
    def post(self,request, *args, **kwrags):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    