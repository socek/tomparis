from uuid import uuid4

from tomparis.config import Config, Field


class Metadata(Config):
    name = Field()
    namespace = Field()
    labels = Field(dict)
    annotations = Field(dict)
    creation_timestamp = Field()
    resource_version = Field()
    uid = Field()

    def _get_uid(self, value):
        if value:
            return value
        elif self.shipment.settings["core"]["autogenerate_uid"]:
            return uuid4().hex
