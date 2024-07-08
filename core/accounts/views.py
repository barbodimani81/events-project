from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User created successfully!'}, status=201)
        else:
            return JsonResponse({'errors': form.errors.as_json()}, status=400)
    elif request.method == 'GET':
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    return JsonResponse({'error': 'Only POST and GET methods allowed!'}, status=405)


def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard after successful login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'signin.html')


def home_view(request):
    return render(request, 'home.html')

