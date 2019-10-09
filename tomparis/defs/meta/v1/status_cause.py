from tomparis.model import Model, Field


class StatusCause(Model):
    field = Field()
    message = Field()
    reason = Field()
