from datetime import datetime

from django.db.models import QuerySet
from django.test import TestCase
from webpyfast.blogs.models import Post, Category


class BlogTest(TestCase):
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


class BlogModelTest(TestCase):
    def setUp(self):
        self.obj = Post(
            title='Titulo do Post',
            slug='titulo-do-post',
            image='blogs/images',
            description='Descrição do blog',
        )
        self.obj.save()

    def test_create(self):
        """Deve criar o objeto Blog"""
        self.assertTrue(Post.objects.exists())

    def test_created_at(self):
        """Deve conter o campo created_at - criado em"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_updated_at(self):
        """Deve conter o campo updated_at - atualizado em"""
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_image_field_blank(self):
        """Deve conter Black True para field Imagem"""
        field = Post._meta.get_field('image')
        self.assertTrue(field.blank)

    def test_image_field_null(self):
        """Deve setar True para o campo null de imagem"""
        field = Post._meta.get_field('image')
        self.assertTrue(field.null)

    def test_str(self):
        """Deve retornar o titulo do post no django admin"""
        self.assertEqual('Titulo do Post', str(self.obj))


class CategoryTest(TestCase):
    def setUp(self):
        self.obj = Category(
            title='Título da Categoria',
            slug='titulo-da-categoria'
        )
        self.obj.save()

    def test_create(self):
        """Deve existir o obj categoria"""
        self.assertTrue(Category.objects.exists())

    def test_str(self):
        """Deve conter o Título da Categoria"""
        self.assertEqual('Título da Categoria', str(self.obj))
