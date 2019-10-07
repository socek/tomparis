from tomparis.config import Config, Field

from .status import Status


class Initializers(Config):
    pending = Field(list)  # Initializer
    result = Field(Status)
