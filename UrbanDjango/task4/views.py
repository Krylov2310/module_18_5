from django.shortcuts import render

menu = {'Навигационная страница': ["http://127.0.0.1:8000/"], 'Магазин': ["http://127.0.0.1:8000/games/"],
        'Корзина': ["http://127.0.0.1:8000/cart/"]}
context = {'base_name': 'Домашнее задание по теме "DTL. Теги, наследование."',
           'base_tsul': 'Цель: освоить синтаксис и инструменты DTL (Языка динамических шаблонов) на практике.',
           'base_task': 'Задача "Сила DTL":',
           'base_time': 'Дата: 07.12.2024г.',
           'base_student': 'Крылов Эдуард Васильевич',
           }


# Create your views here.
def get_menu(request):
    context['base_title'] = 'Главная'
    context['menu'] = menu
    return render(request, 'fourth_task/menu.html', context)


def games(request):
    context['base_title'] = 'Игры'
    context['menu'] = menu
    content = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2'],
               'programs': ['Microsoft Office', 'Windows 10 Pro']
               }
    context['content'] = content
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    context['base_title'] = 'Корзина'
    context['base_cart'] = 'Извините, ваша корзина пуста'
    context['menu'] = menu
    return render(request, 'fourth_task/cart.html', context)
