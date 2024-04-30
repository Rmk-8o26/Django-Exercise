from django.shortcuts import render
from .models import login_model
from rest_framework import generics
from rest_framework.response import Response


class login_api(generics.GenericAPIView):
    def post(self,request):
        try:
            data=request.data
            a=data.get("username")
            b=data.get("password")
            obj1=login_model.objects.get(username=a)
            if obj1.password==b:
                return Response({'status':'success','msg':'login successfull'})
            return Response({'status':'fail','msg':'incorrect password'})
        except login_model.DoesNotExist as e1:
            return Response({"status":"fail","msg":"username not in db"})
        except Exception as e:
            return Response({"status":"fail","msg":"logical error"})