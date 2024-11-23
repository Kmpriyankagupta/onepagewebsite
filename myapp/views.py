from django.shortcuts import render
from django.db.models import Q
from .models import *

def index(request):
      books = Book.objects.filter(Q(published_date__year=2023)|Q(published_date__year=2021))

      print('jhvbjdf',books)

      
      authors = Author.objects.all()

      context = {
            'authors': authors
        }

      return render(request, 'app/index.html', context)

def author(request):

      if request.method == 'POST':
            name = request.POST.get('name')  
            email = request.POST.get('price')  
            # date = request.POST.get('date')
            cloths.objects.create(name=name, price=email)
            print('name', name)

      return render(request,'myapp/author.html')

