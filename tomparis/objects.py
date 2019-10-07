from tomparis.config import Config, Field
from tomparis.meta import Metadata


class KubernetesObject(Config):
    api_version = None
    kind = None

    metadata = Field(Metadata)
    _api_version = Field(lambda instance: instance.api_version, name="apiVersion")
    _kind = Field(lambda instance: instance.kind, name="kind")
