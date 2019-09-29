from tomparis.config import Field
from tomparis.objects import KubernetesObject


class ConfigMap(KubernetesObject):
    api_version = "v1"
    kind = "ConfigMap"

    def __init__(self):
        super().__init__()
        self.data = {}

    @Field("data")
    def get_data(self):
        return self.data
