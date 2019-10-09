from tomparis.model import Model, Field


class StatusDetails(Model):
    causes = Field(list)  # StatusCause
    group = Field()
    kind = Field()
    name = Field()
    retry_after_seconds = Field(name="retryAfterSeconds")
    uid = Field()
