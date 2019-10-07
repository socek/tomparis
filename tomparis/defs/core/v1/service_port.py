from tomparis.config import Config, Field


class ServicePort(Config):
    name = Field()
    node_port = Field(name="nodePort")
    port = Field()
    protocol = Field()
    target_port = Field(name="targetPort")
