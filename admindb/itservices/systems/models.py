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

from itservices.models import ITService


class Landspace(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class AbstrSystem(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)
    note = models.TextField(blank=True)
    itservice = models.ForeignKey(ITService)
    landspace = models.ForeignKey(
        Landspace, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


    class Meta:
        abstract = True
        ordering = ['name']


class AbstrVirtualSystem(AbstrSystem):
    """A virtual system references either a computer or a cluster as host.
    """
    content_type = models.ForeignKey(
        ContentType,
        # limit_choices_to={'model': 'Cluster'
        limit_choices_to = models.Q(app_label = 'systems', model = 'Cluster') |
                           models.Q(app_label = 'systems', model = 'Computer')
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return str(self.content_type) + " - " + str(self.content_object)


class VirtualizationTechnology(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class HostInstance(models.Model):
    # continue here - add foreign keys to hostplug
    virtualization_technology = models.ForeignKey(VirtualizationTechnology)


class Computer(AbstrSystem):
    # For using GenericRelations
    # http://voorloopnul.com/blog/using-django-generic-relations/
    def get_content_type(self):
                return ContentType.objects.get_for_model(self).id

    def __str__(self):
        return str(self.name)


class ClusterTechnology(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Cluster(AbstrSystem):
    cluster_technology = models.ForeignKey(ClusterTechnology)
    # For using GenericRelations
    # http://voorloopnul.com/blog/using-django-generic-relations/
    def get_content_type(self):
                return ContentType.objects.get_for_model(self).id


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


class Container(AbstrVirtualSystem):
    virtualization_technology = models.ForeignKey(
        VirtualizationTechnology)  # VServer or LXC, or...


class VM(AbstrVirtualSystem):
    virtualization_technology = models.ForeignKey(
        VirtualizationTechnology)  # KVM

class ImportSystemsAggregated(AbstrSystem):
    """Import mixed systems here and seperate manually.

    If wanting to import mixed VMs, Containers, Devices, etc,
    then put them into here, set tags to group them and finally 
    use DB commands to insert the fields in the correct models.
    """
    tag1 = models.CharField(max_length=75)
    tag2 = models.CharField(max_length=75)
    
