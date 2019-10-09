from tomparis.model import Model, Field


class SELinuxOptions(Model):
    level = Field()
    role = Field()
    type = Field()
    user = Field()
