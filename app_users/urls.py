from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('auth/', include('social_django.urls', namespace='social')),
]