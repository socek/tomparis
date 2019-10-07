from tomparis.config import Config, Field


class ListMeta(Config):
    continue_ = Field(name="continue")
    resource_version = Field(name="resourceVersion")
