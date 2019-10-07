from tomparis.config import Config, Field

from .list_meta import ListMeta
from .status_details import StatusDetails


class Status(Config):
    api_version = Field(name="apiVersion")
    code = Field()
    details = Field(StatusDetails)
    kind = Field()
    message = Field()
    metadata = Field(ListMeta)
    reason = Field()
    status = Field()
