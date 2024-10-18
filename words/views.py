from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Word
from youtube_transcript_api import YouTubeTranscriptApi


class WordListView(ListView):
    model = Word
    template_name = 'words/index.html'

def add_word(request):
    word = request.POST.get('word').capitalize()
    Word.objects.create(word=word)
    return redirect('words:word_list')

def delete_word(request, pk):
    Word.objects.get(pk=pk).delete()
    return redirect('words:word_list')

def words_from_video(request):
    video_id = request.GET.get('video_id')
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    word_count = {}
    word_context = {}
    

    for t in transcript:
        full_text = t['text']
        text = full_text.replace('\n', ' ')
        text = text.split(' ')
        
        for word in text:
            if word in word_count:
                word_count[word] += 1
            else:
                if word.isalpha():
                    word = word.lower()
                    word_count[word] = 1
                    word_context[word] = full_text

    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1]))

    return render(request, 'words/words_from_yt.html', context={
        'words': sorted_word_count,
        'word_context': word_context,
    })
    
def words_from_video_handler(request):
    if request.method == 'POST':
        word = request.POST.get('word').capitalize()
        if Word.objects.filter(word=word).exists():
            return JsonResponse({'message': 'У вас уже есть это слово!', 'added': False})
        context = request.POST.get('context')
        word_obj = Word(word=word, context=context)
        word_obj.save()
        return JsonResponse({'message': 'Слово было добавлено', 'added': True})
    return JsonResponse({'message': 'This method doesn`t support'})