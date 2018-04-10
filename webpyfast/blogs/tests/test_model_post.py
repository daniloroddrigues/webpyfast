from datetime import datetime

from django.test import TestCase

from webpyfast.blogs.models import Post


class PostModelTest(TestCase):
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

    def test_tags_blank(self):
        """Deve conter o campo em branco em tags"""
        field = Post._meta.get_field('tags')
        self.assertTrue(field.blank)

    def test_categories_blank(self):
        """Deve conter o campo em branco em categorias"""
        field = Post._meta.get_field('categories')
        self.assertTrue(field.blank)
