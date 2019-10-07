from tomparis.config import Field
from tomparis.objects import KubernetesObject


class ConfigMap(KubernetesObject):
    api_version = "v1"
    kind = "ConfigMap"
    data = Field(dict)
