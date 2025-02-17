from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register.as_view(), name='Register'),
    path('update/<int:pk>', views.Update.as_view(), name='Update'),
    path('delete/<int:pk>', views.Delete.as_view(), name='Delete'),
]
