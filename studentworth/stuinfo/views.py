from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404

def index(request):

    pass#stuinfo = models.stuinfo .objects.all()
    return render(request, 'stuinfo/index.html', locals())


def dashboard(request):
    pass
    return render(request, 'stuinfo/dashboard.html', locals())


def detail(request, classid):
    pass#
    """
    以显示学生考试信息详细为例，总分、单科成绩、排名等参照此例。
    :param request:
    :param asset_id:
    :return:
    """
    pass#asset = get_object_or_404(models.Asset, id=classid)
    return render(request, 'stuinfo/detail.html', locals())