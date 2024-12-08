from django.shortcuts import render

context = {'base_name': 'Домашнее задание по теме "Базовые HTML тэги в шаблонах"',
           'base_tsul': 'Цель: применить изученные теги HTML, написав многостраничный проект.',
           'base_task': 'Задача "Первичная структура":',
           'base_time': 'Дата: 07.12.2024г.',
           'base_student': 'Крылов Эдуард Васильевич'
           }


# Create your views here.
def platform_(request):
    context['base_title'] = 'Главная'
    return render(request, 'third_task/platform_.html', context)


def games_(request):
    context['base_title'] = 'Игры'
    return render(request, 'third_task/games_.html', context)


def cart_(request):
    context['base_title'] = 'Корзина'
    context['base_cart'] = 'Извините, ваша корзина пуста'
    return render(request, 'third_task/cart_.html', context)
