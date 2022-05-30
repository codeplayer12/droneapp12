from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/',views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser,name='register'),

    path('',views.home, name='home'),
    path('upload/',views.uploadData, name='upload' ),
    path('projects/', views.projects, name='projects'),
    path('reports/', views.reports, name='reports'),
    # path('profile/', views.profile, name='profile'),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
