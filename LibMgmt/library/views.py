from django.shortcuts import render,redirect
from .models import *
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import FormView
from .forms import *

from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

class BookList(ListView):
    model = BookDataset
    template_name = 'booklist.html'
    context_object_name = 'book'


class AddBooks(FormView):
    template_name = 'Addbook.html'
    form_class = Addbook
    success_url = '/book'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Navbr(TemplateView):
    template_name = 'navbar.html'


class BookIssueRecords(ListView):
    model = IssueRecords
    template_name = 'Issue.html'
    context_object_name = 'issue'


class BookIssue(CreateView):
    template_name = 'Issueform.html'
    form_class = Issuebook
    success_url = '/issue'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StudentDetail(ListView):
    model = StudentRecords
    template_name = 'studentRecords.html'
    context_object_name = 'student'


class AddStudent(CreateView):
    template_name = 'addstudent.html'
    form_class = StudentData
    success_url = '/student'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateStudent(UpdateView):
    model = StudentRecords
    fields = ('__all__')
    template_name = 'addstudent.html'
    success_url = "/student"


class UpdateBooks(UpdateView):
    model = BookDataset
    fields = ('__all__')
    template_name = 'Addbook.html'
    success_url = "/book"


class DeleteStudent(DeleteView):
    model = StudentRecords
    success_url = "/student"


class DeleteBooks(DeleteView):
    model = BookDataset
    success_url = "/book"


def registeradmin(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/home')
    context = {'form': form}
    return render(request,'Admin/AdminPage.html', context)


def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'Admin/Login.html', context)

class Homepage(TemplateView):
    template_name = 'home.html'
