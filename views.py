from django.http import HttpResponse

def home(requests):
    return HttpResponse('<h1>Home Page</h1>')

def about(requests):
    return HttpResponse('<h1>About Us</h1>')

def contact(requests):
   from  return HttpResponse('<h1>Contact page</h1>
