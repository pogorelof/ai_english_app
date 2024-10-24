from django.shortcuts import render
from django.db.models import Count
from random import randint
from words.models import Word
from django.http import JsonResponse
from . import utils


def get_random_word(request):
    words_count = Word.objects.filter(archive=False).count()
    random_index = randint(0, words_count-1)
    word = Word.objects.filter(archive=False)[random_index]
    return JsonResponse({'word':word.word, 'context':word.context})

def memorization(request):
    return render(request, 'games/memorization.html')

def check_word(request):
    word = request.GET.get('word')
    translate = request.GET.get('translate')
    response = utils.check_translate_ai(word, translate)
    if response['result']:
        word_obj = Word.objects.get(word=word)
        word_obj.guessed += 1
        word_obj.translation_to_ru = response['translate'].capitalize()
        if word_obj.guessed == 3:
            word_obj.archive = True
        word_obj.save()
    else:
        word_obj = Word.objects.get(word=word)
        word_obj.wrong += 1
        word_obj.save()
    return JsonResponse(response)