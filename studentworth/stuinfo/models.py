from django.db import models
import uuid
# Create your models here.


#————————————————————————
#————————————————————————
#学生基本信息
#————————————————————————
#————————————————————————
class sudentname(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sudent_schoolid = models.PositiveIntegerField('学号',default=0)
    sudent_name = models.CharField('姓名',max_length=50,default=0)
    sudent_name_new = models.CharField('新增姓名',max_length=50,default=0)
    sudent_age = models.IntegerField('年龄',default=0)
    sudent_gender = models.CharField('性别',max_length=4,default=0)
    sudent_phonenum = models.BigIntegerField('手机号码',default=0)
    def __str__(self):
        return self.name

    class Meta:
        db_table = '17_sudentname'
        verbose_name = '2017届学生注册信息表'



#————————————————————————
#————————————————————————
#学生考试成绩
#————————————————————————
#————————————————————————
class sudentsuccess(models.Model):
    success_id = models.AutoField(primary_key=True)
    sudent_schoolid = models.PositiveIntegerField('学号',default=0)
    sudent_classid = models.PositiveIntegerField('班级',default=0)
    chitotal = models.FloatField('语文总分',default=0)      
    mattotal = models.FloatField('数学总分',default=0)        
    engtotal = models.FloatField('英语总分',default=0)	      
    phytotal = models.FloatField('物理总分',default=0)	        
    chetotal = models.FloatField('化学总分',default=0)	     
    orgtotal = models.FloatField('生物总分',default=0)	       	
    poltotal = models.FloatField('政治总分',default=0)	       
    histotal = models.FloatField('历史总分',default=0)	       
    geototal = models.FloatField('地理总分',default=0)	
    Art_SciClass = models.PositiveIntegerField('文理分科',default=0)	  # 0 未定义，1文科班 2理科班 3综合班，暂不启用。    
    Artsubjecttotal = models.FloatField('文科总分',default=0)
    Scisubjecttotal = models.FloatField('理科总分',default=0)	   

    class Meta:
        abstract = True

class finalexam(sudentsuccess):
    #联考成绩排名，因为拿不到所有联考学生的成绩，只能存储已下发的具体排名。
    chiurbrank = models.PositiveIntegerField('语文单科联考排名',default=0)      
    maturbrank = models.PositiveIntegerField('数学单科联考排名',default=0)        
    engurbrank = models.PositiveIntegerField('英语单科联考排名',default=0)	      
    phyurbrank = models.PositiveIntegerField('物理单科联考排名',default=0)	        
    cheurbrank = models.PositiveIntegerField('化学单科联考排名',default=0)	     
    orgurbrank = models.PositiveIntegerField('生物单科联考排名',default=0)	       	
    polurbrank = models.PositiveIntegerField('政治单科联考排名',default=0)	       
    hisurbrank = models.PositiveIntegerField('历史单科联考排名',default=0)	       
    geourbrank = models.PositiveIntegerField('地理单科联考排名',default=0)	
    
    Artsubjecturbrank = models.PositiveIntegerField('文科总分联考排名',default=0)
    Scisubjecturbrank = models.PositiveIntegerField('理科总分联考排名',default=0)
    finalexamnum = models.PositiveIntegerField('考试编号',default=0) #考试的场次，比如高二秋季学期：201901，前端显示时将重命名为高二（上）学期期考成绩。
    def __str__(self):
        return self.name
    class Meta:
        db_table = '17_sudentfinalexam'
        verbose_name = '2017届学生各学期期考成绩汇总表'

class monthlyexam(sudentsuccess):
    monthlyexam = models.PositiveIntegerField('考试编号',default=0) #考试的场次，比如高二秋季学期第一次月考：2018101801，前端显示时将重命名为2018年秋第一次月考。
    def __str__(self):
        return self.name
    class Meta:
        db_table = '17_sudentmonthlyexam'
        verbose_name = '2017届学生各学期月考成绩汇总表'


#————————————————————————
#————————————————————————
#班级基本信息
#————————————————————————
#————————————————————————
class Sclassname(models.Model):
    
    Sclass_id = models.PositiveIntegerField('班级ID',default=0)
    Sclass_name = models.CharField('班级名称',max_length=50,default=0)
    Sclass_category = models.CharField('班级文理分类',max_length=50,default=0) #文科 理科 综合 此处直击存储说明文本，可任意增
    Sclass_type = models.CharField('班级成绩分类',max_length=50,default=0) #尖子班 重点班 普通班 融职班  此处直击存储说明文本，可任意增
    Sclass_introduction = models.CharField('班级所在阶段',max_length=50,default=0) #高一（上）学期 高一（下）学期  已毕业转往职校  
    Sclass_Abbreviations  = models.CharField('班级阶段简写',max_length=50,default=0) #高一（上） 已毕业 
    def __str__(self):
        return self.name

    class Meta:
        db_table = '17_sudentclassname'
        verbose_name = '2017届各班级基本信息表'
