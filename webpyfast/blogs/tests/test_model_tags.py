from django.test import TestCase

from webpyfast.blogs.models import Tags


class TagsTest(TestCase):
    def setUp(self):
        self.obj = Tags.objects.create(
            title='Titulo da categoria',
            slug='titulo-da-categoria',
        )
        self.obj.save()

    def test_create(self):
        """Deve existir o objeto Tags"""
        self.assertTrue(Tags.objects.exists())

    def test_str(self):
        """Deve retornar o titulo da categoria"""
        self.assertEqual('Titulo da categoria', str(self.obj.title))

