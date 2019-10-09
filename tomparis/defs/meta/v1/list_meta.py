from tomparis.fields import StringField
from tomparis.model import Model


class ListMeta(Model):
    continue_ = StringField(name="continue")
    resource_version = StringField(name="resourceVersion")
    self_link = StringField(name="selfLink")
