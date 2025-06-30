from django.urls import path

from .views import index, detail, login_view, profile_view, resume_view, contacts_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),    
    path('post/<int:id>', detail, name='detail'),
    path('login/', login_view, name='login_view'),
    path('logout', LogoutView.as_view(), name='logout_view'), #FIXME: doesn't work (error code 405)
    path('profile', profile_view, name='profile_view'),
    path('resume', resume_view, name='resume_view'),
    path('contacts', contacts_view, name='contacts_view'),

]