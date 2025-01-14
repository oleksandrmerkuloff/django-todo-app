from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add-task'),
    path('<int:task_id>/', views.update,),
    path('<int:task_id>', views.delete,),
]
