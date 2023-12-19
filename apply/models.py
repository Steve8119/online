# apps/bursary/models.py
from django.db import models

class Applicant(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    institution = models.CharField(max_length=100)
    education_level = models.CharField(max_length=50)
    constituency = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    result = models.FileField(upload_to='results/')
    fee_statement = models.FileField(upload_to='fee_statements/')
    allocation_status = models.CharField(max_length=50, default='pending')
    allocated_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def update_allocation_status(self, status, amount=0):
        self.allocation_status = status
        if status == 'allocated':
            self.allocated_amount = amount
        self.save()

class Allocation(models.Model):
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE)
    allocation_amount = models.DecimalField(max_digits=10, decimal_places=2)
    allocation_status = models.CharField(max_length=50)
