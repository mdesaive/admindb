import django_tables2 as tables
from itservices.systems.models import ImportSystems

class ImportSystemsTable(tables.Table):
        class Meta:
            model = ImportSystems
            # add class="paleblue" to <table> tag
            attrs = {"class": "paleblue"}
            sequence = ("name", "check1", "check2", "description", "group", "itservice", "tag1", "tag2", "tag3")
            exclude = ("id", "note", "landspace", "distribution", "distribution_note", "host", "virtualization_technology", "cluster_technology")
            order_by = ("group", "name")
            orderable = True
            per_page = 200

