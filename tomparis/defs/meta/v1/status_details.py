from tomparis.fields import IntField, ListField, StringField
from tomparis.model import Model

from .status_cause import StatusCause


class StatusDetails(Model):
    causes = ListField(StatusCause)
    group = StringField()
    kind = StringField()
    name = StringField()
    retry_after_seconds = IntField(name="retryAfterSeconds")
    uid = StringField()
