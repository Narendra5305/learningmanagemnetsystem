from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Instructorform , Studentform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from .models import Course,Assignment,Solution
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def mainpage(request):
    return render(request,'learning/index.html')

@login_required(login_url="/learning/UserInstructorLogins/")
def instructormain(request):
    return render(request,'learning/instructormain.html')

@login_required(login_url="/learning/UserstudentLogins/")
def studentmain(request):
    return render(request,'learning/studentmain.html')

def UserInstructorCreate(request):
    if request.method=='POST':
        form=Instructorform(request.POST)
        if form.is_valid():
            form.save()

            return redirect('instructormain')
    else:
        form=Instructorform()
    return render(request,'learning/signuppage.html',{'form':form,'type':'Submit'})

def UserInstructorLogin(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('courcelist')
    else:
        form=AuthenticationForm()
    return render(request,'learning/signinpage.html',{'form':form,'type':'Login'})



def UserStudentCreate(request):
    if request.method=='POST':
        form=Studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentmain')
    else:
        form=Studentform()
    return render(request,'learning/signuppage.html',{'form':form,'type':'Submit'})

def UserStudentLogin(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('courseforstudent')
    else:
        form=AuthenticationForm()
    return render(request,'learning/signinpage.html',{'form':form,'type':'Login'})

def signout_page(request):
    if request.method=='POST':
        logout(request)
        return redirect('mainpage')
    return render(request,'learning/logoutpage.html')

class cource_create_view(LoginRequiredMixin,CreateView):
    model=Course
    fields='__all__'
    template_name='learning/coursecreate.html'
    success_url = reverse_lazy("courcelist")
    login_url="/learning/UserInstructorLogins/"


class cource_list_view(LoginRequiredMixin,ListView):
    model=Course
    context_object_name='Courcess'
    template_name='learning/courselist.html'
    login_url="/learning/UserInstructorLogins/"

class cource_detail_view(LoginRequiredMixin,DetailView):
    model=Course
    context_object_name='course'
    template_name='learning/corcesdetail_inst.html'
    login_url="/learning/UserInstructorLogins/"

class cource_update_view(LoginRequiredMixin,UpdateView):
    model=Course
    fields='__all__'
    template_name='learning/coursecreate.html'
    success_url = reverse_lazy("courcelist")
    login_url="/learning/UserInstructorLogins/"

class cource_delete_view(LoginRequiredMixin,DeleteView):
    model=Course
    template_name='learning/delete.html'
    success_url = reverse_lazy("courcelist")
    login_url="/learning/UserInstructorLogins/"


#assignment crud

class Assignment_list_view(LoginRequiredMixin,ListView):
    model=Assignment
    context_object_name='Assignments'
    template_name='learning/Assignmentlist.html'
    login_url="/learning/UserInstructorLogins/"

class Assignment_create_view(LoginRequiredMixin,CreateView):
    model= Assignment
    fields='__all__'
    template_name='learning/coursecreate.html'
    success_url = reverse_lazy("Assignment_list_view")
    login_url="/learning/UserInstructorLogins/"


class  Assignment_detail_view(LoginRequiredMixin,DetailView):
    model=Assignment
    context_object_name='assignment'
    template_name='learning/assignmentDetail.html'
    login_url="/learning/UserInstructorLogins/"

class  Assignment_update_view(LoginRequiredMixin,UpdateView):
    model=Assignment
    fields='__all__'
    template_name='learning/coursecreate.html'
    success_url = reverse_lazy("Assignment_list_view")
    login_url="/learning/UserInstructorLogins/"

class  Assignment_delete_view(LoginRequiredMixin,DeleteView):
    model=Assignment
    template_name='learning/delete.html'
    success_url = reverse_lazy("Assignment_list_view")
    login_url="/learning/UserInstructorLogins/"



#student assignments crud

class course_list_view_for_student(LoginRequiredMixin , ListView):
    model=Course
    context_object_name='courses'
    template_name='learning/courcepageforstudent.html'
    login_url="/learning/UserstudentLogins/"


class assignment_list_view_for_student(LoginRequiredMixin ,ListView):
    model=Assignment
    context_object_name='assignments'
    template_name='learning/assignmentpageforstudent.html'
    login_url="/learning/UserstudentLogins/"
    
class assignment_detail_view_for_student(LoginRequiredMixin ,DetailView):
    model=Assignment
    context_object_name='assignment'
    template_name='learning/assdetailstudent.html'
    login_url="/learning/UserstudentLogins/"

class solution_create_view_ofstudent(LoginRequiredMixin ,CreateView):
    model=Solution
    template_name='learning/coursecreate.html'
    fields = '__all__'
    login_url="/learning/UserstudentLogins/"
    success_url=reverse_lazy('assignmentforstudent')
