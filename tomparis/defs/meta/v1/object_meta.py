from uuid import uuid4

from tomparis.model import Model, Field

from .initializers import Initializers


class ObjectMeta(Model):
    annotations = Field(dict)
    cluster_name = Field(name="clusterName")
    creation_timestamp = Field(name="creationTimestamp")
    deletion_grace_period_seconds = Field(name="deletionGracePeriodSeconds")
    deletion_timestamp = Field(name="deletionTimestamp")
    finalizers = Field(list)
    generate_name = Field(name="generateName")
    generation = Field(name="generation")
    initializers = Field(Initializers)
    labels = Field(dict)
    name = Field()
    namespace = Field()
    owner_references = Field(list, name="ownerReferences")  # OwnerReference
    resource_version = Field()
    self_link = Field(name="selfLink")
    uid = Field()

    def _get_uid(self, value):
        if value:
            return value
        elif self.shipment.settings["core"]["autogenerate_uid"]:
            return uuid4().hex
