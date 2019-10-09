from tomparis.fields import ModelField, StringField
from tomparis.model import Model

from .list_meta import ListMeta
from .status_details import StatusDetails


class Status(Model):
    api_version = StringField(name="apiVersion")
    code = StringField()
    details = ModelField(StatusDetails)
    kind = StringField()
    message = StringField()
    metadata = ModelField(ListMeta)
    reason = StringField()
    status = StringField()
