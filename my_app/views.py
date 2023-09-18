from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.





def index(request):
    return render(request, "index.html")

class upload_files(View):
    def post(self, request):
        File = request.FILES['File']
        return HttpResponse({"data": "hello world.","111":""})
    # def pdf(self, request):

    def get(self, request, format=None):
        """
        提供get请求
        :param request:
        :param format:
        :return:
        """
        return HttpResponse({"data":"hello world."})


