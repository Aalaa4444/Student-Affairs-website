from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
from .forms import *


@login_required
def editstud(request, stud_id):
    stud = studDetail.objects.filter(id=stud_id)[0]
    if request.method == "POST":
        form = editstudForm(request.POST, instance=stud)
        if form.is_valid():
            stud = form.save()
            return redirect('browse')
        return render(request, 'studs/editstud.html', {"form": form})
    form = editstudForm(instance=stud)
    return render(request, 'studs/editstud.html', {"form": form})


@login_required
def changeDepart(request, stud_id):
    stud = studDetail.objects.filter(id=stud_id)[0]
    if request.method == "POST":
        form = changeDepartForm(request.POST, instance=stud)
        if form.is_valid():
            stud = form.save()
            return redirect('browse')
        return render(request, 'studs/changeDepart.html', {"form": form})
    form = changeDepartForm(instance=stud)
    return render(request, 'studs/changeDepart.html', {"form": form})


@login_required
def changeStatus(request, stud_id):
    stud = studDetail.objects.filter(id=stud_id)[0]
    if request.method == "POST":
        form = changeStatusForm(request.POST, instance=stud)
        if form.is_valid():
            stud = form.save()
            return redirect('browse')
        return render(request, 'studs/changeStatus.html', {"form": form})
    form = changeStatusForm(instance=stud)
    return render(request, 'studs/changeStatus.html', {"form": form})
    

@login_required
def deletestud(request, stud_id):
    #if not request.user.is_superuser:
       # return redirect('browse')
    studDetail.objects.filter(id=stud_id)[0].delete()
    return redirect('browse')



@login_required
def returnstud(request):
    toDelete = studing.objects.filter(studedBy = request.user)
    toDelete.delete()
    return redirect('browse')

@login_required

def studDetails(request, stud_id):
    stud = studDetail.objects.filter(id=stud_id)[0]
    studings = studing.objects.filter(studedstud=stud)
    context = {
        "stud": stud,
    }
    context['cell'] = studings.exists()
    if context['cell']:
        context['cellByUser'] = studings[0].studedBy == request.user
        context['cellUser'] = studings[0].studedBy
        context['returnDate'] = studings[0].returnDate
    else:
        context['cellByUser'] = False
        

    return render(request, 'studs/details.html', context)

def browse(request):
    studs = studDetail.objects.all()
    filteredstuds = studFilter(request.GET, queryset=studs)
    return render(request, 'studs/browse.html', {'studs': filteredstuds})


@login_required
def addstud(request):
    if request.method == "POST":
        form = addstudForm(request.POST)
        if form.is_valid():
            stud = form.save()
            stud.save()
            return redirect('browse')
        return render(request, 'studs/addstud.html', {"form": form})
    form = addstudForm()
    return render(request, 'studs/addstud.html', {"form": form})