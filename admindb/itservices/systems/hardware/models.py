"""Django models definition for App hardware.

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

from django.db import models

from itservices.systems.models import Computer


class CPU(models.Model):
    name = models.CharField(max_length=75)
    vendor = models.CharField(max_length=75)
    arch = models.CharField(max_length=75)
    frequency = models.CharField(max_length=75)
    cores = models.IntegerField()
    computer = models.ForeignKey(Computer)

    def __str__(self):
        return self.name


class RAM(models.Model):
    pass


class Harddisk(models.Model):
    model_name = models.CharField(max_length=75)  # /sys/block/sdx/device/model
    vendor = models.CharField(max_length=75)
    size_sectors = models.IntegerField()  # /sys/block/sdx/size
    sector_size = models.IntegerField()  # /sys/block/sdx/queue/hw_sector_size
    serial = models.CharField(max_length=75)
    revision = models.CharField(max_length=75)


class NIC(models.Model):
    model_name = models.CharField(max_length=75)
    vendor = models.CharField(max_length=75)
    technology = models.CharField(max_length=75)  # Do as foreign key!
    number_ports = models.IntegerField()


class GraphicAdapter(models.Model):
    pass
