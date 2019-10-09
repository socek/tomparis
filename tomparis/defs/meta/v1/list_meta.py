from tomparis.model import Model, Field


class ListMeta(Model):
    continue_ = Field(name="continue")
    resource_version = Field(name="resourceVersion")
