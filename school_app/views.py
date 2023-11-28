from django.shortcuts import render, HttpResponseRedirect
from .models import Student
from .forms import AddStudentForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class HomePage(TemplateView):  # this class just for render the home page template
    template_name = 'home.html'


class StudentList(ListView):  # this class displays list of all students on template
    model = Student
    queryset = Student.objects.all()
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 3


# this class displays form for create new student
class AddStudent(SuccessMessageMixin, CreateView):
    model = Student
    form_class = AddStudentForm
    template_name = 'add_student.html'
    context_object_name = 'form'
    success_url = '/StudentList/'
    success_message = 'Student Added Successfully!!!'


# this class displays form for update existing student
class UpdateStudent(SuccessMessageMixin, UpdateView):
    model = Student
    form_class = AddStudentForm
    template_name = 'update_student.html'
    context_object_name = 'form'
    success_url = '/StudentList/'
    success_message = 'Updated successfully!!!'


# this function takes id of specific student and delete that student
def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    messages.add_message(request, messages.SUCCESS,
                         'Student Deleted Successfully...')
    return HttpResponseRedirect('/StudentList/')


class ContactUsPage(TemplateView):  # this class just for render the contact us template
    template_name = 'contact_us.html'
