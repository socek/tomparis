from tomparis.config import Config, Field


class SELinuxOptions(Config):
    level = Field()
    role = Field()
    type = Field()
    user = Field()
