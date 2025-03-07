from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('donors/<str:blood_group>/', views.donor_list, name='donor_list'),
    path('add/', views.add_donor, name='add_donor'),
    path('edit/<int:donor_id>/', views.edit_donor, name='edit_donor'),
    path('delete/<int:donor_id>/', views.delete_donor, name='delete_donor'),
]
