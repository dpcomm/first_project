from django.urls import path

from . import views

urlpatterns = [
    path('',views.main_def),
    path('join/',views.join,name='register'),
    path('login/',views.login_view,name='login'),
]
