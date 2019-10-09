from tomparis.model import Model, Field

from .list_meta import ListMeta
from .status_details import StatusDetails


class Status(Model):
    api_version = Field(name="apiVersion")
    code = Field()
    details = Field(StatusDetails)
    kind = Field()
    message = Field()
    metadata = Field(ListMeta)
    reason = Field()
    status = Field()
