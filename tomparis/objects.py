from tomparis.model import Model
from tomparis.defs.meta.v1 import ObjectMeta
from tomparis.fields import StringField, ModelField


class KubernetesObject(Model):
    api_version = None
    kind = None

    metadata = ModelField(ObjectMeta)
    _api_version = StringField(lambda instance: instance.api_version, name="apiVersion")
    _kind = StringField(lambda instance: instance.kind, name="kind")
