from tomparis.config import Field
from tomparis.objects import KubernetesObject
from tomparis.defs.meta.v1 import ObjectMeta

from .service_spec import ServiceSpec


class Service(KubernetesObject):
    api_version = "v1"
    kind = "Service"

    metadata = Field(ObjectMeta)
    spec = Field(ServiceSpec)
    status = Field(
        dict
    )  # TODO: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.10/#servicestatus-v1-core
