from django.urls import path
from .views import StudentCreateView, StudentDeleteView, StudentUpdateView, StundentListView
urlpatterns = [
    path('create/',StudentCreateView.as_view(),name='create'),
    path('retrive/',StundentListView.as_view(),name='retrive'),
    path('update/<int:pk>/',StudentUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',StudentDeleteView.as_view(),name='delete'),
]