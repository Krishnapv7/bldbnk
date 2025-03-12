from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('donors/<str:blood_group>/', views.donor_list, name='donor_list'),
    path('add/', views.add_donor, name='add_donor'),
    path('edit/<int:donor_id>/', views.edit_donor, name='edit_donor'),
    path('delete/<int:donor_id>/', views.delete_donor, name='delete_donor'),
    
    path('register-donor/', views.register_donor, name='register_donor'),
    path('blood-request/', views.blood_request, name='blood_request'),
    path('blood-request-list/', views.blood_request_list, name='blood_request_list'),
    path('delete-blood-request/<int:id>/', views.delete_blood_request, name='delete_blood_request'), 
    path("update-blood-request-status/", views.update_blood_request_status, name="update_blood_request_status"),

]
