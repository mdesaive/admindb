import django_tables2 as tables
from itservices.models import ITService, Group

class ITServicesTable(tables.Table):
        class Meta:
            model = ITService
            # add class="paleblue" to <table> tag
            attrs = {"class": "paleblue"}
            sequence = ("name", "description", "group")
            exclude = ("id", "short", "its_type", "distribution", "distribution_note")
            order_by = ("group", "name")
            orderable = True
            per_page = 200

class GroupsTable(tables.Table):
        class Meta:
            model = Group
            # add class="paleblue" to <table> tag
            attrs = {"class": "paleblue"}
            sequence = ("name", "description")
            exclude = ("id", "short")
            orderable = True
            order_by = ("name")



