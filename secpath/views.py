import json
import logging

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from datetime import datetime, timedelta

from secpath.models import Entry
from secpath.utils import random_string

logger = logging.getLogger("OTEL")


def link(request, rand=None):
    entry = get_object_or_404(Entry, link=(request.scheme + "://" + request.META.get('HTTP_HOST') + "/secpath/d/" + rand))
    return render(request, 'link.html', {"message": entry.data, "expires": entry.expire})
    

def main(request):
    response = HttpResponse()
    logger.warning("Got request")
    match request.method:
        case "POST":
            body_json = json.loads(request.body)
            now = datetime.now()
            entry = Entry(
                data=body_json.get('text'),
                expire=(now + timedelta(minutes=int(body_json.get('expiration')))),
                link = request.scheme + "://" + request.META.get('HTTP_HOST') + "/secpath/d/" + random_string(20)
                )
            entry.save()
            response.content = json.dumps({"message": "Accepted", "share_url": entry.link})
        case "GET":
            response = render(request,'main.html')
        case _:
            response.status_code = 400
    return response