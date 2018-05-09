from django.urls import path
from . import views

# имя приложения
app_name = 'issues'
urlpatterns = [
    path('show/', views.index, name='index'),
    path('details/<int:task_id>', views.show_details, name='details'),
]
