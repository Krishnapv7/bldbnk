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
