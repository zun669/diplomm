from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.my_patients, name='my_patients'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('print/', views.print_doc, name='print_doc'),
    path('recommendation/<int:pk>/', views.generate_recommendation, name='generate_recommendation')
]