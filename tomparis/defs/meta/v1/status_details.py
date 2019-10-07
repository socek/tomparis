from tomparis.config import Config, Field


class StatusDetails(Config):
    causes = Field(list)  # StatusCause
    group = Field()
    kind = Field()
    name = Field()
    retry_after_seconds = Field(name="retryAfterSeconds")
    uid = Field()
