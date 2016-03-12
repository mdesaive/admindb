"""Django Admin configuration for App itservices

Author: Melanie Desaive, desaive@gmx.de
Copyrigh (c) 2016, Melanie Desaive
All rights reserved.

Licensed under the GNU General Public License.
See: COPYING.txt in project root.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
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
