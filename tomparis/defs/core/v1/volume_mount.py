from tomparis.model import Model, Field


class VolumeMount(Model):
    mount_path = Field(name="mountPath")
    mount_propagation = Field(name="mountPropagation")
    name = Field()
    readOnly = Field()
    sub_path = Field()
