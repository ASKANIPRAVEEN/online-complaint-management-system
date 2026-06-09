from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Complaint, Feedback
from .forms import ComplaintForm, FeedbackForm # type: ignore
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationForm()
    return render(request, 'user_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_complaint')
    return render(request, 'user_login.html')

def officer_register(request):
    # Similar to user_register but with additional fields if needed
    pass

def officer_login(request):
    # Similar to user_login
    pass

def post_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user  # Associate the complaint with the logged-in user
            complaint.save()
            return redirect('complaint_list')
    else:
        form = ComplaintForm()
    return render(request, 'post_complaint.html', {'form': form})

def complaint_list(request):
    complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'complaint_list.html', {'complaints': complaints})

def feedback(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.complaint = complaint
            feedback.save()
            return redirect('complaint_list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form, 'complaint': complaint})

def admin_login(request):
    # Admin login logic
    pass