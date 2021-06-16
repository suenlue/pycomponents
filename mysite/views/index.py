from django.shortcuts import render

def index(request):
    context = {
      'msg': "index page"
      }
    return render(request, 'test-component/index.html', context)