from datetime import datetime
import re

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from mq.models import CustomUser


def index(request):
    return render(request, 'mq/index.html')

def account(request):
    return render(request, 'mq/profile.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

@require_POST
@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        phone_num = request.POST.get('phone_num')

        # Проверяем, существует ли пользователь с указанным номером телефона
        if CustomUser.objects.filter(phone_num=phone_num).exists():
            error_message = {'error': 'Пользователь с таким номером телефона уже зарегистрирован',
                             'solution': 'Если это ваш аккаунт, пожалуйста, войдите. Если вы забыли пароль, '
                                         'воспользуйтесь функцией восстановления пароля.'}
            return JsonResponse(error_message, status=400)

        # Продолжаем создание пользователя
        email = request.POST.get('email')
        password = request.POST.get('password')
        years_str = request.POST.get('years')
        fio = request.POST.get('fio')

        # Преобразуем входную строку в формат 'YYYY-MM-DD'
        try:
            years_obj = datetime.strptime(years_str, '%d.%m.%Y').date()
        except ValueError:
            return JsonResponse({'error': 'Некорректная дата'}, status=400)

        # Создаем пользователя
        user = CustomUser.objects.create_user(phone_num=phone_num, email=email, password=password, years=years_obj,
                                              fio=fio)

        # После успешной регистрации перенаправляем пользователя на страницу "account"
        return HttpResponseRedirect(reverse('account'))

    else:
        return JsonResponse({'error': 'Метод не разрешен'}, status=405)

@login_required
def account_view(request):
    user = request.user  # Предполагается, что пользователь авторизован
    return render(request, 'profile.html', {'user': user})
