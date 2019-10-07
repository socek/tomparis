from tomparis.config import Config, Field


class OwnerReference(Config):
    api_version = Field(name="apiVersion")
    block_owner_deletion = Field(name="blockOwnerDeletion")
    controller = Field()
    kind = Field()
    name = Field()
    uid = Field()
