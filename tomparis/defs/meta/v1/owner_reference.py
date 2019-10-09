from tomparis.model import Model, Field


class OwnerReference(Model):
    api_version = Field(name="apiVersion")
    block_owner_deletion = Field(name="blockOwnerDeletion")
    controller = Field()
    kind = Field()
    name = Field()
    uid = Field()
