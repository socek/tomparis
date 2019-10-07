from tomparis.config import Config, Field


class VolumeMount(Config):
    mount_path = Field(name="mountPath")
    mount_propagation = Field(name="mountPropagation")
    name = Field()
    readOnly = Field()
    sub_path = Field()
