from tomparis.defs.meta.v1 import ObjectMeta
from tomparis.fields import DictField
from tomparis.fields import ModelField
from tomparis.fields import StringField
from tomparis.objects import KubernetesObject


class Secret(KubernetesObject):
    api_version = "v1"
    kind = "Secret"

    data = DictField()
    metadata = ModelField(ObjectMeta)
    string_data = DictField(name="stringData")
    type = StringField(default=lambda obj: "Opaque")
