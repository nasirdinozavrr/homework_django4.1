from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from . import models, forms

def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})

def book_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book': book})

def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Book created')
    else:
        form = forms.BookForm()
    return render(request, 'add_books.html', {"form": form})

def book_update(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    if request.method == "POST":
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('book: book_all'))
    else:
        form = forms.BookForm(instance=book_object)
    return render(request, 'book_update.html', {'form': form, 'object': book_object})

def book_delete(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    book_object.delete()
    return HttpResponse("Book Deleted")


def book_rate(request, id):
    form = models.Rating.objects.all, id=id
    if request.method == "POST":
        form.save()
    return render(request, 'book_detail.html', {'form': form})

