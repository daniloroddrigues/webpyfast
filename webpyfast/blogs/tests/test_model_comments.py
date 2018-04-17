from django.test import TestCase
from webpyfast.blogs.models import Comments


class CommentsModelTest(TestCase):
    def setUp(self):
        self.obj = Comments.objects.create(
            name='Nome do Comentarista',
            email='nomedocomentarista@email.com',
            comment='Comentário do comentarista'
        )
        self.obj.save()

    def test_create(self):
        """Deve criar objeto comentário"""
        self.assertTrue(Comments.objects.exists())

    def test_str(self):
        """Deve retornar"""
        self.assertEqual('Nome do Comentarista', str(self.obj))
