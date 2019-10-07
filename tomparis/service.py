from tomparis.config import Config, Field
from tomparis.objects import KubernetesObject


class ServicePort(Config):
    port = Field()
    target_port = Field(name="targetPort")
    protocol = Field()
    name = Field()


class ServiceSpec(Config):
    ports = Field(list)
    type = Field()
    selector = Field(dict)

    def add_port(self, port, target_port, protocol=None, name=None):
        service_port = ServicePort()
        service_port.port = port
        service_port.target_port = target_port
        service_port.protocol = protocol
        service_port.name = name
        self.ports.append(service_port)


class Service(KubernetesObject):
    api_version = "v1"
    kind = "Service"

    spec = Field(ServiceSpec)
