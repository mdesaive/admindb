"""Django Admin configuration for App systems.

Author: Melanie Desaive
Copyrigh (c) 2016, Melanie Desaive
All rights reserved.

Licensed under the GNU General Public License.
See: COPYING.txt in project root.
"""

from django.contrib import admin

from itservices.systems.models import Landspace
from itservices.systems.models import VirtualizationTechnology
from itservices.systems.models import HostPlug
from itservices.systems.models import HostInstance
from itservices.systems.models import Computer
from itservices.systems.models import Cluster
from itservices.systems.models import ComputerRole
from itservices.systems.models import ClusterMapComputer
from itservices.systems.models import ClusterTechnology
from itservices.systems.models import Container
from itservices.systems.models import VM


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


class ComputerAdmin(admin.ModelAdmin):
    fieldsets = [(
        None, {
            'fields': ['name', 'description', 'note', 'itservice', 'landspace']}),
    ]
    list_display = ('name', 'description', 'itservice', 'landspace')


class ComputerInline(admin.TabularInline):
    model = Computer
    extra = 1
    exclude = ('note',)


class ClusterAdmin(admin.ModelAdmin):
    fieldsets = [(
        None, {
            'fields': ['name', 'cluster_technology', 'description', 'note', 'itservice', 'landspace']}),
    ]
    inlines = (ClusterMapComputerInline, )
    list_display = ('name', 'cluster_technology',
                    'description', 'itservice', 'landspace')


class ClusterInline(admin.TabularInline):
    model = Cluster
    extra = 1
    exclude = ('note',)


class HostInstanceAdmin(admin.ModelAdmin):
    pass
    # fieldsets = [(None, {'fields': ['name', 'virtualization_technology', 'description', 'note', 'itservice', 'landspace']}),
    # ]
    # list_display = ('name', 'virtualization_technology', 'description',
    # 'note', 'itservice', 'landspace')


class HostPlugAdmin(admin.ModelAdmin):
    inlines = (ComputerInline, ClusterInline)


class ContainerInline(admin.TabularInline):
    model = Container
    extra = 1
    exclude = ('note', )


class VMInline(admin.TabularInline):
    model = VM
    extra = 1
    exclude = ('note', )


class VirtualizationTechnologyAdmin(admin.ModelAdmin):
    inlines = (ContainerInline, VMInline)


admin.site.register(Landspace)
admin.site.register(VirtualizationTechnology, VirtualizationTechnologyAdmin)
admin.site.register(HostPlug, HostPlugAdmin)
admin.site.register(HostInstance, HostInstanceAdmin)
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Cluster, ClusterAdmin)
admin.site.register(ComputerRole)
admin.site.register(ClusterTechnology)
admin.site.register(ClusterMapComputer)
admin.site.register(Container)
admin.site.register(VM)
