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

import pdb

from django.contrib import admin

# To define custom form
from django import forms
# from django.forms import select

# from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.models import ContentTypeManager

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


class ImportSystemsAggregatedForm(forms.ModelForm):
    # Adding an extra field which enables to select the host
    # system ID and disable automatic field.
    # Maybe delete, was a test.
    extra_field = forms.ChoiceField()

    def fill_host_id_choices(self):
        """Prepares a list of choices to select host system. 
        """
        # Fill in the values in the choice field.
        choices_empty = [("None", "None")]
        # choices_computer = [((Computer, x.pk), "Computer: " + str(x)) for x in Computer.objects.all()]
        # choices_cluster = [((Cluster, x.pk), "Cluster: " + str(x)) for x in Cluster.objects.all()] 
        choices_computer = [("computer " + str(x.pk), "Computer: " + str(x)) for x in Computer.objects.all()]
        choices_cluster = [("cluster " + str(x.pk), "Cluster: " + str(x)) for x in Cluster.objects.all()] 
        self.fields['extra_field'].choices = choices_empty + choices_cluster + choices_computer

    def save_host_id_choice(self):
        """Use value from 'extra_field' to set correct host.
        """
        selected_host_str = self.cleaned_data.get('extra_field', None)

        if selected_host_str != "None":
            selected_host_a = selected_host_str.split()

            # pdb.set_trace()

            my_content_type = selected_host_a[0]
            my_content_id = selected_host_a[1]

            # ContentType.objects.get(app_label="auth", model=selected_host[0])
            # my_content_type = ContentTypeManager.get_for_models(selected_host[0])
            # my_host_type_id = my_content_type(app_label="systems", model="computer")

            self.host_id = my_content_id
            self.host_type = my_content_type
        else:
            self.host_id = "Null"
            self.host_type = "Null"

    # def save(self, *args, **kwargs):
    #     # self.save_host_id_choice()
    #     super(ImportSystemsAggregated, self).save(*args, **kwargs)
    #     # Raises error - super(type, obj): obj must be an instance or subtype of type

    def save(self):
        self.save_host_id_choice()
        print("*** save ***")
        return super(ImportSystemsAggregatedForm, self).save(commit=True)

    def save_model(self, request, obj, form, change):
        # obj.user = request.user
        print("**** Here save_model")
        self.save_host_id_choice(obj)
        
        obj.save()

    # def save(self, commit=True):
    #     # self.save_host_id_choice()
    #     return super(ImportSystemsAggregated, self).save(commit=commit)

    def __init__(self, *args, **kwargs):
        super(ImportSystemsAggregatedForm, self).__init__(*args, **kwargs)
        # Overriding to define custom form
        self.fill_host_id_choices()

    class Meta:
        model = ImportSystemsAggregated
        exclude = ('note',)


class ImportSystemsAggregatedAdmin(GenericAdminModelAdmin):
    # Uses my custom form defined above.
    form = ImportSystemsAggregatedForm

    list_display = ('name', 'check1', 'check2', 'itservice', 'group', 'landspace', 'tag1', 'tag2', 'tag3')
    generic_fk_fields = [{
        'ct_field': 'host_type',
        'fk_field': 'host_id',
        }]
    content_type_whitelist = ('computer', 'cluster')
    # formfield_overrides = {
    #     models.TextField: {'widget': RichTextEditorWidget},
    # }


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
