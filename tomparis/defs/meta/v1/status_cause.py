from tomparis.fields import StringField
from tomparis.model import Model


class StatusCause(Model):
    field = StringField()
    message = StringField()
    reason = StringField()
