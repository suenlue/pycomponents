from django.shortcuts import render

def test(request):
    context = {
      'msg': "test page"
      }
    return render(request, 'test-component/index.html', context)