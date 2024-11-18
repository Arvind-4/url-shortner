from collections import Counter
from rest_framework import status
from urllib.parse import urlparse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect

from shortner.models import URL
from shortner.serializers import URLSerializer


class ShortenURLView(APIView):
    serializer_class = URLSerializer
    def post(self, request: Request):
        serializer = URLSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_url = serializer.validated_data["url"]
        obj, _ = URL.objects.get_or_create(url=new_url)
        return Response({"shortened_url": f"/{obj.shortcode}"}, status=status.HTTP_201_CREATED)


class RedirectToOriginalView(APIView):
    serializer_class = None
    def get(self, request: Request, path: str):
        obj = get_object_or_404(URL, shortcode=path)
        return redirect(obj.url)


class MetricsView(APIView):
    serializer_class = None
    def get(self, request: Request):
        objs = URL.objects.all()
        domain_counter = Counter(urlparse(obj.url).netloc for obj in objs)
        top_domains = domain_counter.most_common(3)
        return Response(dict(top_domains), status=status.HTTP_200_OK)
