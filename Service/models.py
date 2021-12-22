import calendar

from django.db import models
from django.utils import timezone


def get_month(month_int):
    if month_int == 1:
        return 'Jan'
    elif month_int == 2:
        return 'Feb'
    elif month_int == 3:
        return 'Mar'
    elif month_int == 4:
        return 'Apr'
    elif month_int == 5:
        return 'May'
    elif month_int == 6:
        return 'Jun'
    elif month_int == 7:
        return 'Jul'
    elif month_int == 8:
        return 'Aug'
    elif month_int == 9:
        return 'Sep'
    elif month_int == 10:
        return 'Oct'
    elif month_int == 11:
        return 'Nov'
    elif month_int == 12:
        return 'Dec'


class Article(models.Model):
    topic = models.CharField(max_length=50)
    article = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/', null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.topic

    def recently_posted(self):
        return (timezone.now() - self.date) < timezone.timedelta(days=1)

    def outdated_post(self):
        return (timezone.now() - self.date) > timezone.timedelta(weeks=4)

    def duration_of_article_publication(self):
        return timezone.now() - self.date
