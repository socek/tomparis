from tomparis.model import Model, Field


class ContainerPort(Model):
    container_port = Field(name="containerPort")
    host_ip = Field(name="hostIP")
    host_port = Field(name="hostPort")
    name = Field()
    protocol = Field()
