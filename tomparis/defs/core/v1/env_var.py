from tomparis.config import Config, Field

from .env_var_source import EnvVarSource


class EnvVar(Config):
    name = Field()
    value = Field()
    value_from = Field(EnvVarSource, name="valueFrom")
