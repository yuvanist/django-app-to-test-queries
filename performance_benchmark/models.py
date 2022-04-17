from django.db import models
from django.db.models import JSONField
from django.core.serializers.json import DjangoJSONEncoder


class Benchmark(models.Model):
    knowledge_begin_date = models.DateTimeField(null=False)
    knowledge_end_date = models.DateTimeField(null=True)
    client_id = models.IntegerField(null=False)
    databook_id = models.UUIDField(null=False)
    datasheet_id = models.UUIDField(null=False)
    data = JSONField(null=True, encoder=DjangoJSONEncoder)

    # UNCOMMNENT THIS TO CHECK PERFORMANCE WITH INDEX
    # class Meta:
    #     indexes = [
    #         models.Index(
    #             fields=[
    #                 "client_id",
    #                 "-knowledge_end_date",  # latest first index ie, descending order
    #             ]
    #         ),
    #         models.Index(fields=["client_id", "databook_id", "datasheet_id"]),
    #     ]
