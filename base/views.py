from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    students = Student.objects.all()
    paginator = Paginator(students, 4)
    page = request.GET.get('page')
    try:
        studs = paginator.page(page)
    except PageNotAnInteger:
        studs = paginator.page(1)
    except EmptyPage:
        studs = paginator.page(paginator.num_pages)
    
    context = {'students': students, 'studs':studs}
    return render(request, 'index.html', context)

def addStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()   #Creates the user object
            return redirect('/')
    
    
    context = {'form': form}
    return render(request, 'addStudent.html', context)

def delete(request, pk):
    to_delete = Student.objects.get(id=pk)
    to_delete.delete()
    return redirect('/')

def modify(request, pk):
    toUpdate = Student.objects.get(id=pk)
    form = StudentForm(instance=toUpdate)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=toUpdate)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'modify.html', context)
