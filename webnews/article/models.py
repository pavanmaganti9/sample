from django.db import models
from django.utils.crypto import get_random_string


def new_file_name(instance, filename):
    return 'images/{0}{1}'.format(get_random_string(length=10), filename)


class Reporter(models.Model):
    name = models.CharField(max_length=20)

    def n_articles(self):
        return self.all_articles.count()

    def __str__(self):
        return self.name


class Article(models.Model):
    heading = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to=new_file_name,
                              blank=True,
                              null=True)

    reporter = models.ForeignKey(Reporter,
                                 related_name='all_articles',
                                 null=True,
                                 blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading + ' ' + str(self.created)

# Create your models here.
