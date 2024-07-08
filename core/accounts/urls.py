from django.urls import path
from .views import signup, signin_view, home_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('', home_view, name='home'),
]
