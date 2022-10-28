from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from.models import Form
# Create your views here.
def index(request):
    if request.method =='POST':
        image_title =request.POST['title']
        image = request.FILES['image']
        form = Form.objects.create(Title=image_title,image=image)
        if form:
            return HttpResponseRedirect('/')
    return render(request,"index.html" )
def about(request):  
    return render(request,"about.html")
def contact(request):
    form = Form.objects.all()
    print(form)
    return render(request,"contact.html",{'form':form,'name':"dhian"})
