from tomparis.fields import StringField
from tomparis.model import Model


class SELinuxOptions(Model):
    level = StringField()
    role = StringField()
    type = StringField()
    user = StringField()
