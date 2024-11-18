from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import URL
from urllib.parse import urlparse
from collections import Counter

import json

@csrf_exempt
def shorten_url(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        new_url = json.loads(request.body).get("url")
        print("new_url", new_url)
        obj, _ = URL.objects.get_or_create(url=new_url)
        return JsonResponse({"shortened_url": f"/{obj.shortcode}"})

def redirect_to_original(request: HttpRequest, path: str) -> HttpResponseRedirect:
    qs = URL.objects.filter(shortcode__iexact=path)
    if qs.count() != 1 and not qs.exists():
        raise Http404
    obj = qs.first()
    return HttpResponseRedirect(obj.url)

def get_metrics(request: HttpRequest) -> JsonResponse:
    objs = URL.objects.all()
    domain_counter = Counter(urlparse(obj.url).netloc for obj in objs)
    top_domains = domain_counter.most_common(3)
    return JsonResponse(dict(top_domains))
