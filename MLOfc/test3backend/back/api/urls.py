from django.urls import path
from .views import *

urlpatterns = [
    path('', FileUploadView.as_view()),
    path('dataset/', DatasetView.as_view()),
    path('dataset2/', DatasetView2.as_view()),
    path('dataset3/', DatasetView3.as_view())

]