from datetime import datetime

from django.db.models import QuerySet
from django.test import TestCase
from webpyfast.blogs.models import Blog


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
        contains = (
            ('class="sidebar"', 1),
            ('class="category"', 1),
        )
        with self.subTest():
            for contain, index in contains:
                self.assertContains(self.resp, contain, index)

    def test_context(self):
        """Deve ter o context blog"""
        blogs = self.resp.context['blogs']
        self.assertIsInstance(blogs, QuerySet)


class BlogModelTest(TestCase):
    def setUp(self):
        self.obj = Blog(
            title='Titulo do Post',
            slug='titulo-do-post',
            image='url/to/image',
            description='Descrição do blog',
        )
        self.obj.save()

    def test_create(self):
        """Deve criar o objeto Blog"""
        self.assertTrue(Blog.objects.exists())

    def test_created_at(self):
        """Deve conter o campo created_at - criado em"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_updated_at(self):
        """Deve conter o campo updated_at - atualizado em"""
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_image_field_blank(self):
        """Deve conter Black True para field Imagem"""
        field = Blog._meta.get_field('image')
        self.assertTrue(field.blank)

    def test_image_field_null(self):
        """Deve setar True para o campo null de imagem"""
        field = Blog._meta.get_field('image')
        self.assertTrue(field.null)

    def test_str(self):
        """Deve retornar o titulo do post no django admin"""
        self.assertEqual('Titulo do Post', str(self.obj))
