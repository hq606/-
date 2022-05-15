from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from api.models import *
from datetime import datetime
import random


#类视图
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.multipartparser import MultiPartParser
@method_decorator(csrf_exempt,"dispatch")
class ClassApi(View):
    #课程操作类
    def __init__(self,**kwargs):
        super(ClassApi, self).__init__(**kwargs)
        self.result = {
            "version":1.0,
            "status": 200,
            "data": []
        }

    def get(self,request,class_id=0):
        if class_id:
            c_list = list(Class_t.objects.filter(Cclassid=class_id).values())
            if c_list:
                self.result["data"] = c_list
            else:
                self.result["status"] = 201
                self.result["data"] = "没有id为{}的数据".format(class_id)
            # return JsonResponse(self.result)

        else:
            '''分页'''
            page = request.GET.get("page")
            if page:
                start = (int(page)-1)*10
                end = (int(page))*10
                c_list = list(Class_t.objects.all().values())[start:end]
                self.result["data"] = c_list
            else:
                c_list = list(Class_t.objects.all().values())
                self.result["data"] = c_list


        return JsonResponse(self.result)

    def post(self,request):
        request_data = request.POST
        c_id = request_data.get("Cclassid")
        c_data = Class_t.objects.filter(Cclassid=c_id).first()
        if c_data:
            self.result["status"] = 201
            self.result["data"] = "已存在id为{}的数据".format(c_id)
        else:
            c = Class_t()
            c.Cclassid = int(str(round(datetime.now().timestamp())))
            c.Ccname = request_data.get("Ccname")
            c.Tid = request_data.get("Tid")
            c.Cid = request_data.get("Cid")

            try:
                c.save()
            except Exception as e:
                self.result["status"] = 500
                self.result["data"] = str(e)
            else:
                self.result["data"] = "成功"

        return JsonResponse(self.result)


    def put(self,request,class_id=0):
        c = Class_t.objects.filter(Cclassid=class_id).first()
        if c:
            put = MultiPartParser(request.META, request, request.upload_handlers).parse()
            request_data = put[0]
            c.Cclassid = request_data.get("Cclassid")
            c.Ccname = request_data.get("Ccname")
            c.Tid = request_data.get("Tid")
            try:
                c.save()
            except Exception as e:
                self.result["status"] = 500
                self.result["data"] = str(e)
            else:
                self.result["data"] = "成功"
        else:
            self.result["status"] = 201
            self.result["data"] = "没有id为{}的数据".format(class_id)

        return JsonResponse(self.result)

    def delete(self,request,class_id=0):
        c = Class_t.objects.filter(Cclassid=class_id).first()
        if c:
            c.delete()
            self.result["data"] = "成功"
        else:
            self.result["status"] = 201
            self.result["data"] = "没有id为{}的数据".format(class_id)
        return JsonResponse(self.result)
