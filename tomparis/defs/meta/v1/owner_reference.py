from tomparis.fields import BoolField, StringField
from tomparis.model import Model


class OwnerReference(Model):
    api_version = StringField(name="apiVersion")
    block_owner_deletion = BoolField(name="blockOwnerDeletion")
    controller = BoolField()
    kind = StringField()
    name = StringField()
    uid = StringField()
