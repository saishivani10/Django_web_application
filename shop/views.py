from django.shortcuts import render

def home(request):
	return render(request, 'shop/home.html')

from django.contrib.auth import login
from .forms import RegisterForm
from django.shortcuts import redirect

from django.contrib.auth.models import Group

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			# Assign user to 'regular' group
			regular_group, created = Group.objects.get_or_create(name='regular')
			user.groups.add(regular_group)
			login(request, user)
			return redirect('home')
	else:
		form = RegisterForm()
	return render(request, 'shop/register.html', {'form': form})
