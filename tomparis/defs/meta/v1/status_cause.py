from tomparis.config import Config, Field


class StatusCause(Config):
    field = Field()
    message = Field()
    reason = Field()
