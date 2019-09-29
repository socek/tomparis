from tomparis.config import Config, Field
from tomparis.objects import KubernetesObject


class ServicePort(Config):
    def __init__(self):
        super().__init__()
        self.port = None
        self.target_port = None
        self.protocol = None
        self.name = None

    @Field("port")
    def get_port(self):
        return self.port

    @Field("targetPort")
    def get_target_port(self):
        return self.target_port

    @Field("protocol")
    def get_protocol(self):
        return self.protocol

    @Field("name")
    def get_name(self):
        return self.name


class Service(KubernetesObject):
    api_version = "v1"
    kind = "Service"

    def __init__(self):
        super().__init__()
        self.ports = []
        self.type = None
        self.selector = {}

    def add_port(self, port, target_port, protocol=None, name=None):
        service_port = ServicePort()
        service_port.port = port
        service_port.target_port = target_port
        service_port.protocol = protocol
        service_port.name = name
        self.ports.append(service_port)

    @Field("ports")
    def get_ports(self):
        return self.ports

    @Field("type")
    def get_type(self):
        return self.type

    @Field("selector")
    def get_selector(self):
        return self.selector
