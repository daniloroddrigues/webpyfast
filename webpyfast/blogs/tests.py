from django.test import TestCase


class BlogTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/blog/')

    def test_get(self):
        """Deve retornar status code 200 para url /blog/"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Deve usar o template blog/blog.html"""
        self.assertTemplateUsed(self.resp, 'blog/blog.html')

    def test_html(self):
        """Deve conter sidebar e category list"""
        self.assertContains(self.resp, 'class="sidebar"', 1)
        self.assertContains(self.resp, 'class="category"', 1)

    def test_context(self):
        context = self.resp.context
