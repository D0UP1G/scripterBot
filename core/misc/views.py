from django.shortcuts import render
from django.views import View
from .form import *


class PushMail(View):
    def get(self, request):
        return render(request, 'index.html', {'form':postcardForm})