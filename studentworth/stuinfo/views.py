from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.db import models
from . import models

def index(request):

    stuinfos = models.finalexam.objects.all()
    return render(request, 'stuinfo/index.html', locals())


def dashboard(request):
    Twoline_Scitotal = models.finalexam.objects.filter(Scisubjecttotal__gte = 338).filter( Art_SciClass = 2).count()      #理科本科线总人数
    Twoline_Arttotal = models.finalexam.objects.filter(Artsubjecttotal__gte = 406).filter( Art_SciClass = 2).count()       #文科本科线总人数


 


    return render(request, 'stuinfo/dashboard.html', locals())


def detail(request, Sclass_id):
    pass#
    """
    以显示学生考试信息详细为例，总分、单科成绩、排名等参照此例。
    :param request:
    :param asset_id:
    :return:
    """
    stuinfo = get_object_or_404(models.stuinfo, id=stuinfo_id)
    return render(request, 'stuinfo/detail.html', locals())

