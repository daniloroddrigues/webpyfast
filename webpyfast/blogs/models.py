from django.db import models


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField('Tags', verbose_name='tags', blank=True)
    categories = models.ManyToManyField('Category', verbose_name='categorias', blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(
        'Imagem',
        upload_to='blogs/images',
        blank=True,
        null=True,
    )
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/blog/{}/{}/'.format(self.pk, self.slug)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-created_at',)


class Category(models.Model):
    title = models.CharField('título da categoria', max_length=255)
    slug = models.SlugField('slug')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


class Tags(models.Model):
    title = models.CharField('tags', max_length=255)
    slug = models.SlugField('slug')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class Comments(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'comentário'
        verbose_name_plural = 'comentários'
