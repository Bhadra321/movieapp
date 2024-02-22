from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import MovieInfo
from . forms import Movieform
# Create your views here.
def myfunction(request):
    return HttpResponse("hello world")
def add(request,a,b):
    return HttpResponse(a+b)
def index(request):
    return render(request,'index.html')
def print(request):
    movie_details={
        'title':'doctorg',
        'summury':'comedy',
        'year':2019,
        'sucsess':True
    }
    return render(request,"index.html",movie_details)

def create(request):
    return render(request,'create.html')
def list(request):
    return render(request,'list.html')
def edit(request):
    return render(request,'edit.html')


def new(request):
    movie=MovieInfo.objects.all()
    cotext={
        'movie_list':movie
    }
    return render(request,'new.html',cotext)
def detail(request,movie_id):
    movie=MovieInfo.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
def add_movie(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        year=request.POST['year']
        img=request.FILES['img']
        movie=MovieInfo(title=title,desc=desc,year=year,img=img)
        movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=MovieInfo.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('new')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=MovieInfo.objects.get(id=id)
        movie.delete()
        return redirect("new")
    return render(request,'delete.html')


