"""Django Admin configuration for App itservices

Author: Melanie Desaive
Copyrigh (c) 2016, Melanie Desaive
All rights reserved.

Licensed under the GNU General Public License.
See: COPYING.txt in project root.
"""

from django.contrib import admin

# Register your models here.
from itservices.models import Distribution
from itservices.models import Group
from itservices.models import ITService
from itservices.models import Type


class ITServiceInline(admin.TabularInline):
    model = ITService
    # exclude = []
    extra = 1


class ITServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['name', 'short', 'description', 'group', 'its_type',
                     'distribution', 'distribution_note']}),
    ]
    list_display = ('name', 'short', 'description',
                    'group', 'its_type', 'distribution')
    list_filter = ('group', 'its_type', 'distribution')
    ordering = ('group', 'name')
    # inlines = [<systems>, <staff>]
    search_fields = ('name',)


admin.site.register(Distribution)
admin.site.register(Group)
admin.site.register(ITService, ITServiceAdmin)
admin.site.register(Type)
