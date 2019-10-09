from tomparis.fields import (DictField, IntField, ListField, ModelField,
                             StringField)
from tomparis.model import Model

from .initializers import Initializers
from .owner_reference import OwnerReference


class ObjectMeta(Model):
    annotations = DictField()
    cluster_name = StringField(name="clusterName")
    creation_timestamp = StringField(name="creationTimestamp")
    deletion_grace_period_seconds = IntField(name="deletionGracePeriodSeconds")
    deletion_timestamp = StringField(name="deletionTimestamp")
    finalizers = ListField()
    generate_name = StringField(name="generateName")
    generation = IntField(name="generation")
    initializers = ModelField(Initializers)
    labels = DictField()
    name = StringField()
    namespace = StringField()
    owner_references = ListField(OwnerReference, name="ownerReferences")
    resource_version = StringField()
    self_link = StringField(name="selfLink")
    uid = StringField()
