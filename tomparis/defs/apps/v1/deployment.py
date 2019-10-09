from tomparis.defs.core.v1 import Container
from tomparis.defs.meta.v1 import ObjectMeta
from tomparis.fields import ModelField
from tomparis.objects import KubernetesObject

from .deployment_spec import DeploymentSpec
from .deployment_status import DeploymentStatus


class Deployment(KubernetesObject):
    api_version = "apps/v1"
    kind = "Deployment"

    metadata = ModelField(ObjectMeta)
    spec = ModelField(DeploymentSpec)
    status = ModelField(DeploymentStatus)

    def add_container(self, container: Container):
        self.spec.template.spec.containers.append(container)

    def add_init_container(self, container: Container):
        self.spec.template.spec.initContainers.append(container)
