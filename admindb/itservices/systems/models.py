"""Django models definition for App systems.

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

from django.db import models
from django.core.exceptions import ValidationError

# Two lines for using generic relations
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Use Django polymorphic.
from polymorphic.models import PolymorphicModel

from itservices.models import ITService
from itservices.models import Group


class Landspace(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class GenericSystem(PolymorphicModel):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)
    note = models.TextField(blank=True)
    itservice = models.ForeignKey(ITService)
    landspace = models.ForeignKey(
        Landspace, blank=True, null=True, on_delete=models.SET_NULL)
    is_host = models.BooleanField()

    def __str__(self):
        return self.name


    class Meta:
        # abstract = True
        ordering = ['name']


class VirtualizationTechnology(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class GenericVirtualSystem(GenericSystem):
    """A virtual system references either a computer or a cluster as host.
    """
    host = models.ForeignKey(GenericSystem, related_name='genericvirtualsystem_host_ptr')
    # host = models.ForeignKey(GenericSystem, related_name='+')
    virtualization_technology = models.ForeignKey(VirtualizationTechnology)

    def __str__(self):
        return str(self.name)



class Computer(GenericSystem):
    def __str__(self):
        return str(self.name)


class ClusterTechnology(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Cluster(GenericSystem):
    cluster_technology = models.ForeignKey(ClusterTechnology)
    computers = models.ManyToManyField(Computer, through='ClusterMapComputer')
    

class ComputerRole(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class ClusterMapComputer(models.Model):
    computer = models.ForeignKey(Computer)
    cluster = models.ForeignKey(Cluster)
    role = models.ForeignKey(ComputerRole)

    def __str__(self):
        return str(self.cluster) + " - " + str(self.computer)


class Container(GenericVirtualSystem):
    pass


class VM(GenericVirtualSystem):
    pass


class ImportSystems(models.Model):
    """Import mixed systems here and seperate manually.

    If wanting to import mixed VMs, Containers, Devices, etc,
    then put them into here, set tags to group them and finally 
    use DB commands to insert the fields in the correct models.

    Would like to inherit from GenericSystem, but some fields
    must be allowed blank and overriding does not work. Maybe
    use django_polymorphic?
    """
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)
    note = models.TextField(blank=True)
    itservice = models.ForeignKey(ITService, blank=True, null=True)
    landspace = models.ForeignKey(
        Landspace, blank=True, null=True, on_delete=models.SET_NULL)

    host = models.ForeignKey(GenericSystem, blank=True, null=True)
    virtualization_technology = models.ForeignKey(
        VirtualizationTechnology,
        blank=True,
        null=True)
    cluster_technology = models.ForeignKey(
        ClusterTechnology,
        blank=True,
        null=True)


    tag1 = models.CharField(max_length=75, blank=True, null=True)
    tag2 = models.CharField(max_length=75, blank=True, null=True)
    tag3 = models.CharField(max_length=75, blank=True, null=True)

    check1 = models.BooleanField(blank=True)
    check2 = models.BooleanField(blank=True)

    group = models.ForeignKey(Group, blank=True, null=True)
    
    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']


