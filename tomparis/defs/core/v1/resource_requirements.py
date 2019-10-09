from tomparis.model import Model, Field


class ResourceRequirementsElement(Model):
    cpu = Field()
    memory = Field()


class ResourceRequirements(Model):
    limits = Field(ResourceRequirementsElement)
    requests = Field(ResourceRequirementsElement)
