from django.db.models import QuerySet
from django.test import TestCase


class BlogViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/blog/')

    def test_get(self):
        """Deve retornar status code 200 para url /blog/"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Deve usar o template blog/blog.html"""
        self.assertTemplateUsed(self.resp, 'blog/post.html')

    def test_html(self):
        """Deve conter sidebar e category list"""
        contains = (
            ('class="sidebar"', 1),
            ('class="category"', 1),
        )
        with self.subTest():
            for contain, index in contains:
                self.assertContains(self.resp, contain, index)

    def test_context(self):
        """Deve ter o context blog"""
        posts = self.resp.context['posts']
        self.assertIsInstance(posts, QuerySet)
