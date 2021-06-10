from django.shortcuts import render

def index(request):
    context = {
      'msg': "hallo welt"
      }
    return render(request, 'test-component/index.html', context)