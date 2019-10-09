from tomparis.defs.meta.v1 import ObjectMeta
from tomparis.fields import DictField, ModelField
from tomparis.objects import KubernetesObject


class ConfigMap(KubernetesObject):
    api_version = "v1"
    kind = "ConfigMap"
    data = DictField()
    binary_data = DictField(name="binaryData")
    metadata = ModelField(ObjectMeta)
