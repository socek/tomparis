from tomparis.config import Config, Field


class LabelSelectorRequirement(Config):
    key = Field()
    operator = Field()
    values = Field(list)


class LabelSelector(Config):
    match_expressions = Field(LabelSelectorRequirement, name="matchExpressions")
    match_labels = Field(dict, name="matchLabels")
