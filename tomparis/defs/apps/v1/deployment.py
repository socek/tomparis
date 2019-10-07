from tomparis.config import Field
from tomparis.objects import KubernetesObject

from tomparis.defs.meta.v1 import ObjectMeta

from .deployment_spec import DeploymentSpec
from .deployment_status import DeploymentStatus


class Deployment(KubernetesObject):
    api_version = "apps/v1"
    kind = "Deployment"

    metadata = Field(ObjectMeta)
    spec = Field(DeploymentSpec)
    status = Field(DeploymentStatus)

    def add_container(self, container):
        self.spec.template.spec.containers.append(container)

    def add_init_container(self, container):
        self.spec.template.spec.initContainers.append(container)
