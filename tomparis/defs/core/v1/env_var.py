from tomparis.fields import ModelField, StringField
from tomparis.model import Model

from .env_var_source import EnvVarSource


class EnvVar(Model):
    name = StringField()
    value = StringField()
    value_from = ModelField(EnvVarSource, name="valueFrom")
