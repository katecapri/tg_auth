import os
from django.shortcuts import render
from secrets import token_urlsafe

def index(request):
    token = token_urlsafe(16)
    context = {
        "tg_link": f'{os.getenv("TG_BOT_URL")}?start={token}',
        "link_text": "Войти через Telegram",
        "token": token,
    }
    return render(request, 'index.html', context=context)