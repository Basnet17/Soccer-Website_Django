from django.shortcuts import render
from .models import playersInfo
# Create your views here.
def playersInfo_detail_view(request):
    obj = playersInfo.objects.all()
    # context ={
    #     "Name":obj.Name,
    #     "Club":obj.Club
    # }
    context = {
        'object':obj
    }
    return render(request, 'players/detail.html', context)
