from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Director, Movie, Review

def test(request):
    return HttpResponse('<h1 style="color:red;">Hello World!</h1>')


def test1(request):
    dict_ = {
        'title': 'Blog APPLICATION',
        'text': 'HELLO WORLD!',
        'date': ''
    }
    return render(request, 'movue.html', context=dict_)

def movie_list_view(request):
    movie_list = Movie.objects.all()
    context = {
        'movie': movie_list
    }
    return render(request, 'movie_list.html', context=context)

def movie_detail_view(request, id):
    try:
        Movie_detail = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        raise Http404('movie not FOUND!!!')
    return render(request, 'movie_detail.html', context={
        'detail': Movie_detail
    })
