from django.db import models

# Create your models here.
'''学生表'''
class Studentinfo(models.Model):
    Sid = models.IntegerField() #学号
    Sname = models.CharField(max_length=32)
    Sphone = models.CharField(max_length=12)#账号
    Spwd = models.CharField(max_length=64)
    Ssex = models.CharField(max_length=12)
    SClass = models.CharField(max_length=32)#所在班级id

'''教师表'''
class Teacherinfo(models.Model):
    Tid = models.IntegerField() #教工号
    Tphone = models.CharField(max_length=12)  # 账号
    Tname = models.CharField(max_length=32)
    Tpwd = models.CharField(max_length=64)
    Tsex = models.CharField(max_length=12)
    Depart = models.CharField(max_length=32)

'''课程表'''
class Course(models.Model):
    Cid = models.IntegerField() #课程号（主键）
    Cname = models.CharField(max_length=32)#课程名字
    Cclassid = models.IntegerField()  # 课程所属班级
    Ccreate_time = models.IntegerField() #课程创建时间
    Cend_time = models.IntegerField()  # 课程结束时间
    Tid = models.IntegerField()#教工编号（外键）

'''班级表'''
class Class_t(models.Model):
    Cclassid = models.IntegerField()  # 班级号（主键）
    Ccname = models.CharField(max_length=32) #班级名字
    Tid = models.IntegerField()  # 班主任（外键）
'''成绩表'''
class Score(models.Model):
    Sid = models.IntegerField() #学号（外键）
    Cid = models.IntegerField() #课程号（外键）
    Degree = models.IntegerField()#成绩

'''试题表'''
class Questions(models.Model):
    Qid = models.CharField(max_length=12) #账号
    Qquestion = models.CharField(max_length=255)#题目
    Qanswer = models.CharField(max_length=255)#答案
    Qoptions = models.CharField(max_length=255)#选项
    Qanalysis = models.CharField(max_length=255)#答案解析
    Qscore = models.FloatField()#试题分值
    Qdifficulty = models.CharField(max_length=2)#试题难度
    QTreeName = models.CharField(max_length=128)#所属课程
    Cid = models.CharField(max_length=12) ##所属课程号
    Qcreate_time = models.IntegerField()  # 试题创建时间