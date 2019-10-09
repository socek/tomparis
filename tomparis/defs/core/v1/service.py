from tomparis.defs.meta.v1 import ObjectMeta
from tomparis.fields import ModelField
from tomparis.model import Field
from tomparis.objects import KubernetesObject

from .service_spec import ServiceSpec


class Service(KubernetesObject):
    api_version = "v1"
    kind = "Service"

    metadata = ModelField(ObjectMeta)
    spec = ModelField(ServiceSpec)
    status = Field(
        dict
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#servicestatus-v1-core
