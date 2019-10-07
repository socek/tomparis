from tomparis.config import Config, Field
from tomparis.defs.meta.v1 import ObjectMeta


class KubernetesObject(Config):
    api_version = None
    kind = None

    metadata = Field(ObjectMeta)
    _api_version = Field(lambda instance: instance.api_version, name="apiVersion")
    _kind = Field(lambda instance: instance.kind, name="kind")
