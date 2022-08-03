from django.urls import path
from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]
