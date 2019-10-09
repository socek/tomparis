from tomparis.model import Model, Field

from .status import Status


class Initializers(Model):
    pending = Field(list)  # Initializer
    result = Field(Status)
