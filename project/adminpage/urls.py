from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_students_excel, name="upload-xlsx")
]