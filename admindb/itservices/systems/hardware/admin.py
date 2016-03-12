"""Django Admin configuration for App hardware.

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
