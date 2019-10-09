from tomparis.model import Model, Field


class ServicePort(Model):
    name = Field()
    node_port = Field(name="nodePort")
    port = Field()
    protocol = Field()
    target_port = Field(name="targetPort")
