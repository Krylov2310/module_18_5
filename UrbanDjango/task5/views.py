from django.shortcuts import render
from .forms import UserRegister

# Create your views here.
users = ['Urban', 'Maikl', 'Эдисон']
context = {'base_name': 'Домашнее задание по теме "Формы отправки данных. HTML и Django формы"',
           'base_tsul': 'Цель: понять на практике как работают POST запросы в Django. '
                        'Использовать формы для обработки этих запросов.',
           'base_task': 'Задача "Имитация регистрации":',
           'base_time': 'Дата: 09.12.2024 г.',
           'base_student': 'Крылов Эдуард Васильевич'
           }


def sign_by_django(request):
    context['base_title'] = 'Регистрация - sign_by_django'

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            set_users(username, password, repeat_password, age)
        context['form'] = form
    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_html(request):
    context['base_title'] = 'Регистрация - sign_up_by_html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        set_users(username, password, repeat_password, age)
    return render(request, 'fifth_task/registration_page.html', context)


def set_users(username, password, repeat_password, age):
    if username in users:
        context['message'] = f'Пользователь {username} уже зарегистрирован в системе'
    elif password != repeat_password:
        context['message'] = 'Данные пароли не совпадают'
    elif len(str(age)) >= 4:
        context['message'] = 'Число символов не должно превышать трёх символов и не равно нулю!'
    elif age <= 18 or age >= 100:
        context['message'] = 'Ваш возраст должен быть не менее 18 и не более 100 лет!'
    else:
        context['message'] = f'Приветствуем, {username}!'
        users.append(username)
    return context, users
