from tomparis.model import Model, Field

from .env_var_source import EnvVarSource


class EnvVar(Model):
    name = Field()
    value = Field()
    value_from = Field(EnvVarSource, name="valueFrom")
