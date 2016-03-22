"""Django Admin configuration for App systems.

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
# from django.contrib.contenttypes.admin import GenericTabularInline

# To use genericadmin
from genericadmin.admin import GenericAdminModelAdmin
from genericadmin.admin import TabularInlineWithGeneric
from genericadmin.admin import GenericTabularInline

from itservices.systems.models import Landspace
from itservices.systems.models import VirtualizationTechnology
from itservices.systems.models import HostInstance
from itservices.systems.models import Computer
from itservices.systems.models import Cluster
from itservices.systems.models import ComputerRole
from itservices.systems.models import ClusterMapComputer
from itservices.systems.models import ClusterTechnology
from itservices.systems.models import Container
from itservices.systems.models import VM
from itservices.systems.models import ImportSystemsAggregated


class ClusterMapComputerInline(admin.TabularInline):
    model = ClusterMapComputer
    extra = 1


class ClusterMapComputerAdmin(admin.ModelAdmin):
    list_display = ('computer', 'cluster', 'role')


# class ComputerAdmin(admin.ModelAdmin):
#     pass
# fieldsets = [
# (None, {'fields': ['system', 'type']}),
# ('Details', {'fields': ['system_description', 'system_note']}),
# ('Mapping', {'fields': ['area', 'new_area', 'landspace']})
# ('Details', {'fields': ['system_description', 'system_note'], 'classes': ['collapse']}),
# ('Mapping', {'fields': ['area', 'landspace'], 'classes': ['collapse']})
# ]
#     inlines = (HostMapComputerInline, )
# fields = ['system', 'type_id', 'system_description', 'system_note', 'area_id', 'landspace_id']
# list_display = ('system', 'new_area', 'area', 'type', 'landspace')
# list_filter = ('area', 'type', 'landspace')
# search_fields = ['system']
# ordering = ('new_area', 'area', 'system')


class ContainerInline(GenericTabularInline):
    model = Container
    extra = 1
    exclude = ('note', )

    ct_field='host_type'
    fk_field='host_id'
    ct_fk_field='host_id'


class VMInline(GenericTabularInline):
    model = VM
    extra = 1
    exclude = ('note', )

    ct_field='host_type'
    fk_field='host_id'
    ct_fk_field='host_id'


class ImportSystemsAggregatedInline(GenericTabularInline):
    model = ImportSystemsAggregated
    extra = 1
    exclude = ('note', )

    ct_field='host_type'
    fk_field='host_id'
    ct_fk_field='host_id'


class ComputerAdmin(admin.ModelAdmin):
    fieldsets = [(
        None, {
            'fields': ['name', 'description', 'note', 'itservice', 'landspace']}),
    ]
    inlines = (ContainerInline, VMInline, ImportSystemsAggregatedInline)
    list_display = ('name', 'description', 'itservice', 'landspace')


class ClusterAdmin(admin.ModelAdmin):
    fieldsets = [(
        None, {
            'fields': ['name', 'cluster_technology', 'description', 'note', 'itservice', 'landspace']}),
    ]
    inlines = (ClusterMapComputerInline, ContainerInline, VMInline, ImportSystemsAggregatedInline)
    list_display = ('name', 'cluster_technology',
                    'description', 'itservice', 'landspace')


class HostInstanceAdmin(admin.ModelAdmin):
    pass
    # fieldsets = [(None, {'fields': ['name', 'virtualization_technology', 'description', 'note', 'itservice', 'landspace']}),
    # ]
    # list_display = ('name', 'virtualization_technology', 'description',
    # 'note', 'itservice', 'landspace')


class VirtualizationTechnologyAdmin(admin.ModelAdmin):
    inlines = (ContainerInline, VMInline)


class ImportSystemsAggregatedAdmin(GenericAdminModelAdmin):
    list_display = ('name', 'check1', 'check2', 'itservice', 'group', 'landspace', 'tag1', 'tag2', 'tag3')
    generic_fk_fields = [{
        'ct_field': 'host_type',
        'fk_field': 'host_id',
        }]
    content_type_whitelist = ('computer', 'cluster')


class VMAdmin(GenericAdminModelAdmin):
    generic_fk_fields = [{
        'ct_field': 'host_type',
        'fk_field': 'host_id',
        }]


class ContainerAdmin(GenericAdminModelAdmin):
    pass


admin.site.register(Landspace)
admin.site.register(VirtualizationTechnology, VirtualizationTechnologyAdmin)
admin.site.register(HostInstance, HostInstanceAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Cluster, ClusterAdmin)
admin.site.register(ComputerRole)
admin.site.register(ClusterTechnology)
admin.site.register(ClusterMapComputer)
admin.site.register(Container, ContainerAdmin)
admin.site.register(VM, VMAdmin)
admin.site.register(ImportSystemsAggregated, ImportSystemsAggregatedAdmin)
