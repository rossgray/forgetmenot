from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('people/<int:pk>/', views.PersonDetail.as_view(), name='person_detail'),
    path('people/add/', views.PersonCreate.as_view(), name='person_create'),
]
