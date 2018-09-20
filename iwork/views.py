from django.shortcuts import render


# Create your views here.
from common.mymako import render_mako_context
from iwork.models import WorkRecord


def home(request):
    records = WorkRecord.objects.all()

    return render_mako_context(request,"/iwork/home.html",{"operator":"coco","records":records})
