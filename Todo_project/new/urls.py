from django.urls import path
from . import views

urlpatterns = [ 
    path('addtask/', views.addtask, name="addtask"),
    path('done/<int:pk>/',views.done,name="done"),
    path('undone/<int:pk>/',views.undone,name="undone"),
    path('edit/<int:pk>/',views.edit,name="edit"),
    path('delete/<int:pk>/',views.delete,name="delete")
]