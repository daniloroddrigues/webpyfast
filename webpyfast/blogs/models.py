from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(
        'Imagem',
        upload_to='blogs/iamges',
        blank=True,
        null=True,
    )
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
