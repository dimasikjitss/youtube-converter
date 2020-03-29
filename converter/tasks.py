
import youtube_dl
from django.core.mail import send_mail
from main.celery import app
from django.conf import settings
from .models import Link
from transliterate import translit



@app.task
def convert(url, email, link):
    
    DOWNLOAD_OPTIONS_MP3 = {

        'format': 'bestaudio/best',
        'outtmpl': 'media/%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],

    }
    with youtube_dl.YoutubeDL(DOWNLOAD_OPTIONS_MP3) as dl:
        result = dl.extract_info(url)
        filename = result['title']
        # new_filename = translit(filename, 'ru', reversed=True)
       

    download_link = 'http://' + link + '/media/' + filename.replace(' ', '%20').replace(' - ', '%20').replace(' | ', '%20') + '.mp3'
    send_mail('Ссылка на скачивание файла', download_link, settings.EMAIL_HOST_USER, [email], fail_silently=True,)