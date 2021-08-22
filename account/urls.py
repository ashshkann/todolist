from django.urls import path
from .views import viewForm, viewregister, viewlogout

urlpatterns = [
    path('login/', viewForm, name='Login'),
    path('register/', viewregister, name='Register'),
    path('logout/', viewlogout, name='Logout')
]
