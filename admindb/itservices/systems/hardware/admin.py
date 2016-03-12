"""Django Admin configuration for App hardware.

Author: Melanie Desaive
Copyrigh (c) 2016, Melanie Desaive
All rights reserved.

Licensed under the GNU General Public License.
See: COPYING.txt in project root.
"""

from django.contrib import admin

from itservices.systems.hardware.models import CPU
from itservices.systems.hardware.models import Harddisk
from itservices.systems.hardware.models import RAM
from itservices.systems.hardware.models import NIC
from itservices.systems.hardware.models import GraphicAdapter


class CPUAdmin(admin.ModelAdmin):
    list_display = ('name', 'computer', 'vendor', 'arch', 'frequency', 'cores')


admin.site.register(CPU, CPUAdmin)
admin.site.register(Harddisk)
admin.site.register(RAM)
admin.site.register(NIC)
admin.site.register(GraphicAdapter)
