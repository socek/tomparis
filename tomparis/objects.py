from tomparis.config import Config, Field
from tomparis.meta import Metadata


class KubernetesObject(Config):
    api_version = None
    kind = None

    def __init__(self):
        super().__init__()
        self.metadata = Metadata()

    @Field("apiVersion")
    def get_api_version(self):
        return self.api_version

    @Field("kind")
    def get_kind(self):
        return self.kind

    @Field("metadata")
    def get_metadata(self):
        return self.metadata
