from django.shortcuts import render, Http404, HttpResponse, redirect
from .models import Director, Movie, Review
from movies.forms import CreateMoviesForm


# def movie1(request):
#     dict_ = {
#         'movie': 'Movie',
#     }
#     return render(request, 'movie.html', context=dict_)

def movie_list_view(request):
    movie_list = Movie.objects.order_by('-created_at')
    context = {
        'movie': movie_list
    }
    return render(request, 'movie.html', context=context)

def movie_detail_view(request, id):
    try:
        movie_detail = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        raise Http404('ID ФИЛЬМОВ НАЧИНАЮТСЯ С 2!!')
    review = Review.objects.filter(movie_id=id)
    return render(request, 'movie_detail_view.html', context={
        'detail': movie_detail,
        'review': review
    })

def create_movies_view(request):
    form = CreateMoviesForm()
    if request.method == 'POST':
        form = CreateMoviesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/movies')
    return render(request, 'add_movies.html', context={
        'form': form
    })