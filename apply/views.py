# apps/bursary/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ApplicantForm
from .models import Applicant, Allocation

def apply_bursary(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('check_bursary_application_status')
    else:
        form = ApplicantForm()
    return render(request, 'bursary/apply_bursary.html', {'form': form})

def check_bursary_application_status(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        try:
            applicant = Applicant.objects.get(phone_number=phone_number)
            return render(request, 'bursary/check_bursary_application_status.html', {'applicant': applicant})
        except Applicant.DoesNotExist:
            return render(request, 'bursary/check_bursary_application_status.html', {'error_message': 'Applicant with this phone number does not exist.'})
    else:
        return render(request, 'bursary/check_bursary_application_status.html')

from .models import Applicant, Allocation

# Existing views...

def admin_dashboard(request):
    applicants = Applicant.objects.all()
    return render(request, 'bursary/admin_dashboard.html', {'applicants': applicants})

def allocate_applicant(request, applicant_id):
    applicant = get_object_or_404(Applicant, id=applicant_id)
    # Add logic to allocate the applicant
    # For example, set allocation_status to 'allocated' and set allocated_amount
    applicant.allocation_status = 'allocated'
    applicant.allocated_amount = 4000  # Set the actual amount
    applicant.save()
    return redirect('admin_dashboard')

def not_allocate_applicant(request, applicant_id):
    applicant = get_object_or_404(Applicant, id=applicant_id)
    # Add logic to mark the applicant as not allocated
    # For example, set allocation_status to 'not_allocated' and set allocated_amount to 0
    applicant.allocation_status = 'not_allocated'
    applicant.allocated_amount = 0
    applicant.save()
    return redirect('admin_dashboard')





def get_applicants_by_status(status):
    if status == 'allocated':
        return Applicant.objects.filter(allocation_status='allocated')
    else:
        return Applicant.objects.filter(allocation_status='not_allocated')




def allocated_applicants(request):
    allocated_applicants = get_applicants_by_status('allocated')
    return render(request, 'bursary/allocated_applicants.html', {'allocated_applicants': allocated_applicants})

def not_allocated_applicants(request):
    not_allocated_applicants = get_applicants_by_status('not_allocated')
    return render(request, 'bursary/not_allocated_applicants.html', {'not_allocated_applicants': not_allocated_applicants})