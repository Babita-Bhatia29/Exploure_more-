from django.shortcuts import render
from application.models import Category,Destination,images1
# Create your views here.
def indexpage(request):
    x=Category.objects.all()
    y=Destination.objects.all()
    z=images1.objects.all()
    return render(request,"index.html",{"x":x,"y":y,"z":z,})



