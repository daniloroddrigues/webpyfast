from django.test import TestCase
from webpyfast.blogs.models import Post, Category


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.obj = Post.objects.create(
            title='Titulo do post',
            slug='titulo-do-post',
            image='url/da/imagem',
            description='Descrição do post',
        )

        p1 = Post.objects.create(title='Titulo do post', slug='titulo-do-post', image='url/da/imagem',
                                 description='Descrição do post')

        p2 = Post.objects.create(title='Titulo do post', slug='titulo-do-post', image='url/da/imagem',
                                 description='Descrição do post')

        c1 = Category.objects.create(title='Titulo da categoria',
                                     slug='titulo-da-categoria')

        t1 = Tags.objects.create(title='Titulo da tag',
                                 slug='titulo-da-tag')

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

    def test_context_category(self):
        """Deve ter o contexto categoria"""
        category = self.resp.context['categories']
        self.assertIsInstance(category, Category)

    def test_get_absolute_url(self):
        """Deve conter a url /blog/1/titulo-do-post/"""
        url = '/blog/{}/{}/'.format(self.obj.pk, self.obj.slug)
        self.assertEqual(url, self.obj.get_absolute_url())
