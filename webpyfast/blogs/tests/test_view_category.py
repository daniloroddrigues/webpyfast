from django.test import TestCase
from webpyfast.blogs.models import Category


class CategoryViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/category/javascript/')

    def test_get(self):
        """Deve retornar status code 200 para a url /category/javascript/"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Deve usar o template blog/category.html"""
        self.assertTemplateUsed(self.resp, 'blog/category.html')

    def test_context(self):
        """Deve ter o contexto"""
        categories = self.resp.context['categories']
        self.assertIsInstance(categories, Category)
