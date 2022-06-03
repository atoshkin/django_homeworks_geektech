from django.contrib import admin
from .models import Director, Movie, Review

class CommentInline(admin.StackedInline):
    model = Movie
    extra = 5


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'descriptions', 'created_at', 'updated_at')
    search_fields = 'title', 'descriptions'.split()
    list_filter = 'created_at'.split()
    inlines = [CommentInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)



admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)