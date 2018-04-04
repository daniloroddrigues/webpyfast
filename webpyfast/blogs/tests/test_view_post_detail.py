from django.test import TestCase


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/blog/url-do-post/')

    def test_get(self):
        """Deve retornar status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Deve conter o template blog/post_detail.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_detail.html')
