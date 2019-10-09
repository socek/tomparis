from tomparis.fields import BoolField, StringField
from tomparis.model import Model


class VolumeMount(Model):
    mount_path = StringField(name="mountPath")
    mount_propagation = StringField(name="mountPropagation")
    name = StringField()
    readOnly = BoolField()
    sub_path = StringField()
