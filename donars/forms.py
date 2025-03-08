from django import forms
from .models import Donor
from django.forms import DateInput

class DonorForm(forms.ModelForm):
    
    class Meta:
        model = Donor
        fields = ['name', 'address', 'blood_group', 'phone_number', 'last_donation_date']
        widgets = {
            'last_donation_date': DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'last_donation_date': 'Last Donation Date (YYYY-MM-DD)'
        }
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        donor_id = self.instance.id
        if Donor.objects.filter(phone_number=phone_number).exclude(id=donor_id).exists():
            raise forms.ValidationError("A donor with this phone number already exists.")
        return phone_number

    def __init__(self, *args, **kwargs):
        super(DonorForm, self).__init__(*args, **kwargs)
        self.fields['blood_group'].choices = [("","Select Blood Group")] + [
            (key, value) for key, value in self.fields['blood_group'].choices if key
        ]