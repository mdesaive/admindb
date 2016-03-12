"""Django models definition for App hardware.

Author: Melanie Desaive
Copyrigh (c) 2016, Melanie Desaive
All rights reserved.

Licensed under the GNU General Public License.
See: COPYING.txt in project root.
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
