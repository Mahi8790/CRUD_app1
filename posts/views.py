from django.shortcuts import render, HttpResponse, redirect
# import datetime
# # Create your views here.
# def hii_mahesh(request):
#     return render(request, 'hii_mahesh.html',{})

# def current_datetime(request):
#     now= datetime.datetime.now()
#     html="<html><body>Now Time is %s,</body></html>"%now
#     return HttpResponse(html)
# from .models import PostModel
# from .forms import PostForm
from .models import Details
from .forms import detailsform
# def create_view(request):
#     context = {}

#     form = PostForm(request.POST or None)
#     if  form.is_valid():
#         form.save()

#     context['form'] = form
#     return render(request,"hii_mahesh.html", context)
# def list_view(request):
#     #dictionary for initial data
#     #fields names as keys
#     context = {}
#     context["dataset"] = PostModel.objects.all()
#     return render(request, "list_views.html",)
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        obj = Details.objects.create(name=name, age=age, address=address)
        obj.save()
    return redirect('/')

def retrieve(request):
    details = Details.objects.all()
    return render(request, 'get_retrieve.html', {'details':details})

def edit(request, id):
    object = Details.objects.get(id=id)
    return render(request, 'edit.html', {'object':object})

def update(request, id):
    object = Details.objects.get(id=id)
    form= detailsform(request.POST, instance = object)
    if form.is_valid:
        form.save()
        objects=Details.objects.all()
    return redirect('retrieve')

def delete(id, pk):
    Details.objects.filter(id=pk).delete()
    return render('retrieve')