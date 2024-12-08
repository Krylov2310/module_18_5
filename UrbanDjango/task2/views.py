from django.shortcuts import render
from django.views.generic import TemplateView

context = {'base_name': 'Домашнее задание по теме "Urls и Views. Функциональное и классовое представление."',
           'base_tsul': 'Цель: закрепить знания о маршрутах (urls) и представлениях (views) в Django.',
           'base_task': 'Задача "Первый проект":',
           'base_time': 'Дата: 07.12.2024г.',
           'base_student': 'Крылов Эдуард Васильевич'
           }


# Create your views here.
def index(request):
    return render(request, 'second_task/index.html',context)


class index2(TemplateView):
    template_name = 'second_task/index2.html'
