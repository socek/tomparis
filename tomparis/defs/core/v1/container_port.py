from tomparis.config import Config, Field


class ContainerPort(Config):
    container_port = Field(name="containerPort")
    host_ip = Field(name="hostIP")
    host_port = Field(name="hostPort")
    name = Field()
    protocol = Field()
