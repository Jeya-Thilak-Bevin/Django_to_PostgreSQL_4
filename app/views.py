from django.shortcuts import render
from .models import Company
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=="POST":
       company=Company()
       code=request.POST.get('Co_code')
       name=request.POST.get('Co_name')
       ibr_name=request.POST.get('IBR_name')
       face_value=request.POST.get('Face_value')
       date_of_inco=request.POST.get('DATE_OF_INCO')
       cnvtopubdt=request.POST.get('CNVTOPUBDT')
       company.Co_code=code
       company.Co_name=name
       company.IBR_name=ibr_name
       company.Face_value=face_value
       company.DATE_OF_INCO=date_of_inco
       company.CNVTOPUBDT=cnvtopubdt
       company.save()
       return HttpResponse("<h1>Thanks For Contact Us</h1>")
    
    return render(request,'index.html')