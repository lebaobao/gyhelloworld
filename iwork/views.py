from django.shortcuts import render


# Create your views here.
from framework.common.mymako import render_mako_context


def home(request):

    return render_mako_context(request,"/iwork/home.html",{"operator":"CoCo"})
