from tomparis.config import Field
from tomparis.objects import KubernetesObject

from tomparis.defs.meta.v1 import ObjectMeta


class ConfigMap(KubernetesObject):
    api_version = "v1"
    kind = "ConfigMap"
    data = Field(dict)
    binary_data = Field(dict, "binaryData")
    metadata = Field(ObjectMeta)
