from django.shortcuts import render
from .models import savings_model
from rest_framework import generics
from rest_framework.response import Response


class savings_api(generics.GenericAPIView):
    def post(self,request):
        try:
            data=request.data
            a=data.get("name")
            b=data.get("age")
            c=data.get("amount")
            print(a)
            print("hi")
            dict_a={"name":a,"age":b,"amount":c}
            s=savings_model.objects.create(**dict_a)
            return Response({"status":"success","message":"data created in db"})
        except Exception as e:
            return Response({"status":"fail","message":"logical error"})
        
    def get(self,request):
        try:
            data=request.GET
            id1=data.get("id")
            obj1=savings_model.objects.get(id=id1)
            dict_b={"name":obj1.name,"age":obj1.age,"amount":obj1.amount}
            print("hi")
            return Response({'status':"success","msg":"data retreived from db","data":dict_b})
        except savings_model.DoesNotExist as e1:
            return Response({"status":"fail","msg":"id not found in db"})
        except Exception as e:
            print("hello")
            return Response({"status":"fail","msg":"logical error"})
        
    def patch(self,request):
        try:
            data=request.GET
            data1=request.data
            id1=data.get("id")
            print(id1)
            a=data1.get("name")
            print(a)
            b=data1.get("age")
            c=data1.get("amount")
            obj2=savings_model.objects.get(id=id1)
            print(obj2)
            obj2.name=a
            obj2.age=b 
            obj2.amount=c 
            obj2.save()
            return Response({"status":"success","msg":"data updated"})
        except savings_model.DoesNotExist as e2:
            return Response({"status":"fail","msg":"id not found in db"})
        except Exception as e:
            return Response({"status":"fail","msg":"logical error"})

    def delete(self,request):
        try:
            data=request.GET
            id1=data.get("id")
            obj2=savings_model.objects.get(id=id1)
            print(obj2)
            obj2.is_active=False
            obj2.save()
            return Response({"status":"success","msg":"data deleted temporarily"})
        except savings_model.DoesNotExist as e2:
            return Response({"status":"fail","msg":"id not found in db"})
        except Exception as e:
            return Response({"status":"fail","msg":"logical error "})