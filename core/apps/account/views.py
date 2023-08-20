from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from core.apps.account.forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return HttpResponse(f'<h4>Создан аккаунт {username}!</h4>')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')
