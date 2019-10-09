from tomparis.model import Model, Field


class LabelSelectorRequirement(Model):
    key = Field()
    operator = Field()
    values = Field(list)
