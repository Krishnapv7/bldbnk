from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Donor
from .forms import DonorForm
import csv


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        
        if user is not None and user.is_active:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request, "❌ Invalid username or password. Please try again.")
    return render(request,'donars/login.html')
    

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    blood_groups = ['A+','A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    return render(request,'donars/dashboard.html', {'blood_groups': blood_groups})


@login_required
def donor_list(request, blood_group):
    donors = Donor.objects.filter(blood_group=blood_group)
    return render(request, 'donars/donar_list.html', {'donors': donors, 'blood_group': blood_group})


@login_required
def add_donor(request):
    if request.method == "POST":
        # Handle CSV Upload
        if "upload_csv" in request.POST:
            csv_file = request.FILES.get("csv_file")
            
            if not csv_file:
                messages.error(request, "Please select a CSV file to upload")
            elif not csv_file.name.endswith('.csv'):
                messages.error(request, "Invalid file type. Please upload a CSV file")
            else:
                try:
                    # Read and reset file pointer
                    csv_file.seek(0)
                    decoded_file = csv_file.read().decode("utf-8-sig").splitlines()
                    reader = csv.DictReader(decoded_file)
                    
                    # Validate CSV structure
                    required_fields = ['name', 'address', 'blood_group', 'phone_number', 'last_donation_date']
                    if not reader.fieldnames:
                        messages.error(request, "CSV file is empty")
                    elif not all(field in reader.fieldnames for field in required_fields):
                        messages.error(request, f"CSV missing columns. Required: {', '.join(required_fields)}")
                    else:
                        count = 0
                        errors = []
                        for i, row in enumerate(reader, start=2):  # Start at line 2 (1-based)
                            try:
                                Donor.objects.create(
                                    name=row['name'],
                                    address=row['address'],
                                    blood_group=row['blood_group'].strip(),
                                    phone_number=row['phone_number'],
                                    last_donation_date=row['last_donation_date'] or None
                                )
                                count += 1
                            except Exception as e:
                                errors.append(f"Row {i}: {str(e)}")
                        
                        if count > 0:
                            messages.success(request, f"Successfully uploaded {count} donors!")
                        if errors:
                            messages.error(request, f"Errors in {len(errors)} rows: {'; '.join(errors[:3])}")
                            
                except Exception as e:
                    messages.error(request, f"CSV processing error: {str(e)}")
            
            return redirect('add_donor')

        # Handle Manual Form Submission
        elif "add_manual" in request.POST:
            form = DonorForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Donor added successfully!")
                return redirect('add_donor')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field.title()}: {error}")
    
    # For GET requests or failed POST
    form = DonorForm()
    return render(request, "donars/add_donar.html", {"form": form})


@login_required
def edit_donor(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    if request.method == "POST":
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_list', blood_group=donor.blood_group)
    else:
        form = DonorForm(instance=donor)
    return render(request, 'donars/edit_donar.html', {'form': form})


@login_required
def delete_donor(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    donor.delete()
    return redirect('donor_list', blood_group=donor.blood_group)