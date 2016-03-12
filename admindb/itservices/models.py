"""
Model definition for app itservice.


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


class Type(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


class Distribution(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


class Group(models.Model):
    name = models.CharField(max_length=255)
    short = models.CharField(max_length=8)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ITService(models.Model):
    name = models.CharField(max_length=75, unique=True)
    short = models.CharField(max_length=8)
    description = models.CharField(max_length=255, blank=True)
    group = models.ForeignKey(Group)
    its_type = models.ForeignKey(Type)
    distribution = models.ForeignKey(Distribution)
    distribution_note = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
