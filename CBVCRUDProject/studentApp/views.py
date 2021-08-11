from django.db import models
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Student
from django.urls import reverse_lazy

# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('retrive')

class StundentListView(ListView):
    model = Student

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('retrive')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('retrive')



