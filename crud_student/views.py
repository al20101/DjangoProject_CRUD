
from django.shortcuts import render, redirect
from crud_student.models import Students
from crud_student.forms import StudentsForm



def initial (request): # atgriez uz sākuma lapu
    return render(request,"initial.html")


def student_add(request): # pievieno studentu caur medoti POST un atgriez uz tabulas lapu
    if request.method == 'POST':
        form=StudentsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = StudentsForm()
    return render(request, 'index.html', {'form': form})

def show ( request ): # apskata atgriez visus ierakstus par studenties
    studentslist = Students.objects.all()
    return render(request, 'show.html', {'studentslist': studentslist})

def edit ( request,id): # sanem studentu pec ID  un atver labošanas lapu
    student = Students.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})

def update ( request,id): # sanem studentu pec ID un aizvieto datus no formas un atver tabulas lapu
    student = Students.objects.get(id=id)
    form = StudentsForm(request.POST , instance=student)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'student': student})

def delete ( request,id): # sanem studentu pec ID un izdzeš no tabulas
    student = Students.objects.get(id=id)
    student.delete()
    return redirect("/show")