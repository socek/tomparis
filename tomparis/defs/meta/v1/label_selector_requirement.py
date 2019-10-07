from tomparis.config import Config, Field


class LabelSelectorRequirement(Config):
    key = Field()
    operator = Field()
    values = Field(list)
