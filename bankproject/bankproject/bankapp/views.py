# views
from django.http import JsonResponse
from bankapp.models import Branch
from django.shortcuts import render, redirect
from .form import DetailsForm


def home(request):
    return render(request, 'home.html')


def details(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bankapp:success')  # Redirect to the success page
    else:
        form = DetailsForm()

    return render(request, 'details.html', {'form': form})

def get_branches(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse({'branches': list(branches)})

def success(request):
    return render(request, 'success.html', {'message': 'Application Accepted'})
