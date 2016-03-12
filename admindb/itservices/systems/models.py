"""Django models definition for App systems.

Author: Melanie Desaive
Copyrigh (c) 2016, Melanie Desaive
All rights reserved.

Licensed under the GNU General Public License.
See: COPYING.txt in project root.
"""

import pdb

from django.db import models
from django.core.exceptions import ValidationError

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


class VirtualizationTechnology(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class HostPlug(models.Model):

    """HostPlug is single point of reference to either Cluster of Computer.


    Maybe there is a much more intended way to do this.
    """

    def clean(self):
        if self.cluster is not None and self.computer is not None:
            raise ValidationError({'HostPlug':
                                   'HostPlug may only be referenced by' +
                                   'exactly one cluster or one computer,' +
                                   'not both.'})

        if self.cluster is None and self.computer is None:
            raise ValidationError({'HostPlug':
                                   'HostPlug must be referenced by exactly' +
                                   'one cluster or one computer, it may not' +
                                   'be unreferenced.'})

    def __str__(self):
        mycomputer = ""
        mycluster = ""
        if hasattr(self, 'cluster'):
            mycluster = str(self.cluster)
        if hasattr(self, 'computer'):
            mycluster = str(self.computer)

        if mycomputer != "" and mycluster != "":
            retval = "Error: cluster = " + mycluster + " and computer = " + \
                mycomputer
        elif mycomputer == "" and mycluster == "":
            retval = "Error: No reference to computer or cluster: id = " + \
                str(self.id)
        else:
            retval = mycluster or mycomputer
        return retval


class HostInstance(models.Model):
    # continue here - add foreign keys to hostplug
    virtualization_technology = models.ForeignKey(VirtualizationTechnology)


class Computer(AbstrSystem):
    host_plug = models.OneToOneField(HostPlug, on_delete=models.CASCADE,
                                     blank=True)

    def create_host_plug(self):
        return HostPlug.objects.create()

    # Overriding
    def save(self, *args, **kwargs):
        # check if the row with this hash already exists.
        # if not self.host_plug:
        self.host_plug = self.create_host_plug()
        super(Computer, self).save(*args, **kwargs)


class ClusterTechnology(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Cluster(AbstrSystem):
    cluster_technology = models.ForeignKey(ClusterTechnology)
    host_plug = models.OneToOneField(HostPlug, on_delete=models.CASCADE,
                                     blank=True)

    def create_host_plug(self):
        return HostPlug.objects.create()

    # Overriding
    def save(self, *args, **kwargs):
        # check if the row with this hash already exists.
        # if not self.host_plug:
        self.host_plug = self.create_host_plug()
        super(Cluster, self).save(*args, **kwargs)


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


class Container(AbstrSystem):
    virtualization_technology = models.ForeignKey(
        VirtualizationTechnology)  # VServer or LXC, or...
    host = models.ForeignKey(HostPlug)


class VM(AbstrSystem):
    virtualization_technology = models.ForeignKey(
        VirtualizationTechnology)  # KVM
    host = models.ForeignKey(HostPlug)
