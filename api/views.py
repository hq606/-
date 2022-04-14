from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from api.models import Teacherinfo,Studentinfo,Score,Questions,Course

# Create your views here.
'''
用户管理-学生
'''
def login_v1(request):
    '''学生登陆'''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 从数据库获取数据
        data = Studentinfo.objects.filter(Sphone=username).first()
        if data:
            # 如果能找到用户账号，并且密码正确
            if username == data.Sphone and password == data.Spwd:
                request.session['info'] = data.Sname
                request.session.set_expiry(60*60*24*7)
                return JsonResponse({"status": 200, "msg": "登陆成功"})
            else:
                return JsonResponse({"status": 201, "msg": "用户名或者密码错误"})
        else:
            return JsonResponse({'status': 201, 'msg': '用户名或者密码错误'})
    else:
        return JsonResponse({'status': 201, 'msg': 'NO GET'})


def add_student(request):
    '''添加学生'''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        name = request.POST.get("name")
        sex = request.POST.get("sex")
        sclass = request.POST.get("class")
        # 从数据库获取数据
        data = Studentinfo.objects.filter(Sphone=username).first()
        # 保证用户和密码不为空值
        if username != '' and username != None and password != '' and password != None:
            if data:
                return JsonResponse({'status': 201, 'msg': '该用户已注册'})
            else:
                Studentinfo.objects.create(Sphone=username, Sname=name, Spwd=password, Ssex=sex, SClass=sclass,Sid='2022'+username)
                return JsonResponse({"status": 200, "msg": "注册成功"})
        else:
            return JsonResponse({'status': 201, 'msg': '请检查账号密码'})
    else:
        return JsonResponse({'status': 201, 'msg': 'NO GET'})


def list_v1(request):
    '''学生列表'''
    if request.method == "POST":
        classid = request.POST.get("classid")
        type = request.POST.get("type")
        if type == '1':
            data = list(Studentinfo.objects.filter(SClass=classid).values('Sid', 'Sname', 'Sphone', 'Ssex', 'SClass'))
            return JsonResponse({'status': 200, 'msg': '成功','data':data})
        if type == '2':
            data = list(Studentinfo.objects.all().values('Sid','Sname','Sphone','Ssex','SClass'))
            return JsonResponse({'status': 200, 'msg': '成功','data':data})
        else:
            return JsonResponse({'status': 201, 'msg': 'NO GET'})
    else:
        return JsonResponse({'status': 201, 'msg': 'NO GET'})



'''
用户管理-教师
'''
def add_teacher(request):
    '''添加教师'''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        name = request.POST.get("name")
        sex = request.POST.get("sex")
        depart = request.POST.get("depart")
        #从数据库获取数据
        data = Teacherinfo.objects.filter(Tphone=username).first()
        #保证用户和密码不为空值
        if username != '' and username != None and password != '' and password != None:
            if data:
                return JsonResponse({'status': 201, 'msg': '该用户已注册'})
            else:
                Teacherinfo.objects.create(Tphone=username, Tname=name, Tpwd=password, Tsex=sex, Depart=depart,Tid='2022'+username)
                return JsonResponse({"status": 200, "msg": "注册成功"})
        else:
            return JsonResponse({'status': 201, 'msg': '请检查账号密码'})
    else:
            return JsonResponse({'status': 201, 'msg': 'NO GET'})



def login_v2(request):
    '''教师登陆'''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #从数据库获取数据
        data = Teacherinfo.objects.filter(Tphone=username).first()
        if data:
            # 如果能找到用户，并且密码正确
            if username == data.Tphone and password == data.Tpwd:
                request.session['info'] = data.Tname
                request.session.set_expiry(60 * 60 * 24 * 7)
                return JsonResponse({"status": 200, "msg": "登陆成功"})
            else:
                return JsonResponse({"status": 201, "msg": "用户名或者密码错误"})
        else:
            return JsonResponse({'status': 201, 'msg': '用户名或者密码错误'})
    else:
        return JsonResponse({'status': 201, 'msg': 'NO GET'})


def list_v2(request):
    '''教师列表'''
    data = list(Teacherinfo.objects.all().values('Tid','Tname','Tsex','Depart','Tphone'))
    return JsonResponse({'status': 200, 'msg': '成功','data':data})



def createCourse(request):
    pass



''''''

def orm(request):
    Teacherinfo.objects.all().delete()

    return JsonResponse({'status': 200, 'msg': '成功'})

    # return HttpResponse("成功")

#类视图
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.multipartparser import MultiPartParser
@method_decorator(csrf_exempt,"dispatch")
class QuestionApi(View):
    #试题操作类
    def __init__(self,**kwargs):
        super(QuestionApi, self).__init__(**kwargs)
        self.result = {
            "version":1.0,
            "status": 200,
            "data": []
        }

    def get(self,request,question_id=0):
        '''
        http://127.0.0.1/api/question/   所有
        http://127.0.0.1/api/question/1/
        :param request:
        :return:
        '''
        # Questions.objects.create(Qid=3,Qquestion="我是题目",Qanswer="我是答案",Qoptions='[{"A":"选项1"},{"B":"选项2"},{"C":"选项3"},{"D":"选项4"}]',Qanalysis="我是题目解析",Qscore="2.0",Qdifficulty="我是题目难度",QTreeName="我是题目科目",Cid="我是题目课程号",Qcreate_time="1646028890")
        # Questions.objects.create(Qid=4,Qquestion="我是题目",Qanswer="我是答案",Qoptions='[{"A":"选项1"},{"B":"选项2"},{"C":"选项3"},{"D":"选项4"}]',Qanalysis="我是题目解析",Qscore="2.0",Qdifficulty="我是题目难度",QTreeName="我是题目科目",Cid="我是题目课程号",Qcreate_time="1646028890")
        # Questions.objects.create(Qid=5,Qquestion="我是题目",Qanswer="我是答案",Qoptions='[{"A":"选项1"},{"B":"选项2"},{"C":"选项3"},{"D":"选项4"}]',Qanalysis="我是题目解析",Qscore="2.0",Qdifficulty="我是题目难度",QTreeName="我是题目科目",Cid="我是题目课程号",Qcreate_time="1646028890")
        # Questions.objects.create(Qid=6,Qquestion="我是题目",Qanswer="我是答案",Qoptions='[{"A":"选项1"},{"B":"选项2"},{"C":"选项3"},{"D":"选项4"}]',Qanalysis="我是题目解析",Qscore="2.0",Qdifficulty="我是题目难度",QTreeName="我是题目科目",Cid="我是题目课程号",Qcreate_time="1646028890")
        # Questions.objects.create(Qid=7,Qquestion="我是题目",Qanswer="我是答案",Qoptions='[{"A":"选项1"},{"B":"选项2"},{"C":"选项3"},{"D":"选项4"}]',Qanalysis="我是题目解析",Qscore="2.0",Qdifficulty="我是题目难度",QTreeName="我是题目科目",Cid="我是题目课程号",Qcreate_time="1646028890")
        # Questions.objects.create(Qid=8,Qquestion="我是题目",Qanswer="我是答案",Qoptions='[{"A":"选项1"},{"B":"选项2"},{"C":"选项3"},{"D":"选项4"}]',Qanalysis="我是题目解析",Qscore="2.0",Qdifficulty="我是题目难度",QTreeName="我是题目科目",Cid="我是题目课程号",Qcreate_time="1646028890")
        # Questions.objects.create(Qid=9,Qquestion="我是题目",Qanswer="我是答案",Qoptions='[{"A":"选项1"},{"B":"选项2"},{"C":"选项3"},{"D":"选项4"}]',Qanalysis="我是题目解析",Qscore="2.0",Qdifficulty="我是题目难度",QTreeName="我是题目科目",Cid="我是题目课程号",Qcreate_time="1646028890")
        # Questions.objects.create(Qid=10,Qquestion="我是题目",Qanswer="我是答案",Qoptions='[{"A":"选项1"},{"B":"选项2"},{"C":"选项3"},{"D":"选项4"}]',Qanalysis="我是题目解析",Qscore="2.0",Qdifficulty="我是题目难度",QTreeName="我是题目科目",Cid="我是题目课程号",Qcreate_time="1646028890")
        # Questions.objects.create(Qid=11,Qquestion="我是题目",Qanswer="我是答案",Qoptions='[{"A":"选项1"},{"B":"选项2"},{"C":"选项3"},{"D":"选项4"}]',Qanalysis="我是题目解析",Qscore="2.0",Qdifficulty="我是题目难度",QTreeName="我是题目科目",Cid="我是题目课程号",Qcreate_time="1646028890")
        #有question_id则单条查询，反之查询所有
        if question_id:
            q_list = list(Questions.objects.filter(Qid=question_id).values())
            if q_list:
                self.result["data"] = q_list
            else:
                self.result["status"] = 201
                self.result["data"] = "没有id为{}的数据".format(question_id)
            # return JsonResponse(self.result)

        else:
            '''分页'''
            page = request.GET.get("page")
            if page:
                start = (int(page)-1)*10
                end = (int(page))*10
                q_list = list(Questions.objects.all().values())[start:end]
                self.result["data"] = q_list
            else:
                q_list = list(Questions.objects.all().values())
                self.result["data"] = q_list
        return JsonResponse(self.result)

    def post(self,request):
        request_data = request.POST
        q_id = request_data.get("Qid")
        q_data = Questions.objects.filter(Qid=q_id).first()
        if q_data:
            self.result["status"] = 201
            self.result["data"] = "已存在id为{}的数据".format(q_id)
        else:
            q = Questions()
            q.Qid = request_data.get("Qid")
            q.Qquestion = request_data.get("Qquestion")
            q.Qanswer = request_data.get("Qanswer")
            q.Qoptions = request_data.get("Qoptions")
            q.Qanalysis = request_data.get("Qanalysis")
            q.Qscore = request_data.get("Qscore")
            q.Qdifficulty = request_data.get("Qdifficulty")
            q.QTreeName = request_data.get("QTreeName")
            q.Cid = request_data.get("Cid")
            q.Qcreate_time = request_data.get("Qcreate_time")
            # q_data = q.objects.filter(Qid=q_id).first()
            try:
                q.save()
            except Exception as e:
                self.result["status"] = 500
                self.result["data"] = str(e)
            else:
                self.result["data"] = "成功"

        return JsonResponse(self.result)

    def put(self,request,question_id=0):
        q = Questions.objects.filter(Qid=question_id).first()
        if q:
            put = MultiPartParser(request.META,request,request.upload_handlers).parse()
            put_data = put[0]
            q.Qid = put_data.get("Qid")
            q.Qquestion = put_data.get("Qquestion")
            q.Qanswer = put_data.get("Qanswer")
            q.Qoptions = put_data.get("Qoptions")
            q.Qanalysis = put_data.get("Qanalysis")
            q.Qscore = put_data.get("Qscore")
            q.Qdifficulty = put_data.get("Qdifficulty")
            q.QTreeName = put_data.get("QTreeName")
            q.Cid = put_data.get("Cid")
            q.Qcreate_time = put_data.get("Qcreate_time")
            # q_data = q.objects.filter(Qid=q_id).first()
            try:
                q.save()
            except Exception as e:
                self.result["status"] = 500
                self.result["data"] = str(e)
            else:
                self.result["data"] = "成功"
        else:
            self.result["status"] = 201
            self.result["data"] = "没有id为{}的数据".format(question_id)

        return JsonResponse(self.result)

    def delete(self,request,question_id=0):
        q = Questions.objects.filter(Qid=question_id).first()
        if q:
            q.delete()
            self.result["data"] = "成功"
        else:
            self.result["status"] = 201
            self.result["data"] = "没有id为{}的数据".format(question_id)
        return JsonResponse(self.result)


#退出
def logout(request):
    request.session.clear()
    return redirect('/')
#登陆
def login(request):
    '''用户登陆'''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 从数据库获取数据
        Student_data = Studentinfo.objects.filter(Sphone=username).first()
        Teacher_data = Teacherinfo.objects.filter(Tphone=username).first()
        if Student_data:
            # 如果能找到用户账号，并且密码正确
            if username == Student_data.Sphone and password == Student_data.Spwd:
                request.session['info'] = {"name":Student_data.Sname,"type":"Student"}
                request.session.set_expiry(60*60*24*7)
                return JsonResponse({"status": 200, "msg": "登陆成功"})
            else:
                return JsonResponse({"status": 201, "msg": "用户名或者密码错误"})
        if Teacher_data:
            # 如果能找到用户账号，并且密码正确
            if username == Teacher_data.Sphone and password == Teacher_data.Spwd:
                request.session['info'] = {"name":Teacher_data.Sname,"type":"Teacher"}
                request.session.set_expiry(60*60*24*7)
                return JsonResponse({"status": 200, "msg": "登陆成功"})
            else:
                return JsonResponse({"status": 201, "msg": "用户名或者密码错误"})
        else:
            return JsonResponse({'status': 201, 'msg': '用户名或者密码错误'})
    else:
        return JsonResponse({'status': 201, 'msg': 'NO GET'})
