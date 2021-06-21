from django.contrib import admin
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _

from .models import Bb, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)


class RubricAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_ads')

    # @admin.display(description=_('Количество объявлений'))
    # def number_of_ads(self, obj):
    #     return Rubric.objects.annotate(number_of_bbs=Count('bb')).order_by('pk')[obj.pk - 1].number_of_bbs


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
