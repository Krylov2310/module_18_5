from django.shortcuts import render
from django.views.generic import TemplateView

context = {'base_name': 'Модуль 18. Django. Представления и Шаблоны',
           'base_student': 'Студент: Крылов Эдуард Васильевич',
           'base_title': 'Навигационная страница'
           }


# Create your views here.
def info(request):
    return render(request, 'info/info.html', context)
