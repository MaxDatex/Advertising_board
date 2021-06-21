from django.contrib import admin
from django.db import models
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name=_('Название'))

    class Meta:
        verbose_name = _('Рубрика')
        verbose_name_plural = _('Рубрики')
        ordering = ('name',)

    def __str__(self):
        return self.name

    # TODO: Dodelat'
    @admin.display(description=_('Количество объявлений'))
    def number_of_ads(self):
        return Rubric.objects.annotate(number_of_bbs=Count('bb')).order_by('pk')[self.pk-1].number_of_bbs


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Товар'))
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name=_('Рубрика'))
    content = models.TextField(null=True, blank=True, verbose_name=_('Описание'))
    price = models.FloatField(null=True, blank=True, verbose_name=_('Цена'))
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_('Опубликовано'))

    class Meta:
        verbose_name = _('Объявление')
        verbose_name_plural = _('Объявления')
        ordering = ('-published',)

    def __str__(self):
        return self.title
