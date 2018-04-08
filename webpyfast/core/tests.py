from django.db.models import QuerySet
from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """Deve retorna status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Deve retornar o template """
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_html(self):
        """Deve conter na home esses html, """
        contains = (
            ('id="company"', 1),
            ('id="services"', 1),
            ('id="clients"', 1),
            ('id="blog"', 1),
            ('id="contact"', 1),
        )

        with self.subTest():
            for contain, index in contains:
                self.assertContains(self.resp, contain, index)

    def test_context(self):
        """Deve conter o contexto post"""
        posts = self.resp.context['posts']
        self.assertIsInstance(posts, QuerySet)
