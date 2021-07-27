from django.shortcuts import render
from django.http import HttpResponse
from .models import BooksDetails

# Create your views here.
def index(request):
    return render(request,'books/index.html')


def StoreDetails(request):

    s=BooksDetails()
    s.book_name=request.POST.get('name')
    s.book_writer=request.POST.get('writer')
    s.book_price=request.POST.get('price')
    s.book_imgs = request.POST.get('avatar')
    dis=int(s.book_price)
    if (dis>=5000):
        s.book_discount=15;
    elif (dis>=3000):
        s.book_discount=10;
    else:
        s.book_discount=0;
    s.save()
    return HttpResponse("successfully saved data")

def ShowBooks(request):
    stu=BooksDetails.objects.all()
    params={"students":stu}
    return render(request,'books/showBooks.html',params)