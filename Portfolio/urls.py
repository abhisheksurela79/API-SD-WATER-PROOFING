from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path("", views.AllFilesListView.as_view(), name='all-files-list')
]
