"""from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


import csv
import codecs
from .models import RepM


class Medicine_api(generics.GenericAPIView):
    def post(self,request):
        try:
            file=request.FILES['file']
            print("hi")
            reader=csv.DictReader(codecs.iterdecode(file,"utf-8"),delimiter=",")
            drugs_list=[]
            print(str(reader))
            for i in reader:
                print("hi")
                drug={"sno":i["sno"],"drug_name":i["drug_name"],"drug_strength":i["drug_strength"],"drug_type":i["drug_type"],"bill_date":i["bill_date"]}
                print(drug)
                drugs_list.append(RepM(**drug))
            print("hello")
            print(drugs_list)
            RepM.objects.bulk_create(drugs_list)
            return Response({"status":"success","message":"import done"})
        except Exception as e:
            return Response({"status":"fail","data":str(e.args)})
                """

from rest_framework import generics
from rest_framework.response import Response
import csv
import codecs
from .models import RepM

class Medicine_api(generics.GenericAPIView):
    def post(self, request):
        try:
            if 'file' not in request.FILES:
                return Response({"status": "fail", "message": "No file uploaded"}, status=400)

            file = request.FILES['file']
            reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
            drugs_list = []

            for row in reader:
                drug = {
                    "sno": row.get("sno"),
                    "drug_name": row.get("drug_name"),
                    "drug_strength": row.get("drug_strength"),
                    "drug_type": row.get("drug_type"),
                    "bill_date": row.get("bill_date")
                }
                drugs_list.append(RepM(**drug))

            RepM.objects.bulk_create(drugs_list)
            return Response({"status": "success", "message": "Import successful"}, status=201)
        
        except KeyError as e:
            return Response({"status": "fail", "message": f"Missing key in CSV: {str(e)}"}, status=400)
        
        except Exception as e:
            return Response({"status": "fail", "message": str(e)}, status=500)

