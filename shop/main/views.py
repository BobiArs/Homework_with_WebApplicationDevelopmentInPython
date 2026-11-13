import datetime as dt
from .services import UserService
from django.core.checks import registry
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

from .models import Card

cards = [
        {
            'image': 'django.jpg',
            'title': 'Розділ 1',
            'text': 'Some quick example text to build on the card title and make up the bulk of the card’s content.',
            'btn_text': 'Go somewhere'
        },
        {
            'image': 'c++.png',
            'title': 'Розділ 2',
            'text': 'Тут можна розмістити новини або корисну інформацію.',
            'btn_text': 'Переглянути'
        },
        {
            'image': 'ue58.jpg',
            'title': 'Розділ 3',
            'text': 'Тут можна розмістити додаткові матеріали',
            'btn_text': 'Переглянути'
        }
    ]

#http://127.0.0.1:8000
def home(request):
    #return HttpResponse("Hello World")
    return render(request, 'main/index.html', {'cards':cards})

# параметри url/id   url/title   rozetka.ua/tv
# query params       rozetka.ua?title=tv&start_price=3400&end_price=10000

def get_card(request, id):
    title = request.GET.get('title', f'Card {id}')

    if 0 < id <= len(cards):
        return render(request, 'main/card.html', {
            'card': cards[id - 1],
            'title': title
        })

    else:
        return HttpResponse("Not Found", status=404)


def get_card_by_title(request):
    title = None
    if request.method=='GET' and  request.GET.get('title'):
        title = request.GET.get('title')

    elif request.method=='POST':
        title = request.POST.get('title')

    if title is not None:
        return JsonResponse({'title': title})

    else:
        return HttpResponse("Not Found")

def about(request):
    # return HttpResponse("About Page")
    text = "Це сторінка про Нас"
    frameworks = ['django', 'flask', 'last api']
    return render(request, 'main/about.html', {'text': text, 'frameworks': frameworks, "cards": cards})

def create_card(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        #TODO:image.name поміняти при збережені (add datetime, uuid)
        #TODO:перевірити чи дійсно це малюнок за ext і розмір
        # print(image.name, image.size)
        # print(title,description,image)
        card = Card(
            title=title,
            description=description,
            image=image,
            created_at=dt.datetime.now(),
            )
        card.save()

    return JsonResponse({'message':'ok'})

def register(request):
    if request.method == 'POST':
        try:
            user = UserService.register_user(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                password=request.POST.get('password'),
                birth_date=request.POST.get('birth_date'),
                avatar=request.FILES.get('avatar')
            )

            return JsonResponse({'message':'ok', 'user_id': user.id}, status=200)

        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)

        except Exception as e:
            return JsonResponse({'error': 'Помилка при реєстрації'}, status=500)

    return render(request, 'main/register.html')