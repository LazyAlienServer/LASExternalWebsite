from django.urls import path
from . import views
from .views import ProfileView


app_name = 'users'
urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
