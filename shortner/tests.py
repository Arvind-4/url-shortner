from django.test import TestCase, Client
from django.urls import reverse
from .models import URL
from urllib.parse import urlparse
import json

class ShortenerViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_url = "http://example.com"
        self.invalid_url = "invalid-url"
        self.short_url_endpoint = reverse("shorten_url")
        self.metrics_endpoint = reverse("get_metrics")

    def test_shorten_url_valid(self):
        """Test shortening a valid URL."""
        response = self.client.post(self.short_url_endpoint, json.dumps({"url": self.valid_url}), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("shortened_url", data)
        self.assertTrue(URL.objects.filter(url=self.valid_url).exists())

    def test_redirect_to_original(self):
        """Test redirection to the original URL."""
        obj = URL.objects.create(url=self.valid_url, shortcode="abc123")
        response = self.client.get(f"/{obj.shortcode}/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.valid_url)

    def test_redirect_to_original_not_found(self):
        """Test redirection for a non-existent shortcode."""
        response = self.client.get("/nonexistent/")
        self.assertEqual(response.status_code, 404)

    def test_get_metrics(self):
        """Test retrieving metrics for top domains."""
        URL.objects.create(url="http://example.com", shortcode="abc123")
        URL.objects.create(url="http://test.com", shortcode="xyz789")
        URL.objects.create(url="http://example.com/page", shortcode="def456")
        response = self.client.get(self.metrics_endpoint)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("example.com", data)
        self.assertIn("test.com", data)
