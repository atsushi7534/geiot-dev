from django.shortcuts import render
# Create your views here.

def index(request):
  return render(request, 'geiot/index.html')

def result(request):
  return render(request, 'geiot/result.html')

def select(request):
  return render(request, 'geiot/select.html')

def test(request):
  return render(request, 'geiot/test.html')
