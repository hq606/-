'''
@Time    : 2022/4/28 16:15
@Author  : YourName
@FileName: exam.py
@Software: PyCharm
 
'''
from django.shortcuts import HttpResponse,render
from django.http import JsonResponse
from api.models import *
from datetime import datetime
def AddExam(request):
    '''创建试卷'''
    if request.method == "POST":
        try:
            title = request.POST.get("title")
            score = request.POST.get("score")
            student = request.POST.get("student")
            Cid = request.POST.get("cid")
            Start_time = request.POST.get("start_time")
            End_time = request.POST.get("end_time")
            State = request.POST.get("state")
            Students_Exam = request.POST.get("studentlist")
            Questions_Exam = request.POST.get("questionlist")
            #获取数据保持到数据库

            Exam.objects.create(Eid=int(round(datetime.now().timestamp())), Title=title, Total_score=score, Cid=Cid, Start_time=Start_time,End_time=End_time,State=State,Students_Exam=Students_Exam,Questions_Exam=Questions_Exam)
            return JsonResponse({"status": 200, "msg": "保存成功"})
        except Exception as e:
            return JsonResponse({"status": 500, "msg": e})
    else:
            return JsonResponse({"status": 500, "msg": 'err'})

def GetExam(request):
    data = list(Exam.objects.all().values('Eid', 'Title', 'Total_score', 'Cid', 'Start_time', 'End_time', 'Create_time','State','Students_Exam','Questions_Exam'))
    return JsonResponse({'status': 200, 'msg': '成功', 'data': data})
