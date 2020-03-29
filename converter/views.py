import os
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LinkForm
from .models import Link
from django.conf import settings
from .tasks import convert
from django.http import HttpResponse, response


def index(request):

    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            email = form.cleaned_data.get('email')
            link = request.get_host()
            convert.delay(url, email, link)
            messages.success(request, 'Ссылка на скачивание отправлена на почту!')
    else:
        form = LinkForm()

    return render(request, 'index.html', locals())









