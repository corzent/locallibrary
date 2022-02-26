from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

from django.views import generic


def index(request):
    """
    Функция отображается для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_books_available = Book.objects.filter(title__icontains='s').count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.
    num_genres = Genre.objects.count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # Переменной контекста context
    return render(
        request,
        'catalog/index.html',
        context={'num_books': num_books,
                 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_authors': num_authors,
                 'num_genres': num_genres,
                 'num_books_available': num_books_available},
    )


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author

