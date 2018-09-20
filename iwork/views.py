from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from common.mymako import render_mako_context
from iwork.models import WorkRecord

@csrf_exempt
def home(request):
    theme = request.POST.get("theme","")
    content = request.POST.get('content',"")
    record1 = WorkRecord(theme=theme,content=content,operstor="coco")
    record1.save
    records = WorkRecord.objects.all()

    return render_mako_context(request,"/iwork/home.html",{"operator":"coco","records":records})

