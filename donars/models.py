from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    blood_group = models.CharField(max_length=5, choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ])
    phone_number = models.CharField(max_length=15,unique=True)
    last_donation_date = models.DateField()
    uploaded_file = models.FileField(upload_to="uploads/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"
    

class BloodRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Done', 'Done'),
        ('Expired', 'Expired'),
    ]
    patient_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5, choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ])
    units_needed = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15)
    hospital_name = models.CharField(max_length=200)
    reason = models.TextField()
    requested_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.patient_name} ({self.blood_group})"
