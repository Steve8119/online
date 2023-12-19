# apps/bursary/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apply_bursary, name='apply_bursary'),
    path('check_bursary_application_status/', views.check_bursary_application_status, name='check_bursary_application_status'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('allocate_applicant/<int:applicant_id>/', views.allocate_applicant, name='allocate_applicant'),
    path('not_allocate_applicant/<int:applicant_id>/', views.not_allocate_applicant, name='not_allocate_applicant'),
    path('allocated/', views.allocated_applicants, name='allocated_applicants'),
    path('not_allocated/', views.not_allocated_applicants, name='not_allocated_applicants'),
]
