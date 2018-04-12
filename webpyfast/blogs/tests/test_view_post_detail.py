from django.db.models import QuerySet
from django.test import TestCase

from webpyfast.blogs.models import Post, Category, Tags


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.obj = Post.objects.create(
            title='Titulo do post',
            slug='titulo-do-post',
            image='url/da/imagem',
            description='Descrição do post',
        )

        post = Post.objects.create(
            title='Titulo do post',
            slug='titulo-do-post',
            image='url/da/imagem',
            description='Descrição do post'
        )

        cat = Category.objects.create(
            title='Titulo da categoria',
            slug='titulo-da-categoria'
        )

        tag = Tags.objects.create(
            title='Titulo da tag',
            slug='titulo-da-tag'
        )

        post.categories.add(cat)
        post.tags.add(tag)

        self.resp = self.client.get('/blog/{}/{}/'.format(self.obj.pk, self.obj.slug))

    def test_get(self):
        """Deve retornar status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Deve conter o template blog/post_detail.html"""
        self.assertTemplateUsed(self.resp, 'blog/post_detail.html')

    def test_context(self):
        """Deve conter o contexto post detail"""
        post_detail = self.resp.context['post_detail']
        self.assertIsInstance(post_detail, Post)

    def test_context_categories(self):
        """Deve ter o contexto categorias"""
        categories = self.resp.context['categories']
        self.assertIsInstance(categories, QuerySet)

    def test_context_tags(self):
        """Deve conter o contexto tags"""
        tags = self.resp.context['tags']
        self.assertIsInstance(tags, QuerySet)

    def test_get_absolute_url(self):
        """Deve conter a url /blog/1/titulo-do-post/"""
        url = '/blog/{}/{}/'.format(self.obj.pk, self.obj.slug)
        self.assertEqual(url, self.obj.get_absolute_url())
