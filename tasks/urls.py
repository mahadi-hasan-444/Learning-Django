from django.urls import path
from tasks.views import show_task  #jekhan theke import korsi
urlpatterns=[
   path('show-task/',show_task)
]