from tomparis.fields import PortField, StringField
from tomparis.model import Model


class ContainerPort(Model):
    container_port = PortField(name="containerPort")
    host_ip = StringField(name="hostIP")
    host_port = PortField(name="hostPort")
    name = StringField()
    protocol = StringField()
