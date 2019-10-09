from tomparis.fields import ListField, ModelField
from tomparis.model import Model

from .initializer import Initializer
from .status import Status


class Initializers(Model):
    pending = ListField(Initializer)
    result = ModelField(Status)
