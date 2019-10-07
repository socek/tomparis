from tomparis.config import Config, Field


class ResourceRequirementsElement(Config):
    cpu = Field()
    memory = Field()


class ResourceRequirements(Config):
    limits = Field(ResourceRequirementsElement)
    requests = Field(ResourceRequirementsElement)
