from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_search, name='student_search'),
    path('search_results/', views.search_results, name='search_results'),
]
