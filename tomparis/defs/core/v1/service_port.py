from tomparis.model import Model
from tomparis.fields import StringField, PortField


class ServicePort(Model):
    name = StringField()
    node_port = PortField(name="nodePort")
    port = PortField()
    protocol = StringField()
    target_port = PortField(name="targetPort")
