from tomparis.fields import ModelField, StringField
from tomparis.model import Model


class ResourceRequirementsElement(Model):
    cpu = StringField()
    memory = StringField()


class ResourceRequirements(Model):
    limits = ModelField(ResourceRequirementsElement)
    requests = ModelField(ResourceRequirementsElement)
