from tomparis.defs.meta.v1 import ObjectMeta
from tomparis.fields import ModelField
from tomparis.fields import StringField
from tomparis.model import Model


class KubernetesObject(Model):
    api_version = None
    kind = None

    metadata = ModelField(ObjectMeta)
    _api_version = StringField(lambda instance: instance.api_version, name="apiVersion")
    _kind = StringField(lambda instance: instance.kind, name="kind")

    def __init__(self, name: str):
        super().__init__()
        self._name = name

    def prepare(self):
        super().prepare()
        self.metadata.name = self.metadata.name or f"{self.chart.prefix}-{self._name}"
