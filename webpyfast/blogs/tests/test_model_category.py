from django.test import TestCase

from webpyfast.blogs.models import Category


class CategoryModelTest(TestCase):
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
